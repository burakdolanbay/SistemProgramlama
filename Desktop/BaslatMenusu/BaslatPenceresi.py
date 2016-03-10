#!/usr/bin/env python
#-*- coding:utf-8-*-

from tkinter import *
import os
import Fonksiyonlar

pencere=Tk()
pencere.title("BAŞLAT MENÜSÜ")
pencere.wm_iconbitmap("hourglass")
pencere.geometry("400x300")
#pencere.state("iconic")

btn_kapat = Button(text="kapat",command=Fonksiyonlar.kapat)
btn_kapat.pack(side="right")
btn_kapat.pack(anchor="sw")

btn_reset = Button(text="reset",command=Fonksiyonlar.reset)
btn_reset.pack(side="right")
btn_reset.pack(anchor="sw")

btn_calis = Button(text="calis",command="")
btn_calis.pack(side="right")
btn_calis.pack(anchor="sw")

entry = Entry()
entry.pack(side="left")
entry.pack(anchor="sw")

btn_ara = Button(text="ARA",command="")
btn_ara.pack(side="left")
btn_ara.pack(anchor="sw")








mainloop()