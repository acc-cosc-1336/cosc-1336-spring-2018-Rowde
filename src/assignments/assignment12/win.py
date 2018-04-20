from tkinter import Tk, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Assignment 12')

        kilometer = 100

        self.converter = Converter()
        
        self.label = Label(self, text='Km: ' + str(kilometer)).grid(row=0)
        self.label = Label(self, text='Miles: ' + format(self.converter.get_miles_from_km(100), '.2f')).grid(row=1)

        self.mainloop()
