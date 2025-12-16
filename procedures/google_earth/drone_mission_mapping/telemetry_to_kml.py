#!/usr/bin/env python3
"""
Drone Telemetry to KML Converter
Converts JSON telemetry files from drone missions to KML format for Google Earth
"""

import json
import os
import sys
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from datetime import datetime, timedelta

def create_kml_from_telemetry(json_file, output_file=None):
    """
    Convert drone telemetry JSON to KML format
    
    Args:
        json_file (str): Path to input JSON telemetry file
        output_file (str): Path to output KML file (optional)
    """
    
    # Generate output filename if not provided
    if output_file is None:
        base_name = os.path.splitext(json_file)[0]
        output_file = f"{base_name}_flight_path.kml"
    
    # Read JSON telemetry data
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return False
    
    # Extract headers and data
    headers = data.get('details_headers', [])
    telemetry_data = data.get('details_data', [])
    
    if not headers or not telemetry_data:
        print("No telemetry data found in JSON file")
        return False
    
    # Find relevant column indices
    try:
        time_idx = headers.index('time')
        drone_lat_idx = headers.index('product_gps_latitude')
        drone_lon_idx = headers.index('product_gps_longitude')
        altitude_idx = headers.index('altitude')
        battery_idx = headers.index('battery_level')
        flying_state_idx = headers.index('flying_state')
        speed_idx = headers.index('speed') if 'speed' in headers else None
    except ValueError as e:
        print(f"Required GPS columns not found: {e}")
        return False
    
    # Create KML structure
    kml = Element('kml')
    kml.set('xmlns', 'http://www.opengis.net/kml/2.2')
    
    document = SubElement(kml, 'Document')
    SubElement(document, 'name').text = f'Drone Flight - {os.path.basename(json_file)}'
    SubElement(document, 'description').text = f'Flight path extracted from {json_file}'
    
    # Add styles for different flight states
    add_flight_styles(document)
    
    # Create flight path
    create_flight_path(document, headers, telemetry_data, time_idx, drone_lat_idx, 
                      drone_lon_idx, altitude_idx)
    
    # Create waypoints with detailed info
    create_waypoints(document, headers, telemetry_data, time_idx, drone_lat_idx, 
                    drone_lon_idx, altitude_idx, battery_idx, flying_state_idx, speed_idx)
    
    # Write KML file
    try:
        rough_string = tostring(kml, 'unicode')
        reparsed = minidom.parseString(rough_string)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(reparsed.toprettyxml(indent="  "))
        
        print(f"KML file created successfully: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error writing KML file: {e}")
        return False

def add_flight_styles(document):
    """Add style definitions for different flight elements"""
    
    # Flight path style
    path_style = SubElement(document, 'Style')
    path_style.set('id', 'flightPath')
    line_style = SubElement(path_style, 'LineStyle')
    SubElement(line_style, 'color').text = 'ff0000ff'  # Red line
    SubElement(line_style, 'width').text = '3'
    
    # Takeoff point style
    takeoff_style = SubElement(document, 'Style')
    takeoff_style.set('id', 'takeoffPoint')
    icon_style = SubElement(takeoff_style, 'IconStyle')
    SubElement(icon_style, 'color').text = 'ff00ff00'  # Green
    SubElement(icon_style, 'scale').text = '1.2'
    icon = SubElement(icon_style, 'Icon')
    SubElement(icon, 'href').text = 'http://maps.google.com/mapfiles/kml/shapes/airports.png'
    
    # Landing point style
    landing_style = SubElement(document, 'Style')
    landing_style.set('id', 'landingPoint')
    icon_style = SubElement(landing_style, 'IconStyle')
    SubElement(icon_style, 'color').text = 'ff0000ff'  # Red
    SubElement(icon_style, 'scale').text = '1.2'
    icon = SubElement(icon_style, 'Icon')
    SubElement(icon, 'href').text = 'http://maps.google.com/mapfiles/kml/shapes/airports.png'
    
    # Waypoint style
    waypoint_style = SubElement(document, 'Style')
    waypoint_style.set('id', 'waypoint')
    icon_style = SubElement(waypoint_style, 'IconStyle')
    SubElement(icon_style, 'color').text = 'ffffff00'  # Yellow
    SubElement(icon_style, 'scale').text = '0.8'

