from megadetector.detection.run_detector_batch import load_and_run_detector_batch
from megadetector.utils import path_utils
import os
# --- Setup ---
image_folder = "/Volumes/GARDEPRO/DCIM/101MEDIA"
all_images = path_utils.find_images(image_folder, recursive=True)
chunk_size = 100
min_conf = 0.05  # raie this to be less sensitive (e.g., 0.8), lower to be more sensitive
# --- Process in chunks ---
for start in range(0, len(all_images), chunk_size):
    end = start + chunk_size
    image_chunk = all_images[start:end]
    print(f"\nProcessing images {start + 1}–{min(end, len(all_images))} of {len(all_images)}")
    # Only detections with conf >= min_conf will be returned
    results = load_and_run_detector_batch(
        'MDV5A',
        image_chunk,
        confidence_threshold=min_conf
    )
    for result in results:
        file = result["file"]
        detections = result.get("detections", [])
        # Category "1" = animal in MD
        num_animals = sum(1 for det in detections if det.get("category") == "1")
        print(f"{os.path.basename(file)}: {num_animals} animal(s) detected at ≥{min_conf:.2f} conf")