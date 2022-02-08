from tkinter import *
import conexao_bd as bd #este seria o relat1
import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
import relat2 as relat2
import relat3 as relat3

class Application:

    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        #MENU do TOPO
        def donothing():
            filewin = Toplevel(root)
            button = Button(filewin, text="Do nothing button")
            button.pack()
        def sobre():
            filewin = Toplevel(root)
            filewin.geometry('200x50')
            lb_sobre = Label(filewin, text="marcelocaon@gmail.com")
            lb_sobre.pack()

        # def nome_usuario():
        #     #para alterar o nome do usuario principal = codigo usuario == 1
        #     novo_usuario = []
        #     tk_novo_usuario = Tk()
        #     tk_novo_usuario.title('Alteração nome do usuário:')
        #     tk_novo_usuario.geometry('300x100+200+220')
        #     label_nome_usuario = Label(tk_novo_usuario, text='Novo nome: ')
        #     label_nome_usuario.grid(row=0, column=0, sticky=E)
        #     entry_nome_usuario = Entry(tk_novo_usuario, bd=5, width=20)
        #     entry_nome_usuario.grid(row=0, column=1)
        #     bt_novo_usuario = Button(tk_novo_usuario, text='Alterar')
        #     bt_novo_usuario.grid(row=2, column=1, sticky=W + E)
        #
        #     def pega_nome_ativo(event):
        #         novo_usuario.append(entry_nome_usuario.get().capitalize())
        #         if bd.nome_usuario(novo_usuario) == True:
        #             messagebox.showinfo('Informação', 'Nome do usuário alterado com sucesso.')
        #             tk_novo_usuario.quit()
        #
        #     bt_novo_usuario.bind("<Button-1>", pega_nome_ativo)
        #     tk_novo_usuario.mainloop()

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        # filemenu.add_command(label="New", command=donothing)
        # filemenu.add_command(label="Open", command=donothing)
        # filemenu.add_command(label="Save", command=donothing)
        # filemenu.add_command(label="Save as...", command=donothing)
        # filemenu.add_command(label="Alterar Usuário", command=nome_usuario)
        # filemenu.add_command(label='Cadastrar ATIVO', command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=root.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        # editmenu = Menu(menubar, tearoff=0)
        # editmenu.add_command(label="Undo", command=donothing)
        # editmenu.add_separator()
        # editmenu.add_command(label="Cut", command=donothing)
        # editmenu.add_command(label="Copy", command=donothing)
        # editmenu.add_command(label="Paste", command=donothing)
        # editmenu.add_command(label="Delete", command=donothing)
        # editmenu.add_command(label="Select All", command=donothing)
        # menubar.add_cascade(label="Edit", menu=editmenu)

        # listagem_menu = Menu(menubar, tearoff=0)
        # listagem_menu.add_command(label="Listar Ações", command=donothing)
        # listagem_menu.add_separator()
        # listagem_menu.add_command(label="Posição da Carteira", command=donothing)
        # menubar.add_cascade(label="Carteira", menu=listagem_menu)

        helpmenu = Menu(menubar, tearoff=0)
        #helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="Sobre...", command=sobre)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)

        root.config(menu=menubar)
        #MENU = FIM

