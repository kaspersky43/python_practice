# -*- coding: cp949 -*-

class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []
    
    def open(self):
        self.isOpened = True
        print('����� ���� �������...')
    
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('����� �ӿ� ������ ����...')
        else:
            print('����� ���� �����־ ���ְھ��...')
    
    def close(self):
        self.isOpened = False
        print('����� ���� �ݾҾ��...')

class Food:
    pass
