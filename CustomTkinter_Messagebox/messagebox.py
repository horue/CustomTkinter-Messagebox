import customtkinter as ct
import winsound

def open():
    system_sound_path = "C:\\Windows\\Media\\Windows Notify System Generic.wav"
    winsound.PlaySound(system_sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def messagebox(title='Aviso', text='Placeholder'):
    message_box = ct.CTkToplevel()
    message_box.geometry('320x150')
    message_box.title(title)
    message_box.resizable(False, False)
    message_box.attributes('-toolwindow', False, '-topmost', True)
    message_box.grab_set()


    l1 = ct.CTkLabel(message_box, text=text)
    l1.pack(pady=30)

    b1 = ct.CTkButton(message_box, text='Ok', command=message_box.destroy)
    b1.pack(pady=15)

    open()



root = ct.CTk()
root.geometry("300x200")

# Botão para mostrar a caixa de diálogo personalizada
button = ct.CTkButton(root, text="Test Button", command=lambda:messagebox(title='Warning!', text='Missing arg'))
button.pack(pady=20)

root.mainloop()