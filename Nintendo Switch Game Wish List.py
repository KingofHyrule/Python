# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
import webbrowser

istek_listesi = Tk()
istek_listesi.title("Nintendo Switch Game Wish List")
istek_listesi.configure(background="white")

tkinter.messagebox.showwarning("Dikkat!", "Lütfen uygulamayı tam ekranda kullanınız...")

def kapat():
    answer = tkinter.messagebox.askyesno("Emin Misin?", "Çıkmak istediğine emin misin?")
    if answer == YES:
        tkinter.messagebox.showerror("Hata!", "Uygulama kapatılamıyor!")
    else:
        pass
    

def first_game():
    tkinter.messagebox.showinfo("1. İstek", "Super Mario Odyssey")
    answer_first_game = tkinter.messagebox.askyesno("Oyun Hakkında...", "İlgili Siteleri Açmak İster Misiniz?")
    if answer_first_game == YES:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=wGQHQc_3ycE")
        webbrowser.open_new(r"https://www.nintendo.com/games/detail/super-mario-odyssey-switch")
    else:
        answer_first_game_2 = tkinter.messagebox.askyesno("Oyun Hakkında...", "Emin Misin?")
        if answer_first_game_2 == NO:
            webbrowser.open_new(r"https://www.youtube.com/watch?v=wGQHQc_3ycE")
            webbrowser.open_new(r"https://www.nintendo.com/games/detail/super-mario-odyssey-switch")
        else:
            pass

def second_game():
    tkinter.messagebox.showinfo("2. İstek", "Mario Tennis Aces")
    answer_second_game = tkinter.messagebox.askyesno("Oyun Hakkında...", "İlgili Siteleri Açmak İster Misiniz?")
    if answer_second_game == YES:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=jxrHwK-e1vk")
        webbrowser.open_new(r"https://www.nintendo.com/games/detail/mario-tennis-aces-switch")
    else:
        answer_second_game_2 = tkinter.messagebox.askyesno("Oyun Hakkında...", "Emin Misin?")
        if answer_second_game_2 == NO:
            webbrowser.open_new(r"https://www.youtube.com/watch?v=jxrHwK-e1vk")
            webbrowser.open_new(r"https://www.nintendo.com/games/detail/mario-tennis-aces-switch")
        else:
            pass


def third_game():
    tkinter.messagebox.showinfo("3. İstek", "Splatoon 2")
    answer_third_game = tkinter.messagebox.askyesno("Oyun Hakkında?", "İlgili Siteleri Açmak İster Misiniz?")
    if answer_third_game == YES:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=ylBYfndq8fU")
        webbrowser.open_new(r"https://www.nintendo.com/games/detail/splatoon-2-switch")
    else:
        answer_third_game_2 = tkinter.messagebox.askyesno("Oyun Hakkında...", "Emin Misin?")
        if answer_third_game_2 == NO:
            webbrowser.open_new(r"https://www.youtube.com/watch?v=ylBYfndq8fU")
            webbrowser.open_new(r"https://www.nintendo.com/games/detail/splatoon-2-switch")
        else:
            pass

def fourth_game():
    tkinter.messagebox.showinfo("4. İstek", "Super Smash Bros. Ultimate")
    answer_fourth_game = tkinter.messagebox.askyesno("Oyun Hakkında?", "İlgili Siteleri Açmak İster Misiniz?")
    if answer_fourth_game == YES:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=w3Gt42kVgCw")
        webbrowser.open_new(r"https://www.nintendo.com/games/detail/super-smash-bros-switch")
    else:
        answer_fourth_game_2 = tkinter.messagebox.askyesno("Oyun Hakkında...", "Emin Misin?")
        if answer_fourth_game_2 == NO:
            webbrowser.open_new(r"https://www.youtube.com/watch?v=w3Gt42kVgCw")
            webbrowser.open_new(r"https://www.nintendo.com/games/detail/super-smash-bros-switch")
        else:
            pass

def fifth_game():
    tkinter.messagebox.showinfo("5. İstek", "Super Smash Bros. Ultimate")
    answer_fifth_game = tkinter.messagebox.askyesno("Oyun Hakkında?", "İlgili Siteleri Açmak İster Misiniz?")
    if answer_fifth_game == YES:
        webbrowser.open_new(r"https://www.youtube.com/watch?v=Y8zQxSWaotc")
        webbrowser.open_new(r"https://www.nintendo.com/games/detail/captain-toad-treasure-tracker-switch")
    else:
        answer_fifth_game_2 = tkinter.messagebox.askyesno("Oyun Hakkında...", "Emin Misin?")
        if answer_fifth_game_2 == NO:
            webbrowser.open_new(r"https://www.youtube.com/watch?v=Y8zQxSWaotc")
            webbrowser.open_new(r"https://www.nintendo.com/games/detail/captain-toad-treasure-tracker-switch")
        else:
            pass

Button(istek_listesi, text="Çıkış", width=15, command=kapat).grid(row=10, column=0, sticky=W)
Button(istek_listesi, text="1. İstek", width=15, command=first_game).grid(row=0, column=0, sticky=W)
Button(istek_listesi, text="2. İstek", width=15, command=second_game).grid(row=2, column=0, sticky=W)
Button(istek_listesi, text="3. İstek", width=15, command=third_game).grid(row=4, column=0, sticky=W)
Button(istek_listesi, text="4. İstek", width=15, command=fourth_game).grid(row=6, column=0, sticky=W)
Button(istek_listesi, text="5. İstek", width=15, command=fifth_game).grid(row=8, column=0, sticky=W)

istek_listesi.mainloop()