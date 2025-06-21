import os
import shutil
image_path = "C:/Users/Usha/Pictures"
video_path = "C:/Users/Usha/Videos"
music_path = "C:/Users/Usha/Music"
docs_path = "C:/Users/Usha/Document"
zip_path = "C:/Users/Usha/Desktop/zip"


downloads_path = "C:/Users/Usha/Downloads"
# downloads = set(os.listdir(downloads_path))


def move_image(modal, image, folder):
    img = f"C:/Users/Usha/Downloads/{image}"
    try:
        if folder:
            new_img_path = f"C:/Users/Usha/Pictures/{folder}/"
            # Create folder if it doesn't exist
            os.makedirs(new_img_path, exist_ok=True)
            shutil.move(img, os.path.join(new_img_path, os.path.basename(img)))
            modal.destroy()
        else:
            shutil.move(img, image_path)
            modal.destroy()
    except Exception as e:
        print(f"Error: {e}")


def move_video(modal, video, folder):

    vid = f"C:/Users/Usha/Downloads/{video}"
    try:
        if folder:
            new_vid_path = f"C:/Users/Usha/Videos/{folder}"
            # Create folder if it doesn't exist
            os.makedirs(new_vid_path, exist_ok=True)
            shutil.move(vid, os.path.join(new_vid_path, os.path.basename(vid)))
            modal.destroy()
        else:
            shutil.move(vid, video_path)
            modal.destroy()
    except Exception as e:
        print(f"Error: {e}")


def move_document(modal, document, folder):

    docs = f"C:/Users/Usha/Downloads/{document}"
    try:
        if folder:
            new_docs_path = f"C:/Users/Usha/Documents/{folder}"
            # Create folder if it doesn't exist
            os.makedirs(new_docs_path, exist_ok=True)
            shutil.move(docs, os.path.join(new_docs_path, os.path.basename(docs)))
            modal.destroy()
        else:
            shutil.move(docs, docs_path)
            modal.destroy()
    except Exception as e:
        print(f"Error: {e}")


def move_music(modal, music, folder):

    mus = f"C:/Users/Usha/Downloads/{music}"
    try:
        if folder:
            new_music_path = os.makedirs(f"C:/Users/Usha/Music/{folder}")
            # Create folder if it doesn't exist
            os.makedirs(new_music_path, exist_ok=True)
            shutil.move(mus, os.path.join(new_music_path, os.path.basename(mus)))
            modal.destroy()
        else:
            shutil.move(mus, music_path)
            modal.destroy()
    except Exception as e:
        print(f"Error: {e}")


def move_zip(modal, file, folder):
    zip = f"C:/Users/Usha/Downloads/{file}"
    try:
        if folder:
            new_zip_path = f"C:/Users/Usha/Desktop/zip/{folder}/"
            # Create folder if it doesn't exist
            os.makedirs(new_zip_path, exist_ok=True)
            shutil.move(zip, os.path.join(new_zip_path, os.path.basename(zip)))
            modal.destroy()
        else:
            shutil.move(zip, zip_path)
            modal.destroy()
    except Exception as e:
        print(f"Error: {e}")