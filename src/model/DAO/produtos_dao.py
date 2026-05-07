from src.model.DAO.base_db import BaseDB

class Produtos_DAO:

    def __init__(self):
        self.__conn=BaseDB("produto.json")

    def add_produtos(self,data:dict):
        try:
            self.__conn.save(data)
            return "Produto adicionado com sucesso!"
        except Exception as e:
            raise ValueError("Erro no momento de adicionar um produto no banco de dados",e)

    def ler_produtos(self):
        return self.__conn.read_list()

    def deletar_produto(self,id_produto):
        nova_lista=[produto for produto in self.ler_produtos() if produto["id"] != id_produto]
        if len(nova_lista)==len(self.ler_produtos()):
            raise ValueError("Nenhum produto encontrado com esse ID")
        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

    def buscar_por_ID(self,id):
        try:
            produto_encontrado=[produto for produto in self.ler_produtos() if produto["id"] == id][0]
            return produto_encontrado
        except IndexError as e:
            raise ValueError("Produto não existe no Sistema",e)





if __name__ == '__main__':
    p1=Produtos_DAO()

    try:
        print(p1.buscar_por_ID(6))
    except Exception as e:
        print(e)