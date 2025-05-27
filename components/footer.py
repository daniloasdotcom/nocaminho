from fasthtml.common import *
import datetime # Importe o módulo datetime

def footer():
    current_year = datetime.date.today().year # Obtém o ano corrente
    return Div(
        P(f"© {current_year} Meu Aplicativo. Todos os direitos reservados."),
        P(
            A("Todos os Estudos", href="/todos_os_estudos") # Link "Todos os Estudos" restaurado
        ),
        P(
            "Desenvolvido em fastHTML, e criado e mantido por Danilo (",
            A("daniloas.com", href="http://daniloas.com", target="_blank"),
            ")."
        ),
        _class="footer"
    )