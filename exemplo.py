import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.item_label = tk.Label(self, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(self)
        self.item_entry.pack()

        self.quantity_label = tk.Label(self, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_order)
        self.submit_button.pack()

    def submit_order(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()

        # Aqui você pode implementar a lógica de processamento do pedido
        # e exibir uma mensagem na interface gráfica informando se o pedido foi bem-sucedido ou não.

        print(f"Pedido recebido: {item} x{quantity}")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
