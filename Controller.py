import Model
import View

class Controller():
    def __init__(self, model):
        self.model = model
       
    def adicionar(self, titulo, diretor, review ,status, genero, nota,id):

        self.model.titulo = titulo
        self.model.diretor = diretor
        self.model.review =  review
        self.model.status = status
        self.model.genero = genero
        self.model.nota = nota
        self.model.id = id

        self.model.salvar()

       
    def deletar(self, id):
        self.model.id = id
        self.model.deletar(self.model.id)

    def atualizar(self, id, titulo, diretor, review , genero, nota):
        self.model.id = id
        self.model.titulo = titulo
        self.model.diretor = diretor
        self.model.review =  review
        self.model.genero = genero
        self.model.nota = nota


        self.model.atualizar(id, titulo, diretor, review, genero, nota)