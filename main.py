from Model import Model
from View import View
from Controller import Controller

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    view = View(controller)
    
