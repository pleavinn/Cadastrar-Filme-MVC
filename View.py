import sys
import tkinter as tk
from tkinter import ttk
from Controller import *


def donothing():
    pass


class View():
    def __init__(self,controller):
        self.controller =  controller

        self.root = tk.Tk()
        self.radioValue = tk.IntVar()

        self.filme()
        self.status()
        self.genero()
        self.buttons()
        self.id()

        self.root.bind('<Escape>', self.close)

        self.root.mainloop() # ✿ comando necessário para manter a janela aberta ✿ #

    

    #Cria a função filme e adiciona um container para colocar label e entry "Filme" "Diretor" e "Review"#
    def filme(self):
        container = tk.Frame(self.root)
        container.pack()

        # ✿ "label" posiciona um texto na tela ✿ 
        labelFilme = tk.Label(container, width=20, text='Filme')
        # ✿ "grid" e o comando utilizado para posicionar, levando em conta colunas e linhas
        labelFilme.grid(column=0, row=0, padx=5, pady=5)

        # ✿ "entry" e o comando utilizado para inserir uma caixa de entrada de texto
        self.entryFilme = tk.Entry(container, width=20)
        # ✿ posicionando nossa caixa de texto
        self.entryFilme.grid(column=0, row=1, padx=5, pady=5)
        

        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿
        ###### R E P E T I N D O ###### colocando e posicionando textos e entrada de texto#
        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿
        labelDiretor = tk.Label(container, width=20, text='Diretor')
        labelDiretor.grid(column=0, row=2, padx=5, pady=5)
        self.entryDiretor = tk.Entry(container, width=20)
        self.entryDiretor.grid(column=0, row=3, padx=5, pady=5)

        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿

        labelReview = tk.Label(container, width=20, text='Review')
        labelReview.grid(column=0, row=4, padx=5, pady=5)
        self.entryReview = tk.Entry(container, width=20)
        self.entryReview.grid(column=0, row=5, padx=5, pady=5)

    def status(self):
        container = tk.Frame(self.root)
        container.pack()

        labelStatus = tk.Label(container, width=20, text='Status:')
        labelStatus.grid(column=0, row=1, padx=5, pady=5)

        # cria uma variável para receber o valor do radiobutton ✿
        self.radioValue = tk.StringVar()

        # cria um radiobutton chamado assistido

        self.radioUm = tk.Radiobutton(container, text='Assistido', width=20,
                                      variable=self.radioValue, value=1,
                                      anchor=tk.W)
        # insere e posiciona o botao Assistido
        self.radioUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioDois = tk.Radiobutton(container, text='Watchlist', width=20,
                                        variable=self.radioValue,
                                        value=2,
                                        anchor=tk.W)
        self.radioDois.grid(column=1, row=1, padx=5, pady=5)

        self.radioTres = tk.Radiobutton(container, text='Favoritos', width=20,
                                        variable=self.radioValue,
                                        value=3,
                                        anchor=tk.W)
        self.radioTres.grid(column=1, row=2, padx=5, pady=5)

    def genero(self):
        container = tk.Frame(self.root)
        container.pack()

        labelGenero = tk.Label(container, width=20, text='Gênero')
        labelGenero.grid(column=0, row=0, padx=5, pady=5)

        # cria um combobox com as opções de generos de filme ✿
    
        self.comboGenero = ttk.Combobox(container, width=20,
                                            values=['Ação',
                                                    'Aventura',
                                                    'Cinema de Arte',
                                                    'Comédia'
                                                    'Dança',
                                                    'Documentário',
                                                    'Drama',
                                                    'Espionagem',
                                                    'Faroeste',
                                                    'Fantasia',
                                                    'Ficção Científica',
                                                    'Filmes de Guerra',
                                                    'Mistério',
                                                    'Musical',
                                                    'Romance',
                                                    'Terror',])
        self.comboGenero.grid(column=1, row=0, padx=5, pady=5)


        # cria o texto nota ✿

        labelGenero = tk.Label(container, width=20, text='Nota')
        labelGenero.grid(column=0, row=1, padx=5, pady=5)

        # cria uma variável para receber a nota
        self.nota = tk.DoubleVar()

        # cria a barrinha para inserir valor
        escalaNota = tk.Scale(container, from_=0, to=100, width=20,
                                 length=200, variable=self.nota,
                                 orient=tk.HORIZONTAL)
        escalaNota.grid(column=1, row=1, padx=5, pady=5)

    def id(self):
        container = tk.Frame(self.root)
        container.pack()

        labelId = tk.Label(container, width=20, text='ID')
        labelId.grid(column=0, row=0, padx=1, pady=1)

        self.entryID = tk.Entry(container, width=20)
        self.entryID.grid(column=0, row=5, padx=1, pady=1)


    def buttons(self):
        container = tk.Frame(self.root)
        container.pack()

        # cria o botão Adicionar ✿
        btnAdicionar = tk.Button(container, text='Adicionar', width=20,
                                command=self.adicionar)
        btnAdicionar.grid(column=0, row=0, padx=5, pady=5)

        # cria o botão Atualizar ✿
        btnAtualizar = tk.Button(container, text='Atualizar', width=20,
                                command=self.atualizar)
        btnAtualizar.grid(column=1, row=0, padx=5, pady=5)

        # cria o botão Remover ✿
        btnRemover = tk.Button(container, text='Remover', width=20, 
                               command=self.deletar)
        btnRemover.grid(column=2, row=0, padx=5, pady=5)

    def adicionar(self):
        if self.controller:

            if self.radioValue.get() ==  1:
                status = "Assistido"

            elif self.radioValue.get() ==  2:
                status = "Watchlist"
            
            elif self.radioValue.get() ==  3:
                status = "Favoritos"
            
            else:
                status = ""

            titulo = self.entryFilme.get()
            diretor = self.entryDiretor.get()
            review = self.entryReview.get()
            genero = self.comboGenero.get()
            nota = self.nota.get()
            id = self.entryID.get()

        self.controller.adicionar(titulo, diretor, review,status,genero,nota,id)

    def deletar(self):
        id = self.entryID.get()
        self.controller.deletar(id)

    def atualizar(self):
  
        id = self.entryID.get()
        titulo = self.entryFilme.get()
        diretor = self.entryDiretor.get()
        review = self.entryReview.get()
        genero = self.comboGenero.get()
        nota = self.nota.get()    
        self.controller.atualizar(id, titulo, diretor, review, genero, nota)






    def close(self, event=None):
        self.root.destroy()

