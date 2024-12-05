from tkinter import *
import pandas as pd
import random as rd
import os

from pandas.errors import EmptyDataError
from pygments.lexer import words

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None

class UserInterface(Tk):
    def __init__(self):
        super().__init__()
        self.dict_word = self.read_csv()

        self.title('Flash Cards')
        #self.geometry('900x700')
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.frame = Frame(self)
        self.image_wrong = PhotoImage(file='flash-card-project-start/images/wrong.png')
        self.button_wrong = Button(image=self.image_wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=self.press_right)
        self.button_wrong.grid(row=1, column=0)
        self.image_right = PhotoImage(file='flash-card-project-start/images/right.png')
        self.button_right = Button(image=self.image_right, highlightthickness=0, background=BACKGROUND_COLOR, command=self.press_right)
        self.button_right.grid(row=1, column=1)

        self.card_front = PhotoImage(file='flash-card-project-start/images/card_front.png')
        self.card_back = PhotoImage(file='flash-card-project-start/images/card_back.png')
        self.flash_canvas = Canvas( width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
        self.card = self.flash_canvas.create_image(400, 263, image=self.card_front)
        self.title_card = self.flash_canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
        self.word_card = self.flash_canvas.create_text(400, 263, text=self.get_word()['French'], font=('Ariel', 60, 'bold'))
        self.flash_canvas.grid(row=0, column=0, columnspan=2)
        self.after(3000, self.flip_card)

    # def read_csv(self):
    #     df = pd.read_csv('flash-card-project-start/data/french_words.csv')
    #     dict_word = df.to_dict(orient='records')
    #     list_french = [v for d in dict_word for k, v in d.items() if k == 'French']
    #     list_english = [v for d in dict_word for k, v in d.items() if k == 'English']
    #     #english_dict = {'English': list_english}
    #     #french_dict = {'French': list_french}
    #     #return(french_dict, english_dict)
    #     return {french_word: english_word for french_word, english_word in zip(list_french, list_english)}
    def read_csv(self):
        try:
            if os.path.isfile('words_to_learn.csv'):
                df = pd.read_csv('words_to_learn.csv')
                if not df.empty:
                    dic_word = df.to_dict(orient='records')
                    return dic_word
        except EmptyDataError:
            pass
        except FileNotFoundError:
            pass
        df = pd.read_csv('flash-card-project-start/data/french_words.csv')
        dic_word = df.to_dict(orient='records')
        return dic_word

    def get_word(self):
        self.current_card = rd.choice(self.dict_word)
        return self.current_card

    def press_right(self):
        global flip_timer
        self.after_cancel(flip_timer)
        self.current_card = self.get_word()
        self.flash_canvas.itemconfig(self.card, image=self.card_front)
        self.flash_canvas.itemconfig(self.word_card, text=self.current_card['French'], fill='black')
        self.flash_canvas.itemconfig(self.title_card, text='French', fill='black')
        flip_timer = self.after(3000, self.flip_card)
        self.save_progress(self.current_card['French'], self.current_card['English'])

    def press_wrong(self):
        self.current_card = self.get_word()
        self.flash_canvas.itemconfig(self.card, image=self.card_front)
        self.flash_canvas.itemconfig(self.word_card, text=self.current_card['French'], fill='black')
        self.flash_canvas.itemconfig(self.title_card, text='French', fill='black')

    def flip_card(self):
        self.flash_canvas.itemconfig(self.card, image=self.card_back)
        self.flash_canvas.itemconfig(self.word_card, text=self.current_card['English'], fill='white')
        self.flash_canvas.itemconfig(self.title_card, text='English', fill='white')

    def save_progress(self, french_word, english_word):
        print(french_word, english_word)
        dict_to_remove = {'French': french_word, 'English': english_word}
        if dict_to_remove in self.dict_word:
            self.dict_word.remove(dict_to_remove)
        else:
            print('This word is not in the dictionary.')

        df = pd.DataFrame.from_dict(self.dict_word)
        df.to_csv('words_to_learn.csv', index=False)

if __name__ == '__main__':
    app = UserInterface()
    flip_timer = app.after(3000, app.flip_card)
    app.mainloop()
