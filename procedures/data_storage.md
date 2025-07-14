# Data Storage Protocols

At the end of each data collection period, back up all data to OSC. For bioacoustic monitors and camera traps, data will be backed up once SD card is retrieved. For drone missions, data will be backed up after each flight,

## Permanent Data Storage in [OSC](https://osc.edu/)
Use Globus or rsync to backup data to OSC from SD cards or other storage devices. The data will be stored in the following directory structure:

Location: /fs/ess/PAS2136/TheWilds2025

## Directory structure:
```
TheWilds/
├── site_locations.csv
├── field_notes/
│   └── YYYY-MM-DD/
│       └── team_notes.txt
│
├── camera_traps/
│   └── jotform_entries.csv
│   └── [site_id]_[camera_id]/
|           ├── metadata.txt # include any notes about the deployment and the sensor's settings 
│           └── [sd_card_id]_[deploy_date]_[retrieve_date]/
│               └──images/
│                  ├── IMG_001.jpg
│                  ├── IMG_002.jpg
│                  └── ...
│               
│
├── bioacoustics/
|   ├── jotform_entries.csv
│   └── [site_id_sensor_id]/
│       ├── metadata.txt # include any notes about the deployment and the sensor's settings 
│       └── [sd_card_id]_[deploy_date]_[retrieve_date]/
│            └── audio_files/
│                   ├── REC_001.wav
│                   ├── REC_002.wav
│                   └── ...
│                   
│
├── drones/
│   └── YYYYMMDD_dronemodel_[flight_number]/
│       ├── video_files/
│       │   ├── VID_001.mp4
│       │   └── ...
│       └── metadata/
│           ├── mission_notes.txt (include flight objectives, observations, lead and co-pilot, drone used)
│           ├── flight_log.json
│           └── flight_path_map.png
│
└── movement_platform/
    └── deployments/
        └── [deployment_name]_YYYY-MM-DD/
            ├── gps_data/
            │   ├── track_001.gpx
            │   └── ...
            └── metadata/
                ├── deployment_log.csv
                ├── device_settings.txt
                └── battery_log.csv


```
### Metadata Standards
Maintain a metadata file for each sensor deployment collected using Jotform, including:
- Sensor ID
- Deployment date and time
- Retrieval date and time
- GPS coordinates
- Environmental conditions (weather, habitat type)
- Equipment settings (camera model, bioacoustic sensor settings)
- Notes on any issues or anomalies observed during deployment
- Team members involved in deployment and retrieval