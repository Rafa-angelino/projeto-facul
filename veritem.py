from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
from PIL import Image, ImageTk

co0 = "#2e2d2b" #preto
co1= "#feffff" #branco
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

def ver_item():
    janela_ver_item = Toplevel()
    janela_ver_item.title('Itens')
    janela_ver_item.geometry('900x600')
    janela_ver_item.configure(background=co9)
    janela_ver_item.resizable(width=FALSE, height=FALSE)

    style = ttk.Style(janela_ver_item)
    style.theme_use("clam")
    mostrar_item(janela_ver_item)



def mostrar_item(janela):
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Codpedido','Nome', 'Barra','Descrição', 'Valor']

    lista_itens = []



    tree = ttk.Treeview(janela, selectmode="extended",columns=tabela_head, show="headings", height=20)
   

    # vertical scrollbar
    vsb = ttk.Scrollbar(janela, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(janela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    janela.grid_rowconfigure(0, weight=300, pad=50)

    position=["center","center","center","center","center"]
    head_width=[100,260,260,100,160]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=head_width[n],anchor=position[n])
  
        n+=1    