
from pymongo.mongo_client import MongoClient
from pymongo import *

class Model():
    def __init__(self):
        self.client = MongoClient("mongodb+srv://isabelly:isa12366@cavv.m9wzdzw.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["Cavv_db"]
        self.collection = self.db["cadastro"]   

        self.id = ""
        self.titulo = ""
        self.diretor = ""
        self.review = ""
        self.status = ""
        self.genero = ""
        self.nota = ""
        

    def salvar(self):
        user_data = {
            '_id' : self.id,
            'titulo': self.titulo,
            'diretor': self.diretor,
            'review': self.review,
            'status': self.status,
            'genero': self.genero,
            'nota': self.nota

        }

        result_save = self.collection.insert_one(user_data) 


        if result_save.inserted_id:
            print("Cadastro feito com sucesso!")
        
        else:
            print("Cadastro não realizado.")
            
    
    def deletar(self, item_id):

        result = self.collection.delete_one({"_id": item_id})
        if result.deleted_count > 0:
            print("Item deletado com sucesso!")
        else:
            print("Nenhum item foi deletado.")
            

    def atualizar(self, item_id, titulo, diretor, review, genero, nota):
        result = self.collection.update_one(
            {"_id": item_id},
            {
                "$set": {
                    "titulo": titulo,
                    "diretor": diretor,
                    "review": review,
                    "genero": genero,
                    "nota": nota
                }
            }
        )

        if result.modified_count > 0:
            print("Item atualizado com sucesso!")
        else:
            print("Nenhum item foi atualizado.")





