from tkinter import Frame, Text, Label, Canvas, Pack, Grid, Place
from tkinter.constants import RIGHT, LEFT, Y, BOTH
import sys

class TextWidget(Label):
    def __init__(self, master=None,  **kw):
        self.frame = Frame(master)

        if 'height' in kw:
            del kw['height']

        if len(kw['text']) < kw['width']:
            kw['width'] = len(kw['text'])

        kw['text'] = self.prepare_text(kw['text'], kw['width'])    
        Label.__init__(self, self.frame, **kw)

        self.pack(side=LEFT, fill=BOTH, expand=True)

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Label).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))


    def prepare_text(self, text, width):
        n = int(len(text)/width)
        if n > 1:
            for i in range(1, int(n+1)):
                pos = width*i
                for j in range(width*(i-1), width*i):
                    if text[j] == ' ':
                        pos = j
                text = text[:pos]+'\n'+text[pos:]
        return text
            


def example():

    big_text = TextWidget(width=20, relief='solid', pady=50, text='Now you can write a really big text without loss beyound the form')
    big_text.pack(fill=BOTH, side=LEFT, expand=True)
    big_text.focus_set()
    big_text.bind('<Escape>', exit)
    big_text.mainloop()

if __name__ == "__main__":
    example()
