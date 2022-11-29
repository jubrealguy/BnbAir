#!usr/bin/python3
'''

'''
from uuid import uuid4
from datetime import datetime
class BAseModel:
    '''
    Creating public instanc attribute:
    '''

    def __init__(self):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        
        return '[{}] ({}) {}'.format([self.__class__.__name__, self.id, self.__dict__])
