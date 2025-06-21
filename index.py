import time
import os
from button_handler import yes_button_command, new_button_command
from download_handler import get_media
from gui import window

path = "C:/Users/Usha/Downloads"
# window.title("HouseKeeper")
# window.minsize(width=500, height=300)

def get_downloads():
    return set(os.listdir(path))


downloads = get_downloads()



while True:
    latest_downloads = get_downloads()
    new_files = list(latest_downloads - downloads)

    if new_files:
        modal = window(title="HouseKeeping", width=440, height=88)
        for file in new_files:
            media = get_media(file)

            if media["type"] == "photo":
                modal.add_label(text=f"New image downloaded - Move to Pictures or create new folder?", x=10, y=10)
                yes_button = modal.add_button(text="  Yes  ", x=340, y=55, command=lambda: yes_button_command(modal, media["type"], media["payload"]))
                new_button = modal.add_button(text="  New  ", x=380, y=55, command=lambda: new_button_command(modal, yes_button, new_button, media))
            elif media["type"] == "video":
                print(media["type"])                
                modal.add_label(text=f"new video downloaded /nMove to Videos or create new folder? ", x=5, y=5)
                yes_button = modal.add_button(text="  Yes  ", x=340, y=55, command=lambda: yes_button_command(modal, media["type"], media["payload"]))
                new_button = modal.add_button(text="  New  ", x=380, y=55, command=lambda: new_button_command(modal, yes_button, new_button, media))

            elif media["type"] == "music":
                modal.add_label(text=f"new music downloaded /nMove to Musics or create new folder? ", x=5, y=5)
                yes_button = modal.add_button(text="  Yes  ", x=340, y=55, command=lambda: yes_button_command(modal, media["type"], media["payload"]))
                new_button = modal.add_button(text="  New  ", x=380, y=55, command=lambda: new_button_command(modal, yes_button, new_button, media))

            elif media["type"] == "document":
                modal.add_label(text=f"new document downloaded /nMove to Documents or create new folder? ", x=5, y=5)
                yes_button = modal.add_button(text="  Yes  ", x=340, y=55, command=lambda: yes_button_command(modal, media["type"], media["payload"]))
                new_button = modal.add_button(text="  New  ", x=380, y=55, command=lambda: new_button_command(modal, yes_button, new_button, media))

            else:
                modal.add_label(text=f"new unknown file downloaded /nMove to Recycle bin or create new folder? ", x=5, y=5)
                yes_button = modal.add_button(text="  Yes  ", x=340, y=55, command=lambda: yes_button_command(modal, media["type"], media["payload"]))
                new_button = modal.add_button(text="  New  ", x=380, y=55, command=lambda: new_button_command(modal, yes_button, new_button, media))

        # update the downloads to the latest state
        modal.mainloop()
        downloads = latest_downloads
    time.sleep(1)