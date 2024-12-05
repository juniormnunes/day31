from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

class UserInterface(Tk):
    def __init__(self):
        super().__init__()
        self.title('Flash Cards')
        #self.geometry('900x700')
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.frame = Frame(self)
        self.image_wrong = PhotoImage(file=r'/Users/juniormnunes/Documents/PythonProgramming/100 Days of Code/Day31/flash-card-project-start/images/wrong.png')
        self.button_wrong = Button(image=self.image_wrong, highlightthickness=0, background=BACKGROUND_COLOR)
        self.button_wrong.grid(row=1, column=0)
        self.image_right = PhotoImage(file=r'/Users/juniormnunes/Documents/PythonProgramming/100 Days of Code/Day31/flash-card-project-start/images/right.png')
        self.button_right = Button(image=self.image_right, highlightthickness=0, background=BACKGROUND_COLOR)
        self.button_right.grid(row=1, column=1)

        self.card_front = PhotoImage(file=r'/Users/juniormnunes/Documents/PythonProgramming/100 Days of Code/Day31/flash-card-project-start/images/card_front.png')
        self.card_back = PhotoImage(file=r'/Users/juniormnunes/Documents/PythonProgramming/100 Days of Code/Day31/flash-card-project-start/images/card_back.png')
        self.flash_canvas = Canvas( width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
        self.flash_canvas.create_image(400, 263, image=self.card_front)
        self.flash_canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
        self.flash_canvas.create_text(400, 263, text='title', font=('Arial', 60, 'bold'))
        self.flash_canvas.grid(row=0, column=0, columnspan=2)




if __name__ == '__main__':
    app = UserInterface()
    app.mainloop()
