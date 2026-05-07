
from src.model.DAO.base_db import BaseDB

#estamos criando herança

class Estoque(BaseDB):
    def __init__(self):
        super().__init__("estoque.json")

    def ler_estoque(self):
        return self.read_list()


    def add_produto_estoque(self,data):
        self.save(data)


    def incrementar_produto_estoque(self,id_produto,quantidade:int):
        linha,produto=[(index,produto) for index, produto in enumerate(self.ler_estoque())
                       if produto["id"]==id_produto][0]
        produto["quantidade"]+=quantidade
        novaLista=self.ler_estoque()[linha]
        novaLista[linha]=produto

        self.save_list(novaLista)

    def decrementar_produto_estoque(self, id_produto, quantidade: int):
        linha, produto = [(index, produto) for index, produto in enumerate(self.ler_estoque())
                          if produto["id"] == id_produto][0]
        produto["quantidade"] -= quantidade
        novaLista = self.ler_estoque()[linha]
        novaLista[linha] = produto

        self.save_list(novaLista)

    def buscar_por_id_produto_estoque(self,id):
        try:
            produto_encontrado=[produto for produto in self.ler_estoque() if produto["id"] == id][0]
            return produto_encontrado
        except IndexError as e:
            raise ValueError("Produto não existe no Sistema",e)

if __name__ == '__main__':
    estoque=Estoque()
    produto= {
    "id": 6,
    "quantidade":0
    }
    estoque.add_produto_estoque(produto)
    estoque.ler_estoque()