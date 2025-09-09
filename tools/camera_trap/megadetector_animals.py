from megadetector.detection.run_detector_batch import load_and_run_detector_batch
from megadetector.utils import path_utils
import os

# --- Setup ---
image_folder = "/Volumes/GARDEPRO/DCIM/127MEDIA"
all_images = path_utils.find_images(image_folder, recursive=True)

chunk_size = 100

# --- Process in chunks ---
for start in range(0, len(all_images), chunk_size):
    end = start + chunk_size
    image_chunk = all_images[start:end]
    
    print(f"\n Processing images {start + 1}–{min(end, len(all_images))} of {len(all_images)}")
    
    results = load_and_run_detector_batch('MDV5A', image_chunk)

    for result in results:
        file = result["file"]
        detections = result.get("detections", [])
        num_animals = sum(1 for det in detections if det["category"] == "1")
        print(f"{os.path.basename(file)}: {num_animals} animal(s) detected")