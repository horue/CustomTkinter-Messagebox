
# CustomTkinterMessagebox

CustomTkinterMessagebox is a Python library that provides a customizable message box functionality for Tkinter-based applications. It allows developers to easily create message boxes with custom text, buttons, and optional sound effects.

## 1. Features

-   **Customizable Content:** Specify the title, message text, button text, and sound option for each message box.
-   **Resizable:** By default, the message boxes are resizable to accommodate different content lengths.
-   **Always on Top:** Message boxes are set to be always on top of other windows for better visibility.
-   **Sound Effects:** Optionally play a system sound effect when the message box is displayed.
-   **Easy Integration:** Integrates seamlessly with CustomTkinter, a custom-themed extension of the Tkinter GUI toolkit.

## 2.  Usage

To use CustomTkinterMessagebox in your Python application, follow these steps:

1.  **Installation:** Install the library using pip:
   
    `pip install CustomTkinterMessagebox` 
    
2.  **Import:** Import the `CTkMessagebox` class from the library in your Python script:
    
    `from CustomTkinterMessagebox import CTkMessagebox` 
    
3.  **Display Message Box:** Call the `messagebox` method with your desired parameters to display a message box:
 
    `CTkMessagebox.messagebox(title='CustomTKinterMessagebox', text='This is a sample message!', sound='on', button_text='OK')` 

## 3. Parameters for the `messagebox` Function
| Parameter    | Default Value           | Description                                             |
|--------------|-------------------------|---------------------------------------------------------|
| title        | 'CustomTKinterMessagebox!' | The title of the message box.                         |
| text         | 'Messagebox is working!'  | The message text displayed in the message box.        |
| sound        | 'on'                        | Sound option for playing system sound effect.         |
| button_text  | 'OK'                        | Text for the button displayed in the message box.     |
| size         | '320x150'                   | Size of the message box window.                       |
| center       | True                        | Whether to center the message box window on the screen.|
| top          | True                        | Whether the message box window should be on top.      |
## 4. Dependencies

CustomTkinterMessagebox depends on the following Python libraries:

-   **CustomTkinter:** A custom-themed extension of the Tkinter GUI toolkit.
-   **PIL (Python Imaging Library):** Used for image processing and displaying icons in the message box.
-   **winsound:** Required for playing system sound effects, especially on Windows platforms.

Make sure to have these dependencies installed in your Python environment before using CustomTkinterMessagebox.

## 5. Additional Notes

-   Customize the appearance and behavior of the message box by modifying the code within the `CTkMessagebox` class.
-   Feel free to contribute to the project by submitting bug reports, feature requests, or code contributions on the GitHub repository.

## 6. Support and Contributions

If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the GitHub repository. Contributions via pull requests are also welcome!

## 7. Examples

Check out the `examples.py` file for some usage examples of CustomTkinterMessagebox.

    from  CustomTkinterMessagebox  import  *
    import  customtkinter  as  ct
    
    def  main():
	    root  =  ct.CTk()
	    root.geometry("300x600")
	    root.title('Test Window')
	    
	    l1  =  ct.CTkLabel(root, text='')
	    l1.pack()
	    
	    b1  =  ct.CTkButton(root, text="Normal Button", command=lambda:CTkMessagebox.messagebox())
	    b1.pack(pady=10)
    

	    b2  =  ct.CTkButton(root, text="Variables Button", command=lambda:CTkMessagebox.messagebox(title='Warning!', text='Error. No link was given.'))
	    b2.pack(pady=10)

	    fs  =  'f string'    
	    b3  =  ct.CTkButton(root, text='F string text test', command=lambda:CTkMessagebox.messagebox(title='Variable Test', text=f'This is a {fs} test!'))
	    b3.pack(pady=10)

	    b4  =  ct.CTkButton(root, text="No sound test", command=lambda:CTkMessagebox.messagebox(title='No sound example!', text='No sound here.', sound='off'))
	    b4.pack(pady=10)
    
	    root.mainloop()
    
    main()

## 8. License

CustomTkinterMessagebox is licensed under the MIT License. You are free to use and modify this software for any purpose.

## 9. Inspired by CustomTkinter

CustomTkinterMessagebox was inspired by the CustomTkinter library, a custom-themed extension of the Tkinter GUI toolkit. While CustomTkinterMessagebox provides specific functionality for creating customizable message boxes, the underlying structure and theme integration were influenced by CustomTkinter.

CustomTkinter, created by [Tom Schimansky](https://github.com/TomSchimansky), offers a variety of customization options for Tkinter-based applications, including custom-themed widgets, color schemes, and layout enhancements. CustomTkinterMessagebox leverages this framework to provide an intuitive and visually appealing message box solution for developers.

We would like to express our gratitude to the creators and contributors of CustomTkinter for their innovative work and inspiration.