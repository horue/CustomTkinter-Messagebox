import customtkinter as ct

def messagebox(title='Aviso'):
    message_box = ct.CTkToplevel()
    message_box.geometry('320x150')
    message_box.title(title)
    message_box.resizable(False, False)
    message_box.attributes('-toolwindow', True, '-topmost', True)

    b1 = ct.CTkButton(message_box, text='Ok', command=message_box.destroy)
    b1.pack()


root = ct.CTk()
root.geometry("300x200")

# Botão para mostrar a caixa de diálogo personalizada
button = ct.CTkButton(root, text="Mostrar Aviso", command=lambda:messagebox(title='Aviso!'))
button.pack(pady=20)

root.mainloop()