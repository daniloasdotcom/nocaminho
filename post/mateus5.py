from fasthtml.common import *
from components.footer import footer
from components.navigation import get_prev_next

text_blocks = [
    "Esse versículo de Mateus 5:3 é o ponto inicial do Sermão da Montanha, onde Jesus começa a ensinar sobre as bem-aventuranças — uma série de bênçãos dirigidas àqueles que, de maneira humilde, encontram em Deus sua força e esperança.",
    "Mas o que significa ser “pobre de espírito”? Ser pobre de espírito não é ser desprovido de valor ou dignidade. Pelo contrário, é reconhecer que, por nós mesmos, somos limitados e incompletos.",
    "A pobreza de espírito é uma abertura para a graça, é um convite para deixar de lado o orgulho e a autossuficiência e, com humildade, reconhecer nossa dependência de Deus.",
    "Quem é pobre de espírito sabe que o próprio ego não basta e que a verdadeira força vem de algo muito maior — de Deus. Essa pessoa se abre para receber o amor e a orientação divina.",
    "Assim, o Reino dos Céus não é prometido aos poderosos ou autossuficientes, mas aos humildes, aos que reconhecem suas limitações e confiam na graça do Senhor."
]

def mateus5():
    current_path = "/mateus5"
    prev_study, next_study = get_prev_next(current_path)
    total_blocks = len(text_blocks)

    content_fragments = [
        Div(
            Div(
                P(block, _class="post-commentary"),
                Div(f"{i+1}/{total_blocks}", _class="fragment-counter") if i + 1 < total_blocks else "",
                Button("↓", _class="down-arrow active-arrow" if i == 0 else "down-arrow") if i + 1 < total_blocks
                else Div("fim", _class="end-label"),
                _class="fragment-inner"
            ),
            id=f"block-{i}",
            _class="fragment" + (" visible" if i == 0 else "")
        )
        for i, block in enumerate(text_blocks)
    ]

    return Html(
        Head(
            Title("Mateus 5:3 - Humildade de Espírito"),
            Link(rel="stylesheet", href="/static/styles.css"),
            Script(src="/static/scroll-handler.js", type="text/javascript")
        ),
        Body(
            Div(
                Div(
                    Div(
                        H1("Mateus 5:3"),
                        Div(
                            P('"Bem-aventurados os humildes de espírito, porque deles é o reino dos céus."'), _class="verse-box"),
                        A("← Voltar para a página inicial", href="/", _class="back-link"),
                        _class="post-fixed-column"
                    ),
                    Div(
                        H1("Reflexão Inspiradora"),
                        *content_fragments,
                        Div(
                            A("← Estudo Anterior", href=prev_study["path"]) if prev_study else "",
                            A("Próximo Estudo →", href=next_study["path"]) if next_study else "",
                            _class="study-nav-links"
                        ),
                        _class="post-scrollable-column"
                    ),
                    _class="post-container"
                ),
                _class="post-page"
            ),
            footer()
        )
    )