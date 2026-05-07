from src.model.DAO.base_db import BaseDB

class Fornecedor_DAO:

    def __init__(self):
        self.__conn = BaseDB("fornecedores.json")

    def add_fornecedor(self,data:dict):
        try:
            self.__conn.save(data)
            return "Fornecedor adicionado com sucesso!"
        except Exception as e:
            raise ValueError("Erro no momento de adicionar um fornecedor no banco de dados",e)

    def ler_fornecedores(self):
        return self.__conn.read_list()

    def deletar_fornecedor(self,id_fornecedor):
        nova_lista=[fornecedor for fornecedor in self.ler_fornecedores() if fornecedor["id"] != id_fornecedor]
        if len(nova_lista)==len(self.ler_fornecedores()):
            raise ValueError("Nenhum funcionario encontrado com esse ID")

        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

    def buscar_id_fornecedor(self,id):
        try:
            produto_encontrado=[produto for produto in self.ler_fornecedores() if produto["id"] == id][0]
            return produto_encontrado
        except IndexError as e:
            raise ValueError("Produto não existe no Sistema",e)