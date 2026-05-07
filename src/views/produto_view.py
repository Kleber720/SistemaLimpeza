from flet import *


class ProdutoView(View):

    def __init__(self):
        super().__init__()
        self.nome_produto=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marca_produto=TextField(label="Nome",icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.valor_produto=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add produto",icon=CupertinoIcons.PLUS,col=3)
        self.nomeFornecedor=TextField(label="Nome Fornecedor",icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.route="/"


    def build(self):
        modalProduto=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nome_produto,
                            self.valor_produto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    ResponsiveRow(
                        controls=[
                            self.nome_produto,
                            self.valor_produto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )
                    ]
            ),
            col={"SM":12,"MD":6}
        )
        modalFornecedor=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeFornecedor,
                            self.btnCadastrarProduto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),

                    ]
            ),
            col={"SM":12,"MD":6}
        )

        self.controls=[
            ResponsiveRow(
                controls=[modalProduto,modalFornecedor],
                alignment = MainAxisAlignment.SPACE_AROUND
        )
        ]
        return self.controls