# TELA PRINCIPAL
        path = 'LOGOSD.bmp'
        img = Image.open(path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel = Label(self.widget1, image=img)
        self.panel.image = img
        self.panel.pack()


        self.msg = Label(self.widget1, text="MENU")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack()

        self.btn1 = Button(self.widget1)
        self.btn1["text"] = "1 - Ficha de cobrança:"
        self.btn1["font"] = ("Calibri", "12", "bold")
        self.btn1["width"] = 50
        self.btn1["bg"] = 'Blue'
        self.btn1["fg"] = 'White'
        self.btn1.bind("<Button-1>", self.relatorio1)
        self.btn1.pack()

        self.btn2 = Button(self.widget1)
        self.btn2["text"] = "2 - Cliente em aberto por rota:"
        self.btn2["font"] = ("Calibri", "12", "bold")
        self.btn2["width"] = 50
        self.btn2["bg"] = 'White'
        self.btn2["fg"] = 'Blue'
        #self.btn2.bind("<Button-1>", self.relatorio2)
        self.btn2.bind("<ButtonRelease-1>", self.relatorio2)
        self.btn2.pack()
        #self.btn2.pack(pady=(0,10))#para gerar um espaco entre o campo de texto

        self.btn3 = Button(self.widget1)
        self.btn3["text"] = "3 - Contas a receber por vendedor:"
        self.btn3["font"] = ("Calibri", "12", "bold")
        self.btn3["width"] = 50
        self.btn3["bg"] = 'Blue'
        self.btn3["fg"] = 'White'
        #self.btn2.bind("<Button-1>", self.relatorio2)
        self.btn3.bind("<ButtonRelease-1>", self.relatorio3)
        #self.btn2.pack()
        self.btn3.pack(pady=(0,10))#para gerar um espaco entre o campo de texto



        #STATUS BAR
        status = Label(self.widget1, text='Versão: 14/10/2019 @celocaon', bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        #STATUS BAR = FIM

# FUNCOES
    def fechar_programa(self, event):
        root.quit()

    def tela_data(self):
        pass





    def relatorio3(self, event):
        #RELATORIO 3
        #gera clientes em aberto por vendedor (total)
        self.e_data = Tk()
        self.e_data.geometry('400x75+250+350')  # Width x Height + posicao da janela
        self.e_data.resizable(0, 0)
        self.e_data.title("Informe as datas para pesquisa:")

        #ini, fim = StringVar()
        self.label_data_in = Label(self.e_data, text="Data Inicial:")
        self.label_data_in.grid(row=1, column=0, sticky=E)
        self.entry_data_in = Entry(self.e_data, bd=5)
        self.entry_data_in.grid(row=1, column=1)
        #self.entry_data_in.bind("<KeyRelease>", mostra_nome)
        self.entry_data_in.focus_force()
        self.label_data_fi = Label(self.e_data, text="Data Final:")
        self.label_data_fi.grid(row=2, column=0, sticky=E)
        self.entry_data_fi = Entry(self.e_data, bd=5)
        self.entry_data_fi.grid(row=2, column=1)
        #self.entry_data_fi.bind("<KeyRelease>", mostra_nome)

        def relatorio3_chama(event):
            data_in = self.entry_data_in.get()
            data_fi = self.entry_data_fi.get()
            if relat3.gerar_relat3(data_in, data_fi):
                messagebox.showinfo('Informação', 'Relatório 3 gerado com sucesso', icon='info')
                self.e_data.destroy()

        self.btn_data = Button(self.e_data)
        self.btn_data["text"] = "Consultar"
        self.btn_data["font"] = ("Calibri", "8")
        self.btn_data["width"] = 10
        self.btn_data["bg"] = 'Green'
        self.btn_data["fg"] = 'White'
        #self.btn_data["state"] = DISABLED
        self.btn_data.bind("<ButtonRelease-1>", relatorio3_chama)
        self.btn_data.grid(row=3, column=1)



    def relatorio2(self, event):
        #RELATORIO 2
        #gera clientes em aberto por dia de visita
        if relat2.gerar_relat2():
            messagebox.showinfo('Informação', 'Relatório 2 gerado com sucesso', icon='info')

    def relatorio1(self, event):
        #RELATORIO 1
        #imprime um formulario com as cobrancas do cliente informado
        self.e_cliente = Tk()
        self.e_cliente.geometry('400x75+250+350') #Width x Height + posicao da janela
        self.e_cliente.resizable(0,0)
        self.e_cliente.title("Digite o código do cliente:")

        # Label(self.e_cliente,
        #          text="""Código:""",
        #          justify=LEFT,
        #          padx=20, font=(None,10,'bold')).grid(row=0, column=1)
        def mostra_nome(event):
            codigo=[]
            codigo.append(self.entry_cliente.get())
            cliente = []
            cliente = bd.procura_cliente(codigo)
            if cliente.__len__() > 0:
                self.label_nome = Label(self.e_cliente, text=cliente[0][0][0:], font=(None,12,'bold'))
                self.label_nome.grid(row=2, column=1,columnspan=2)
                self.btn_cliente["state"] = NORMAL
            else:
                self.label_nome = Label(self.e_cliente, text='Código de cliente não encontrado...', font=(None,12,'bold'))
                self.label_nome.grid(row=2, column=1,columnspan=2)

        v = StringVar()
        self.label_cliente = Label(self.e_cliente, text="Código:")
        self.label_cliente.grid(row=1, column=0, sticky=E)
        self.entry_cliente = Entry(self.e_cliente, bd=5, textvariable=v)
        self.entry_cliente.grid(row=1, column=1)
        self.entry_cliente.bind("<KeyRelease>", mostra_nome)
        self.entry_cliente.focus_force()

        self.btn_cliente = Button(self.e_cliente)
        self.btn_cliente["text"] = "Consultar"
        self.btn_cliente["font"] = ("Calibri", "8")
        self.btn_cliente["width"] = 10
        self.btn_cliente["bg"] = 'Green'
        self.btn_cliente["fg"] = 'White'
        self.btn_cliente["state"] = DISABLED
        self.btn_cliente.bind("<Button-1>", self.ficha_cobranca)
        self.btn_cliente.grid(row=1, column=2)

    def ficha_cobranca(self, event):
        if self.btn_cliente["state"] == DISABLED:
            pass
        else:
            codcli = self.entry_cliente.get()
            bd.relatorio1(codcli)
            self.e_cliente.destroy()



#MAIN
#Inicia o programa com interface
root = Tk()
root.title('SD Distribuidora')
root.geometry('480x580+200+200') #Width x Height / +300 + 300 posicionar a janela
#nao permite que o usuario mude o tamanho da janela principal
root.resizable(0,0)
Application(root)
root.mainloop()