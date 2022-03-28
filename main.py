import pylab as plt
import tkinter as tk
import numpy as np
from tkinter import *
from numpy import *


def graph_txt():
    f = open("soubor-win.txt", 'r')
    x = []
    y = []
    while 1:
        line = f.readline()
        if line == '':
            break
        numbers = line.split()
        x.append(float(numbers[0]))
        y.append(float(numbers[1]))
        print(line, numbers)
    f.close()
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

def graph_make():
    frekvence = vstup1_var.get()
    zacatek = vstup2_var.get()
    konec = vstup3_var.get()
    amplituda = vstup4_var.get()
    x = plt.linspace(zacatek, 10 / frekvence, frekvence * 10000)
    y = amplituda * (plt.cos(2 * pi * frekvence * x))
    plt.plot(x, y)
    plt.title("Cosinus")
    plt.xlabel("t[s]")
    plt.ylabel("u[V]")
    plt.grid()
    plt.show()


okno=Tk()
okno.title("Vytvoření grafů")
vstup1_var = tk.IntVar()
vstup2_var = tk.IntVar()
vstup3_var = tk.IntVar()
vstup4_var = tk.IntVar()
nadpis=Label(okno, text=u"Vytvoření grafu pomocí textového souboru", font="Arial 18")
nadpis.pack(anchor=S)
b = Button(okno, text="Vytvoř", command=graph_txt)
b.pack(anchor=S)
nadpis2=Label(okno,text=u"vytvoření grafu pomocí zadaných hodnot", font="Arial 18")
nadpis2.pack(anchor=S)
stitek1 = Label(okno, text=u"frekvence")
stitek1.pack(anchor=S)
vstup1 = Entry(okno, textvariable = vstup1_var)
vstup1.pack()
vstup1.focus_set()
stitek2 = Label(okno, text=u"zacatek")
stitek2.pack(anchor=S)
vstup2 = Entry(okno, textvariable = vstup2_var)
vstup2.pack()
vstup2.focus_set()
stitek3 = Label(okno, text=u"konec")
stitek3.pack(anchor=S)
vstup3 = Entry(okno, textvariable = vstup3_var)
vstup3.pack()
vstup3.focus_set()
stitek4 = Label(okno, text=u"amplituda")
stitek4.pack(anchor=S)
vstup4 = Entry(okno,textvariable = vstup4_var)
vstup4.pack()
vstup4.focus_set()
b = Button(okno, text="Vytvoř", command=graph_make)
b.pack()

okno.mainloop()


