from flet import *


class ProdutoView(View):

    def __init__(self):
        super().__init__()
        self.nome_produto=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marca_produto=TextField(label="Marca",icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.valor_produto=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add produto",icon=CupertinoIcons.PLUS,col=3)
        self.nomeFornecedor=TextField(label="Nome Fornecedor",icon=CupertinoIcons.CUBE_BOX_FILL,col=7)
        self.btnCadastrarFornecedor = Button("Add", icon=CupertinoIcons.PLUS, col=3)
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
                            self.marca_produto, self.btnCadastrarProduto
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )
                    ]
            ),
            col={"sm": 12, "md": 6},
            border=Border.all(4, "#E9EEF6"),
            padding=10,
            height=150
        )
        modalFornecedor=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeFornecedor,
                            self.btnCadastrarFornecedor
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),

                    ]
            ),
            col={"sm": 12, "md": 6},
            border=Border.all(4, "#E9EEF6"),
            padding=10,
            height=150
        )

        self.controls=[
            ResponsiveRow(
                controls=[modalProduto,modalFornecedor],
                alignment = MainAxisAlignment.SPACE_AROUND
        )
        ]
        return self.controls

