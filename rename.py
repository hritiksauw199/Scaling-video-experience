import os

# Path to the folder containing images
folder_path = "./images/potrait/faces"

# List all jpeg files
images = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpeg")]

# Sort to have consistent ordering before renaming
images.sort()

# Iterate and rename
for idx, img in enumerate(images, start=1):
    old_path = os.path.join(folder_path, img)
    new_name = f"P_faces_{idx}.jpeg"
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print(f"Renamed {len(images)} images successfully!")