from tkinter import *
import math
import time

hesapmakinesi = Tk()
hesapmakinesi.title("Hesap Makinesi")
hesapmakinesi.configure(background="gray")

sayi_gir_1 = Entry(hesapmakinesi, width=40, bg="white")
sayi_gir_1.grid(row=2, column=5, sticky=W)
Label(hesapmakinesi, text="1. Sayı:", bg="gray", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)

sayi_gir_2 = Entry(hesapmakinesi, width=40, bg="white")
sayi_gir_2.grid(row=3, column=5, sticky=W)
Label(hesapmakinesi, text="2. Sayı:", bg="gray", fg="white", font="none 12 bold") .grid(row=3, column=0, sticky=W)

def kapat():
    hesapmakinesi.destroy()
    exit()

def topla():
    girilen_sayi_1 = sayi_gir_1.get()
    girilen_sayi_2 = sayi_gir_2.get()
    sonuc = float(girilen_sayi_1) + float(girilen_sayi_2)
    Label(hesapmakinesi, text="Sonuç:", bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
    Label(hesapmakinesi, text=sonuc, bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=5, sticky=W)

def cıkart():
    girilen_sayi_1 = sayi_gir_1.get()
    girilen_sayi_2 = sayi_gir_2.get()
    sonuc = float(girilen_sayi_1) - float(girilen_sayi_2)
    Label(hesapmakinesi, text="Sonuç:", bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
    Label(hesapmakinesi, text=sonuc, bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=5, sticky=W)

def carp():
    girilen_sayi_1 = sayi_gir_1.get()
    girilen_sayi_2 = sayi_gir_2.get()
    sonuc = float(girilen_sayi_1) * float(girilen_sayi_2)
    Label(hesapmakinesi, text="Sonuç:", bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
    Label(hesapmakinesi, text=sonuc, bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=5, sticky=W)

def bol():
    girilen_sayi_1 = sayi_gir_1.get()
    girilen_sayi_2 = sayi_gir_2.get()
    sonuc = float(girilen_sayi_1) / float(girilen_sayi_2)
    Label(hesapmakinesi, text="Sonuç:", bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
    Label(hesapmakinesi, text=sonuc, bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=5, sticky=W)

Button(hesapmakinesi, text="÷", width=15, command=bol) .grid(row=12, column=11, sticky=W)
Button(hesapmakinesi, text="+", width=15, command=topla) .grid(row=3, column=11, sticky=W)
Button(hesapmakinesi, text="x", width=15, command=carp) .grid(row=9, column=11, sticky=W)
Button(hesapmakinesi, text="-", width=15, command=cıkart) .grid(row=6, column=11, sticky=W)
Button(hesapmakinesi, text="Çıkış", width=15, command=kapat) .grid(row=2, column=11, sticky=W)

hesapmakinesi.mainloop()