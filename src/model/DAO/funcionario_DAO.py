from src.model.DAO.base_db import BaseDB


class Funcionario_DAO:

    def __init__(self):
        self.__conn = BaseDB("funcionarios.json")

    def add_funcionario(self,data:dict):
        try:
            self.__conn.save(data)
            return "Fornecedor adicionado com sucesso!"
        except Exception as e:
            raise ValueError("Erro no momento de adicionar um fornecedor no banco de dados",e)

    def ler_funcionario(self):
        return self.__conn.read_list()

    def deletar_funcionario(self, id_funcionario):
        nova_lista=[funcionario for funcionario in self.ler_funcionario() if funcionario["id"] != id_funcionario]
        if len(nova_lista)==len(self.ler_funcionario()):
            raise ValueError("Nenhum produto encontrado com esse ID")

        self.__conn.save_list(nova_lista)
        print("Deletado com Sucesso!")

if __name__ == "__main__":
    f1 = Funcionario_DAO()
    # funcionario = {"id": 2, "nome": "Alice"}
    # f1.add_funcionario(funcionario)

    try:
        for funcionario in f1.ler_funcionario():
            print(funcionario["nome"])
            print(funcionario["id"])
            print("------------------------------")
        f1.deletar_funcionario(2)
    except Exception as e:
        print("Erro:", e)