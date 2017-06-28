#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from Tkinter import *
import tkFileDialog
from CheckEncoding import *


class Application(Frame):
    def createWidgets(self):
        self.fr_top = Frame(self)
        self.fr_bottom = Frame(self)

        self.FilePath = StringVar()
        self.EncodingInfo = StringVar()
        self.Entry = Entry(self.fr_top, textvariable=self.FilePath, width=40)
        self.OpenFile = Button(self.fr_top, text="OpenFile", command=self.OpenFile)
        self.QUIT = Button(self.fr_top, text="QUIT", fg="red", command=self.quit)

        self.EncodingLabel = Label(self.fr_bottom, textvariable=self.EncodingInfo, width=60, justify=LEFT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.minsize(300, 100)
        master.geometry('500x200+550+150')
        self.createWidgets()
        self.SelfPack()

    def OpenFile(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("all files", "*.*"), ("txt files", "*.txt"),
                                                                ("excel file", "*.xlsx")))

        # print CheckEncoding(self.filename).GetEncoding()
        # self.FilePath.set(CheckEncoding(self.filename).GetEncoding())
        self.FilePath.set(self.filename)
        Info = CheckEncoding(self.filename).GetEncoding()
        self.EncodingInfo.set("文件编码：" + Info.get("encoding") + '\n' \
                              "识别概率：" + str(Info.get("confidence") * 100) + '%\n')

    def SelfPack(self):
        self.fr_top.pack({"side": "top"})
        self.Entry.pack({"side": "left"})
        self.OpenFile.pack({"side": "left"})
        self.QUIT.pack({"side": "left"})
        self.fr_bottom.pack({"side": "bottom"})
        self.EncodingLabel.pack({"side": "left"})
        self.pack()


root = Tk()
app = Application(master=root)
app.mainloop()
