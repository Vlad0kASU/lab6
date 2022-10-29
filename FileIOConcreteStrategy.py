# -*-coding utf-8-*-
import pickle
import os

from IOStrategy import IOStrategy


class FileIOConcreteStrategy(IOStrategy):
    def read(self):
        with open('notes.dumps', 'rb') as file:
            try:
                return pickle.load(file)['data']
            except IOError:
                print('Файл не найден')

                return []

    def write(self, notes):
        with open('notes.dumps', 'wb') as file:
            try:
                pickle.dump({'data': notes}, file)
            except IOError:
                print('Файла не найден')
