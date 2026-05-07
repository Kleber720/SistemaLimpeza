from src.main.constructor.produtoConstructor import produtoConstructor
from flet import *

def app(page:Page):
    page.title="Controle de Estoque"

    def changeRoute():
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
        )

        page.update()
    page.on_route_change=changeRoute
    changeRoute()

