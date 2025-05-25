from fasthtml.common import *
from routes.studies import studies
from components.footer import footer

def todos_os_estudos():
    cards = [
        Div(
            H3(study["reference"]),
            P(study["title"], _class="study-card-title"),
            A("→ Ler estudo", href=study["path"], _class="study-card-link"),
            _class="study-card"
        ) for study in studies
    ]

    return Html(
        Head(
            Title("Todos os Estudos"),
            Link(rel="stylesheet", href="/static/styles.css")
        ),
        Body(
            Div(
                H1("Todos os Estudos"),
                Div(*cards, _class="study-grid"),
                A("← Voltar para a página inicial", href="/", _class="back-link"),
                _class="section section-white"
            ),
            footer()
        )
    )