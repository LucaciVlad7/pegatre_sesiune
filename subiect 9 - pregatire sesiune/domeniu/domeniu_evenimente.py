class Eveniment():
    def __init__(self,data,ora,descriere):
        self.__data=data
        self.__ora=ora
        self.__descriere=descriere

    def get_data(self):
        return self.__data

    def get_ora(self):
        return self.__ora

    def get_descriere(self):
        return self.__descriere