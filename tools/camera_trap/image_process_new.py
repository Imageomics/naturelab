from megadetector.detection.run_detector_batch import load_and_run_detector_batch
from megadetector.utils import path_utils
import os
import sys
import shutil

# --- Setup ---
if len(sys.argv) < 3:
    print("Usage: python image_process_new.py <image_folder> <output_folder>")
    sys.exit(1)

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.isdir(image_folder):
    print(f"Error: {image_folder} is not a valid directory.")
    sys.exit(1)

os.makedirs(output_folder, exist_ok=True)

# Find all images
all_images = path_utils.find_images(image_folder, recursive=True)
chunk_size = 100

# --- Load the model once ---
# model_path = 'MDV5A'  # Path or identifier for MegaDetector model file
# print(f"Loading MegaDetector model from {model_path}...")
# detector = load_detector(model_path)

total_images_with_animals = 0

# --- Process in chunks ---
for start in range(0, len(all_images), chunk_size):
    end = start + chunk_size
    image_chunk = all_images[start:end]
    print(f"\nProcessing images {start + 1}–{min(end, len(all_images))} of {len(all_images)}")
    
    results = load_and_run_detector_batch('MDV5A', image_chunk)
    
    for result in results:
        file = result["file"]
        detections = result.get("detections", [])
        
        # Check if there is at least one animal detection
        has_animal = any(det["category"] == "1" for det in detections)
        
        if has_animal:
            total_images_with_animals += 1
            
            # Copy the image to the output folder
            shutil.copy2(file, os.path.join(output_folder, os.path.basename(file)))

print(f"\nTotal images containing animals: {total_images_with_animals}")
print(f"Copied to: {output_folder}")
