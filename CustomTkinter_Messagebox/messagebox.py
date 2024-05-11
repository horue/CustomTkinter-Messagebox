import customtkinter as ct
import winsound
from PIL import Image

def open_sound():
    system_sound_path = "C:\\Windows\\Media\\Windows Notify System Generic.wav"
    winsound.PlaySound(system_sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def messagebox(title='Aviso', text='Placeholder', sound='on'):
    message_box = ct.CTkToplevel()
    message_box.geometry('320x150')
    message_box.title(title)
    message_box.resizable(False, False)
    message_box.attributes('-toolwindow', True, '-topmost', True)
    message_box.grab_set()


    l1 = ct.CTkLabel(message_box, text=text)
    l1.pack(pady=30)


    my_image = ct.CTkImage(light_image=Image.open(r"Visual\Icons\close.png"), dark_image=Image.open(r"Visual\Icons\close.png"),size=(30, 30))

    i1 = ct.CTkLabel(message_box, image=my_image, text="")

    colored_frame = ct.CTkFrame(message_box, height=1)
    colored_frame.pack(side="bottom", fill="x")

    b1 = ct.CTkButton(colored_frame, text='Ok', command=message_box.destroy)
    b1.pack(pady=15)

    if sound == 'on':
        open_sound()
    else:
        pass



root = ct.CTk()
root.geometry("300x200")

button = ct.CTkButton(root, text="Test Button", command=lambda:messagebox(title='Warning!', text='Missing arg'))
button.pack(pady=20)

root.mainloop()