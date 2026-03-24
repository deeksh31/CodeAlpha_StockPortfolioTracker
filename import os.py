import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    try:
        if not os.path.exists(source_folder):
            print("❌ Source folder does not exist!")
            return

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for file in os.listdir(source_folder):
            if file.endswith(".jpg"):
                source_path = os.path.join(source_folder, file)
                destination_path = os.path.join(destination_folder, file)

                shutil.move(source_path, destination_path)
                print(f"Moved: {file}")

        print("✅ Done!")
        

    except Exception as e:
        print("❌ Error:", e)

# ✅ Correct paths here
source = "C:/Users/hp/Desktop/images"
destination = "C:/Users/hp/Desktop/jpg_files"

move_jpg_files(source, destination)