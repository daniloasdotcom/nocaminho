from fasthtml.common import *
from pages.home import home
from post.mateus5 import mateus5
from post.prov423 import prov4_23
from post.pv246 import prov24_6
from post.tiago3 import tiago3  # ← NOVO
from pages.todos_os_estudos import todos_os_estudos

# Cria a aplicação e o roteador
app, rt = fast_app(static_dir="static")

# Configuração das rotas
@rt('/')
def route_home():
    return home()

@rt('/mateus5')
def route_mateus5():
    return mateus5()

@rt('/pv246')
def route_pv246():
    return prov24_6()

@rt('/prov423')
def route_prov4_23():
    return prov4_23()

@rt('/tiago3')  # ← NOVA ROTA
def route_tiago3():
    return tiago3()

@rt('/todos_os_estudos')
def route_todos_estudos():
    return todos_os_estudos()

# Só executa o servidor localmente
if __name__ == "__main__":
    serve()