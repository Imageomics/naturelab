# Data Storage Protocols

At the end of each data collection period, back up all data to OSC. For bioacoustic monitors and camera traps, data will be backed up once SD card is retrieved. For drone missions, data will be backed up after each flight.

## Permanent Data Storage in [OSC](https://osc.edu/)
Use Globus or rsync to backup data to OSC from SD cards or other storage devices. The data will be stored in the following directory structure:

Location: /fs/ess/PAS2136/TheWilds2025

Directory structure:
```
TheWilds2025/
├── camera_traps
│   ├── camera_trap_1
│       ├── images
│       └── metadata
│   ├── camera_trap_2
│   └── ...
├── audio_moths
│   ├── audio_moth_1
│        ├── audio files
│        └──metadata
│   ├── audio_moth_2
│   └── ...
├── gps_data
│   ├── moovement_platform
│       ├── gps_data
│       └── metadata
│   └── ...
├── drone_lidar
│   ├── drone_lidar_1
│       ├── lidar_data
│       └── metadata (includes telemetry data)
│   ├── drone_lidar_2
│   └── ...
├── drone_video
│   ├── drone_video_1
│       ├── video_files
│       └── metadata (includes telemetry data)
│   ├── drone_video_2
│   └── ...


```

Metadata files include location, date, time, and sensor specifications. Each sensor type has its own directory for organization.
