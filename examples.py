from CustomTkinterMessagebox import *
import customtkinter as ct


def main():
    root = ct.CTk()
    root.geometry("300x200")
    root.title('Test Window')

    b1 = ct.CTkButton(root, text="Test Button", command=lambda:CTkMessagebox.messagebox(title='Warning!', text='Error. No link was given.'))
    b1.pack(pady=20)

    var = 'VARIABLE HERE'
    b2 = ct.CTkButton(root, text='Variable text test', command=lambda:CTkMessagebox.messagebox(title='Variable Test', text=f'This is a {var} test'))
    b2.pack()

    root.mainloop()

main()