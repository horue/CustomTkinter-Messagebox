import customtkinter as ct
import winsound
from PIL import Image

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width) // 2
    y = (screen_height) // 2
    window.geometry(f"+{x}+{y}")

def open_sound():
    system_sound_path = "C:\\Windows\\Media\\Windows Notify System Generic.wav"
    winsound.PlaySound(system_sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)


class CTkMessagebox():
    def messagebox(title='CustomTKinterMessagebox!', 
                   text='Messagebox is working!', 
                   sound='on', 
                   button_text='OK', 
                   size='320x150', 
                   center=True,
                   top=True):
        message_box = ct.CTkToplevel()
        message_box.geometry(size)
        message_box.title(title)
        message_box.resizable(False, False)
        message_box.attributes('-toolwindow', True, '-topmost', top)
        message_box.grab_set()

        if center == True:
            center_window(message_box)
        else:
            pass


        l1 = ct.CTkLabel(message_box, text=text)
        l1.pack(pady=30)

        colored_frame = ct.CTkFrame(message_box, height=1)
        colored_frame.pack(side="bottom", fill="x")

        b1 = ct.CTkButton(colored_frame, text=button_text, command=message_box.destroy)
        b1.pack(pady=15)

        if sound == 'on':
            open_sound()
        else:
            pass



"""root = ct.CTk()
root.geometry("300x200")

nome = 'Calin'
button = ct.CTkButton(root, text="Test Button", command=lambda:Messagebox.CTkMessagebox(title='Warning!', text='Error.'))
button.pack(pady=20)

root.mainloop()"""