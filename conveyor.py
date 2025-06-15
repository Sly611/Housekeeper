import os
import shutil

destination_path = "C:/Users/Usha/Pictures/junk"

downloads_path = "C:/Users/Usha/Downloads"
downloads = set(os.listdir(downloads_path))

def extract_images(list):
    valid_extentions = [".jpeg", ".PNG", ".png", ".JPEG", ".jpg", ".JPG", ".gif", ".GIF", ".tiff", ".tif"]
    pictures = []
    for media in list:
        file_extention = os.path.splitext(media)[1]
        if file_extention in valid_extentions:
            # print(file_extention)
            pictures.append(media)

    return pictures

def move_image(list):
    try:
        for media in list:
            image = f"C:/Users/Usha/Downloads/{media}"
            print(image)
            shutil.move(image, destination_path)
    except Exception as e:
        print(f"Error: {e}")


pics = extract_images(downloads)
move_image(pics)