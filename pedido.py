from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
from PIL import Image, ImageTk

from cadastropedido import*
from veritem import*

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

def abrir_Pedido():
    janela2 = tk.Toplevel()
    janela2.title('Cadastro de pedido')
    janela2.geometry('900x600')
    janela2.configure(background=co1)
    janela2.resizable(width=FALSE, height=FALSE)

    style = ttk.Style(janela2)
    style.theme_use("clam")
    
    #criando frames 
    frameTop = Frame(janela2, width=1043, height=50, bg=co1, relief= FLAT)
    frameTop.grid(row=0, column=0)

    frameMid = Frame(janela2, bg=co1,pady= 20, relief= FLAT)
    frameMid.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)
    

    #trabalhando no frametop 
    
    btn_Order = Button(frameTop,width=29, text='Adicionar'.upper(),command=cadastrar_pedido, font=('Ivy 8'), bg=co1, fg=co0)
    btn_Order.grid(row=0, column=0,padx=15, pady=10)
    btn_ver_pedido = Button(frameTop,width=29, text='Ver itens'.upper(),command=ver_item, font=('Ivy 8'), bg=co1, fg=co0)
    btn_ver_pedido.grid(row=0, column=2, padx=15, pady=10)

    mostrar_tabela(frameMid)
    
    janela2.mainloop()
    
# tabela -----------------------------------------------------------
def mostrar_tabela(frame):
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#CodPedido','Cliente','Vendedor', 'Valor','Data de compra']

    lista_pedido = [[1, "rafael", "rafael", "12,90", "12/10/2023"]]



    tree = ttk.Treeview(frame, selectmode="extended",columns=tabela_head, show="headings", height=20)
   

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame.grid_rowconfigure(0, weight=300, pad=50)

    position=["center","center","center","center","center"]
    head_width=[100,260,260,100,160]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=head_width[n],anchor=position[n])
  
        n+=1    
    
    for item in lista_pedido:
        tree.insert('', 'end', values=item)    