def create_flight_path(document, headers, data, time_idx, lat_idx, lon_idx, alt_idx):
    """Create the main flight path line"""
    
    placemark = SubElement(document, 'Placemark')
    SubElement(placemark, 'name').text = 'Flight Path'
    SubElement(placemark, 'styleUrl').text = '#flightPath'
    
    linestring = SubElement(placemark, 'LineString')
    SubElement(linestring, 'extrude').text = '1'
    SubElement(linestring, 'tessellate').text = '1'
    SubElement(linestring, 'altitudeMode').text = 'relativeToGround'
    
    coordinates = SubElement(linestring, 'coordinates')
    
    # Build coordinate string
    coord_list = []
    for row in data:
        try:
            lon = float(row[lon_idx])
            lat = float(row[lat_idx])
            alt = float(row[alt_idx]) if row[alt_idx] else 0
            
            # Only add valid GPS coordinates
            if -180 <= lon <= 180 and -90 <= lat <= 90:
                coord_list.append(f"{lon},{lat},{alt}")
        except (ValueError, IndexError):
            continue
    
    coordinates.text = '\n'.join(coord_list)

def create_waypoints(document, headers, data, time_idx, lat_idx, lon_idx, alt_idx, 
                    battery_idx, flying_state_idx, speed_idx):
    """Create waypoint markers with flight information"""
    
    # Flying state meanings (common for Parrot drones)
    flying_states = {
        0: "Landed",
        1: "Taking Off", 
        2: "Hovering",
        3: "Flying",
        4: "Landing",
        5: "Emergency",
        6: "User Takeoff",
        7: "Motor Ramping"
    }
    
    # Create folder for waypoints
    folder = SubElement(document, 'Folder')
    SubElement(folder, 'name').text = 'Flight Waypoints'
    SubElement(folder, 'description').text = 'Detailed flight information at key points'
    
    # Sample waypoints (every 10th point to avoid clutter)
    sample_interval = max(1, len(data) // 20)  # Max 20 waypoints
    
    for i in range(0, len(data), sample_interval):
        row = data[i]
        
        try:
            lon = float(row[lon_idx])
            lat = float(row[lat_idx])
            alt = float(row[alt_idx]) if row[alt_idx] else 0
            
            # Skip invalid coordinates
            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                continue
            
            time_ms = row[time_idx]
            battery = row[battery_idx]
            flying_state = row[flying_state_idx]
            speed = row[speed_idx] if speed_idx else 0
            
            # Create waypoint
            placemark = SubElement(folder, 'Placemark')
            
            # Determine style based on position
            if i == 0:
                SubElement(placemark, 'name').text = 'Takeoff'
                SubElement(placemark, 'styleUrl').text = '#takeoffPoint'
            elif i == len(data) - sample_interval:
                SubElement(placemark, 'name').text = 'Landing'
                SubElement(placemark, 'styleUrl').text = '#landingPoint'
            else:
                SubElement(placemark, 'name').text = f'Waypoint {i//sample_interval + 1}'
                SubElement(placemark, 'styleUrl').text = '#waypoint'
            
            # Create description with flight data
            description = f"""
            <![CDATA[
            <b>Time:</b> {time_ms/1000:.1f}s<br/>
            <b>Altitude:</b> {alt:.1f}m<br/>
            <b>Battery:</b> {battery}%<br/>
            <b>Flying State:</b> {flying_states.get(flying_state, f'Unknown ({flying_state})')}<br/>
            <b>Speed:</b> {speed:.1f}m/s<br/>
            <b>Coordinates:</b> {lat:.6f}, {lon:.6f}
            ]]>
            """
            SubElement(placemark, 'description').text = description
            
            # Add point geometry
            point = SubElement(placemark, 'Point')
            SubElement(point, 'altitudeMode').text = 'relativeToGround'
            SubElement(point, 'coordinates').text = f"{lon},{lat},{alt}"
            
        except (ValueError, IndexError):
            continue

def process_multiple_files(directory):
    """Process all JSON files in a directory"""
    
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    if not json_files:
        print(f"No JSON files found in {directory}")
        return
    
    print(f"Found {len(json_files)} JSON files")
    
    for json_file in json_files:
        file_path = os.path.join(directory, json_file)
        print(f"Processing: {json_file}")
        
        success = create_kml_from_telemetry(file_path)
        if success:
            print(f"  ✓ Converted successfully")
        else:
            print(f"  ✗ Conversion failed")

def main():
    """Main function to handle command line arguments"""
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python telemetry_to_kml.py <telemetry.json>")
        print("  Directory:   python telemetry_to_kml.py <directory>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if os.path.isfile(input_path):
        # Process single file
        create_kml_from_telemetry(input_path)
    elif os.path.isdir(input_path):
        # Process all JSON files in directory
        process_multiple_files(input_path)
    else:
        print(f"Error: {input_path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()