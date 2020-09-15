'''
@author: Jörg Reisslein
'''

from view import View
from model import Model

class Controller:
    '''
    Classdoc
    '''
    def __init__(self):
        self.myView = View(self)
        self.myModel = Model()

    def main(self):
        self.myView.defaultView()


if __name__ == '__main__':
    myController = Controller()
    myController.main()




