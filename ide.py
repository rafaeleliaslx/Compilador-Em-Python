# -*- coding: utf-8 -*-
from tkinter import*
# from tkFileDialog import askopenfilename, askdirectory
import os
import shutil


class AppScript(Frame):
    def __init__(self, width = 500, height=500):
        Frame.__init__(self, raiz)
        
        self.frame1 = Frame(self)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self)
        self.frame2.pack()
        self.frame3 = Frame(self)
        self.frame3.pack(side=BOTTOM)

        self.fonte1 = ('Verdana', '13', 'bold')
        self.fonte3 = ('Verdana', '9', 'bold')
        self.fonte2 = ('Verdana', '8')

        self.texto = Text(self.frame1, font = self.fonte2, background="white")
        # self.texto.insert(1.0, self.lista())
        self.texto.pack(pady=10)
        # self.texto.configure(state=DISABLED)
        
        self.sb = Scrollbar()
        self.sb.pack(side=RIGHT,fill="y")
        self.sb.configure(command=self.texto.yview())
        self.texto.configure(yscrollcommand=self.sb.set)


raiz = Tk()
aplicativo = AppScript(raiz)
aplicativo.master.title("Script for Organization   @PhilippeOz")
aplicativo.pack()
raiz.mainloop()