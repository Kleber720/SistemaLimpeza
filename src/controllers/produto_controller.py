from src.model.entitys.produto import Produto
from src.model.DAO.produtos_dao import Produtos_DAO
from src.infrastructure.services.geradorID import GeradorID


class ProdutoController:

    def __init__(self):
        self.dao = Produtos_DAO()

    def cadastrarProduto(self, nome: str, marca: str,unidade, valor: float, id_fornecedor: int):
        id_produto: int = GeradorID(r"C:\Users\kleber.asilva16\PycharmProjects\SistemaLimpeza\src\database\produto.json", "id").id_gerado
        p = Produto(id_produto, nome, marca,unidade, id_fornecedor,valor)
        self.dao.add_produtos(p.produtoDict())

    def listarProdutos(self) -> list:
        return self.dao.ler_produtos()

    def buscarProdutoID(self, id: int):
        try:
            return self.dao.buscar_por_ID(id)
        except Exception as e:
            return e


if __name__ == '__main__':
    p = ProdutoController()
    p.cadastrarProduto("feijao","camil",1,10.00,1)
    print(p.buscarProdutoID(11))
    # print(p.listarProdutos())

