from media_handler import move_document, move_image, move_music, move_video


def yes_button_command(modal, media_type, payload):
    if media_type == "photo":
        print(payload)
        move_image(modal=modal, image=payload, folder=None)
    elif media_type == "video":
        move_video(modal=modal, video=payload, folder=None)
    elif media_type == "music":
        move_music(modal=modal, music=payload, folder=None)
    elif media_type == "document":
        move_document(modal=modal, document=payload, folder=None)

def move_button_command(modal, media_type, payload, destination):
    print(destination)
    if media_type == "photo":
        move_image(modal, image=payload, folder=destination)
    elif media_type == "video":
        move_video(modal, video=payload, folder=destination)
    elif media_type == "music":
        move_music(modal, music=payload, folder=destination)
    elif media_type == "document":
        move_document(modal, document=payload, folder=destination)


def new_button_command(modal, yes_button, new_button, media):
    yes_button.destroy()
    new_button.destroy()
    modal.add_label(text="Enter Folder :", x=10, y=53)
    input = modal.add_text_input()
    modal.add_button(text="move", x=380, y=55, command=lambda: move_button_command(modal, media["type"], media["payload"],  input.get()))