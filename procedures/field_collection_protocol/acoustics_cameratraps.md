# Bioacoustic and Camera Trap Data Collection Protocol
*Adapted from fieldwork protocols developed by the Koa team for the 2025 Experiential Introduction to AI and Biodiversity course, in collaboration with NEON, ABC Center, and Imageomics.*


### Field Protocol Overview

**Equipment per deployment:**
- Camera traps with paired SD cards
- AudioMoth bioacoustic sensors with paired SD cards
- GPS unit
- Zip ties for mounting to fence posts and trees
- Spare equipment (camera traps, AudioMoths, batteries, SD cards)
- Field notebook and pencil
- Multi-tool/wrench set
- Multimeter for battery testing

### Site Setup (Initial Deployment)

#### Camera Trap Deployment
1. **Site Selection & Setup**
   - Select monitoring locations based on wildlife corridors, water sources, and habitat features. Confirm with conservation experts at The Wilds.
    - Ensure site is accessible and safe for equipment deployment
   - Mount camera traps at eye-level (approximately 5 feet) on fence posts or trees using zip ties
   - Clear vegetation from detection zone (approximately 10-15 feet in front of camera)
   - Record GPS coordinates, habitat type, and mounting details in field notebook, and back up CSV to OSC.

2. **Camera Configuration** (TO BE FINALIZED)
   - Set date/time: Navigate to settings using up/down arrows
   - Configuration sequence: Time → Date → Photo burst (3 photos) → Delay (00:15) → Sensitivity (HI) → Detection mode (dEFN) → Format (FOrN)
   - Test trigger by waving hand in front of sensor
   - Record camera ID and SD card pairing in field notebook, and back up CSV to OSC.

#### AudioMoth Deployment
1. **Site Selection**
   - Place AudioMoths to capture diverse acoustic environments
   - Mount at eye-level (approximately 5 feet) on fence posts or trees using zip ties
   - Ensure microphone points away from prevailing wind direction
   - Avoid areas with excessive mechanical noise (roads, equipment)
   - Select sites to mount AudioMoths in same location as camera traps.

2. **AudioMoth Configuration**
   - Set recording schedule based on target species activity patterns
   - Configure portion of monitors to sample rate to record 5 minutes every hour, on the hour.
   - Configure portion of monitors to record 1 hour in the morning and 1 hour in the evening.
   - Test recording function before final deployment
   - Record serial number, GPS coordinates, and deployment details in field notebook, and back up CSV to OSC.

### Regular Maintenance Protocol

#### Camera Trap SD Card Replacement

**At each camera location:**
1. Approach camera and record location ID in field notebook
2. Wave hand in front of camera to mark end of collection period
3. Turn camera off (slide switch to bottom position)
4. Remove SD card and record:
   - Camera ID
   - SD card ID
   - Date and time removed
   - Battery status
5. Insert fresh SD card from paired set
6. Record new SD card ID
7. Turn camera on and set current date/time
8. Wait 15 seconds for initialization (red light stops flashing)
9. Test trigger with hand wave

#### AudioMoth SD Card Replacement

**At each AudioMoth location:**
1. Locate AudioMoth using GPS coordinates
2. Turn device off using switch
3. Remove SD card and record:
   - AudioMoth serial number
   - SD card ID
   - Date and time removed
   - Battery voltage (if display available)
4. Insert fresh SD card
5. Turn device on and verify recording status (LED indicators)
6. Record new SD card ID and deployment time

#### Equipment Checks

**Camera Traps:**
- Remove spider webs and debris from lens and sensor
- Check battery level (replace if low/dead)
- Tighten mounting if loose
- Verify detection zone is clear

**AudioMoths:**
- Check for water damage in housing
- Verify microphone is unobstructed
- Test battery level
- Ensure secure mounting

### Data Management

#### Naming Conventions

**Site Identification:** (TO FINALIZE)
- Use descriptive site codes (e.g., NP = North Pasture, SF = South Forest, WP = Wetland Pond)
- Number stations within sites (NP1, NP2, etc.)

**Camera Trap Labels:**
- Format: [Site ID]-CT[##] (e.g., NP-CT01, SF-CT12)

**AudioMoth Labels:**
- Format: [Site ID]-AM[##] (e.g., NP-AM01, SF-AM03)

**SD Card Identification:**
- Camera SD cards: [Color]-[Size]-[Number]-[A/B] (e.g., R-64-01-A)
- AudioMoth SD cards: AM-[Size]-[Number]-[A/B] (e.g., AM-32-05-B)

#### Folder Structure
```
TheWilds/
├── Camera-traps/
│   └── [SiteID-camera-label]/
│       └── [sd_card_id_datein_dateout]/
│           └── [date-label]-[sequence]/
├── Bioacoustics/
│   └── [Serial-number]/
│       └── [site_id]-[YYYY-MM-DD-DD]/
├── Metadata/
│   ├── camera_trap_deployments.csv
│   ├── camera_trap_sd_cards.csv
│   ├── audiomoth_deployments.csv
│   ├── audiomoth_sd_cards.csv
│   └── site_locations.csv
└── Field-notes/
    └── [YYYY-MM-DD]/
```

#### Required Metadata Spreadsheets

**Camera Trap Deployment Log:**
- Camera ID, Site ID, GPS coordinates, habitat type, mounting height, deployment date, retrieval date, notes

**Camera SD Card Log:**
- SD card ID, Camera ID, date/time inserted, date/time removed, battery status, data quality notes

**AudioMoth Deployment Log:**
- AudioMoth serial number, Site ID, GPS coordinates, mounting height, deployment date, retrieval date, recording schedule, notes

**AudioMoth SD Card Log:**
- SD card ID, AudioMoth serial number, date/time inserted, date/time removed, battery voltage, recording quality notes

**Site Location Master:**
- Site ID, descriptive name, GPS coordinates, habitat description, access notes, deployment history

### Field Safety & Best Practices

- Always inform supervisor of field schedule and expected return
- Carry communication device (cell phone/radio)
- Work in pairs when possible
- Be aware of wildlife activity and seasonal considerations
- Follow all Wilds safety protocols and vehicle operation procedures
- Weather monitoring - avoid deployments during severe weather
- Respect all facility rules regarding animal enclosures and restricted areas

### Data Transfer & Storage

1. **Immediate Processing:**
   - Transfer SD card data to secure storage upon return from field
   - Verify file integrity and completeness
   - Update metadata spreadsheets
   - Format SD cards for next deployment

2. **Data Backup:**
   - Maintain multiple copies of all data
   - Follow institutional data management protocols
   - Regular backup verification

3. **Quality Control:**
   - Review sample of images/recordings for equipment function
   - Note any issues with specific cameras or AudioMoths
   - Schedule maintenance as needed

### Troubleshooting

**Camera Issues:**
- No photos: Check battery, SD card seating, detection settings
- Blurry images: Clean lens, check for condensation
- Inconsistent triggering: Adjust sensitivity, clear detection zone

**AudioMoth Issues:**
- No recordings: Verify battery, SD card, recording schedule
- Poor audio quality: Check microphone obstruction, gain settings
- Shortened recording periods: Monitor battery drain, temperature effects

### Seasonal Considerations

- **Spring/Summer:** Increased vegetation growth requiring more frequent site maintenance
- **Fall/Winter:** Battery performance monitoring, weather protection checks
- **Year-round:** Adjust recording schedules based on target species activity patterns

---

*This protocol should be reviewed and updated based on site-specific conditions and research objectives at The Wilds.*