import customtkinter as ct

def messagebox(title='Aviso', text='Placeholder'):
    message_box = ct.CTkToplevel()
    message_box.geometry('320x150')
    message_box.title(title)
    message_box.resizable(False, False)
    message_box.attributes('-toolwindow', True, '-topmost', True)

    l1 = ct.CTkLabel(message_box, text=text)
    l1.pack(pady=30)

    b1 = ct.CTkButton(message_box, text='Ok', command=message_box.destroy)
    b1.pack(pady=15)




root = ct.CTk()
root.geometry("300x200")

# Botão para mostrar a caixa de diálogo personalizada
button = ct.CTkButton(root, text="Test Button", command=lambda:messagebox(title='Warining!'))
button.pack(pady=20)

root.mainloop()