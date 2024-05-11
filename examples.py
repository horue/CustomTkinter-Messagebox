from CustomTkinterMessagebox import *
import customtkinter as ct


def main():
    root = ct.CTk()
    root.geometry("300x600")
    root.title('Test Window')

    l1 = ct.CTkLabel(root, text='')
    l1.pack()

    b1 = ct.CTkButton(root, text="Normal Button", command=lambda:CTkMessagebox.messagebox())
    b1.pack(pady=10)

    b2 = ct.CTkButton(root, text="Variables Button", command=lambda:CTkMessagebox.messagebox(title='Warning!', text='Error. No link was given.'))
    b2.pack(pady=10)

    fs = 'f string'
    b3 = ct.CTkButton(root, text='F string text test', command=lambda:CTkMessagebox.messagebox(title='Variable Test', text=f'This is a {fs} test!'))
    b3.pack(pady=10)

    b4 = ct.CTkButton(root, text="No sound test", command=lambda:CTkMessagebox.messagebox(title='No sound example!', text='No sound here.', sound='off'))
    b4.pack(pady=10)


    root.mainloop()

main()