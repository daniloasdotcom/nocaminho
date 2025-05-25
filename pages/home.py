# pages/home.py
from fasthtml.common import *
from routes.home_highlights import home_highlights
from components.footer import footer

def home():
    cards = [
        Div(
            H2(study["title"]),
            P(f'"{study["excerpt"]}"'),
            _class=f"column {study['column_class']}",
            onclick=f"window.location='{study['path']}'"
        ) for study in home_highlights
    ]

    return Html(
        Head(
            Title("No Caminho - Página Inicial"),
            Link(rel="stylesheet", href="/static/styles.css")
        ),
        Body(
            Div(
                H1("Bem-vindo ao 'No Caminho'"),
                P("Estudos bíblicos fundamentados na fé reformada."),
                _class="section section-white"
            ),
            Div(*cards, _class="columns section-forest-green"),
            Div(
                Blockquote("“Eu sou o caminho, a verdade e a vida...” - João 14:6"),
                _class="section section-white"
            ),
            footer()
        )
    )