import os
import sys
import json
import tkinter
from tkinter import ttk

with open('settings.json', 'r', encoding="utf-8") as f:
    configs = json.load(f)
    lang = configs['language']

with open('resources/language.json', 'r', encoding="utf-8") as f:
    language_pack = json.load(f)


def shutdown():
    os.system('shutdown /s /t 10')


def reboot():
    os.system('shutdown /r /t 10')


def endsession():
    os.system('shutdown /l /t 10')


def hibernation():
    os.system('shutdown /h /t 10')


def exit_ps():
    os.system('shutdown /a')
    sys.exit()


root = tkinter.Tk()
root.title(language_pack[lang]['pc_power_management'])
root.iconbitmap(default=configs['iconbitmap'])
root.geometry(configs['geometry'])
root.attributes("-alpha", 0.9)
root.resizable(configs['resizable_x'], configs['resizable_y'])

label = tkinter.Label(text=language_pack[lang]['pc_power_management'], font=("Arial", 16))
label.pack(expand=True, anchor=tkinter.N)

btns = ttk.Button(text=language_pack[lang]['shutdown'], command=shutdown)
btnr = ttk.Button(text=language_pack[lang]['reboot'], command=reboot)
btnl = ttk.Button(text=language_pack[lang]['end_session'], command=endsession)
btnh = ttk.Button(text=language_pack[lang]['hibernation'], command=hibernation)
btn_exit = ttk.Button(text=language_pack[lang]['exit'], command=exit_ps)

btns.pack(anchor=tkinter.CENTER)
btnr.pack(anchor=tkinter.CENTER)
btnl.pack(anchor=tkinter.CENTER)
btnh.pack(anchor=tkinter.CENTER)
btn_exit.pack(expand=True, anchor=tkinter.S, fill=tkinter.BOTH, padx=2, pady=2)

root.mainloop()
