from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
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


def cadastrar_pedido(): 
    janela_cadastro = Toplevel()
    janela_cadastro.title('Cadastro de pedido')
    janela_cadastro.geometry('900x600')
    janela_cadastro.configure(background=co9)
    janela_cadastro.resizable(width=FALSE, height=FALSE)

    style = ttk.Style(janela_cadastro)
    style.theme_use("clam")