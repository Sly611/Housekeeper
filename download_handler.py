import os
from media_handler import move_document, move_image, move_music, move_video

img_extentions = [".jpeg", ".PNG", ".png", ".JPEG", ".jpg", ".JPG", ".gif", ".GIF", ".tiff", ".tif"]
vid_extentions = [".mp4", ".MP4", ".avi", ".mov", ".wmv", ".mkv", ".mpg", ".mpeg", ".m4v", ".rm"]
mus_extensions = [".mp3", ".wav", ".flac", ".m4a", ".wma", ".ape", ".aac", ".opus", ".ogg"]
doc_extensions = [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".rtf", ".ppt", ".pptx", ".ods", ".odp"]


def get_media(media):
    media_type = os.path.splitext(media)[1]
    if media_type in img_extentions:
        return {"type": "photo", "payload": media}
    elif media_type in vid_extentions:
        return {"type": "video", "payload": media}
    elif media_type in mus_extensions:
        return {"type": "music", "payload": media}
    elif media_type in doc_extensions:
        return {"type": "document", "payload": media}
    else:
        return {"type": "unknown", "payload": media}


