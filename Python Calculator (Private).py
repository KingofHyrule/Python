from tkinter import *
import math

hesapmakinesi = Tk()
hesapmakinesi.title("Hesap Makinesi")
hesapmakinesi.configure(background="gray")

sayi_gir_1 = Entry(hesapmakinesi, width=40, bg="white")
sayi_gir_1.grid(row=2, column=0, sticky=W)

sayi_gir_2 = Entry(hesapmakinesi, width=40, bg="white")
sayi_gir_2.grid(row=4, column=0, sticky=W)

def kapat():
    hesapmakinesi.destroy()
    exit()

def tamam_1():
    girilen_sayi_1 = sayi_gir_1.get()

def tamam_2():
    girilen_sayi_2 = sayi_gir_2.get()

def topla():
    sonuc = girilen_sayi_1 + girilen_sayi_2
    Label(hesapmakinesi, text=sonuc, bg="gray", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

#Button(hesapmakinesi, text="÷", width=6, command=(a/b)) .grid(row=12, column=6, sticky=W)
Button(hesapmakinesi, text="+", width=6, command=topla) .grid(row=3, column=6, sticky=W)
#Button(hesapmakinesi, text="x", width=6, command=(a*b)) .grid(row=9, column=6, sticky=W)
#Button(hesapmakinesi, text="-", width=6, command=(a-b)) .grid(row=6, column=6, sticky=W)
Button(hesapmakinesi, text="Çıkış", width=6, command=kapat) .grid(row=2, column=6, sticky=W)
Button(hesapmakinesi, text="Tamam (1. Sayı İçin (Üstteki))", width=6, command=tamam_1) .grid(row=14, column=6, sticky=W)
Button(hesapmakinesi, text="Tamam (2. Sayı İçin (Alttaki))", width=6, command=tamam_2) .grid(row=16, column=6, sticky=W)

hesapmakinesi.mainloop()