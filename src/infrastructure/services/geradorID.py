import json
from json import JSONDecodeError


class GeradorID:

    def __init__(self,path_file,atributo):
        self.path_file=path_file
        self.id_gerado=None

        #verificando se abre o arquivo
        try:
            with open(self.path_file,"r",encoding="utf-8")as file:
                lista=json.load(file)
                lista_id=[data[atributo] for data in lista]
                # vai pegar o id maior e adicionar mais criando um id
                self.id_gerado=max(lista_id)+1
        except JSONDecodeError as e:
            self.id_gerado=1


if __name__ == '__main__':
    idNovo=GeradorID(r"C:\Users\kleber.asilva16\PycharmProjects\SistemaLimpeza\src\database\estoque.json","id").id_gerado
    print(idNovo)