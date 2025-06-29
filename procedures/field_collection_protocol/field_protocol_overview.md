# Field Collection Protocol Overview

## Field Safety & Best Practices

- Always inform supervisor of field schedule and expected return
- Carry communication device (cell phone/radio)
- Work in pairs when possible
- Be aware of wildlife activity and seasonal considerations
- Follow all Wilds safety protocols and vehicle operation procedures
- Weather monitoring - avoid deployments during severe weather
- Respect all facility rules regarding animal enclosures and restricted areas

### In the event of an emergency
- Follow established emergency protocols.
- Ensure all team members are accounted for and safe.
- Contact emergency services if necessary.
- Document the incident and report it to the Team Lead.

## Pre-deployment Preparation
   - Review and understand all field collection protocols.
   - Ensure all equipment is packed and in working order.
   - Charge all batteries and pack spares.
   - Format SD cards and label them with unique IDs.
   - Access Jotform for data entry, with a paper backup.
   - Confirm team roles and responsibilities.
   - Download all apps and tools needed for data collection and communication.

      Required apps include:
     - Jotforms: ensure logs in Offline mode for data entry.
     - SM Config for configuring bioacoustic sensors.

     Optional:
     - DJI Fly and FreeFlight Pro for drone operations.
     - Reveal and COMMANS apps for smart camera traps.
     - Merlin Bird ID for bird identification.
     - iNaturalist for species identification and logging.

## Photography and Documentation
Team members are encouraged to take photos of the field site, equipment setup, and any notable wildlife encounters. These photos should be uploaded to the appropriate directories in OSC and referenced in Jotform entries.


## Site Identification and Mapping
### Location Selection
- Use GPS to identify and mark locations for camera traps and bioacoustic sensors.
- Ensure locations cover diverse habitats and wildlife corridors.
- Create a map of the field site with marked locations for each team.
- Record reasoning behind site selection, including habitat features and expected wildlife activity in the field log.

### Site Location Log
Maintain a log with the following details for each site:
- Site ID
- Descriptive name
- GPS coordinates
- Habitat description
- Reason for selection
- Access notes
- Deployment history with dates and equipment used
- Any special considerations (e.g., seasonal wildlife activity, weather conditions)


### Naming Conventions
   - **Site ID:** Use a consistent format (e.g., "TW-001" for The Wilds site 1).
   - **Camera Trap ID:** Combine site ID with camera number (e.g., "TW-001-CT01").
   - **Sound Meter ID:** Combine site ID with sensor number (e.g., "TW-001-SM01").
   - **SD Card ID:** Use a unique identifier for each SD card (e.g., "SD001", "SD002").
   - **Date Format:** Use YYYYMMDD for all date entries (e.g., 20240615 for June 15, 2024).
   - **Time Format:** Use 24-hour format (e.g., 1430 for 2:30 PM).

## Team Roles and Responsibilities
Work in pairs, one person handling setup and maintenance, the other documenting data. Rotate roles as needed.

**Team Lead:** Oversees the entire field operation, ensures protocols are followed, and manages communication with external parties.
   
**Data Manager:** Responsible for data collection, maintaining field log, entry into Jotform, and ensuring data integrity.

---
   
**Camera Trap Set Up:** Handles the deployment, maintenance, and retrieval of camera traps.
   
**Camera Trap Documenter:** Records all relevant information about camera trap deployments and maintenance in Jotform or field notebook.

---

**Bioacoustic Sensor Set Up:** Manages the deployment, maintenance, and retrieval of bioacoustic sensors.

**Bioacoustic Sensor Documenter:** Records all relevant information about bioacoustic sensor deployments and maintenance in Jotform or field notebook.

---

**Lead Pilot (if drones are used):** Responsible for the safe operation of the drone, including pre-flight checks and flight execution.

**Pilot Assistant:** Assists the Lead Pilot with situational awareness, including monitoring airspace, ground conditions, and wildlife. Handles communication between the Lead Pilot and third parties.
 
 **Ground Crew:** Assists with equipment setup, packing, and other logistical tasks, and ensures the safety of the operational area by monitoring for ground obstacles and wildlife.

## Assign Locations to Each Crew
- Divide the field site into zones, assigning each team to specific areas for camera traps and bioacoustic sensors.
- Ensure each team has a map and GPS coordinates for their assigned locations.
- Rotate teams between zones as needed to ensure comprehensive coverage of the field site.
- Determine rally points and times for teams to regroup and share data.

## Post-Fieldwork
- Complete any remaining data entry and ensure all records are accurate and complete. Back up all data to OSC using Globus or rsync. Refer to the Data Transfer & Storage instructions for detailed steps. IMPORTANT: Make sure the files are editable by all team members and properly organized in the directory structure:
  ```bash
  # Navigate to the data directory first
  cd /fs/ess/PAS2136/TheWilds2025
  
  # Set permissions for the specific data directories
  chmod -R 775 camera_traps/ bioacoustic_data/ field_notes/
  ```
- Ensure all Jotform entries are completed and submitted.
- Verify that all equipment is accounted for and in good working condition.
- Conduct a debrief with the team to discuss what went well and what could be improved for future fieldwork.
- Prepare a summary report of the fieldwork activities and findings.





