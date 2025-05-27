from fasthtml.common import *
from components.footer import footer
from components.navigation import get_prev_next # Supondo que esta função lide com a lista de estudos

# Texto de reflexão ajustado para Salmos 1, com foco na interpretação fornecida
text_blocks_salmos1 = [
    "O Salmo 1 é um convite inspirador para a vida abundante que floresce quando nossa jornada é guiada pela Palavra do Senhor. Ele nos oferece um caminho claro para responder à pergunta essencial: 'Como posso viver os propósitos de Deus para mim?'.",
    "Este Salmo descreve a profunda experiência daquele que encontra verdadeiro prazer na lei do Senhor. Não como um conjunto de regras frias, mas como uma fonte de sabedoria e vida, na qual ele medita dia e noite, permitindo que ela molde seu coração e suas escolhas.",
    "Ao se abster dos conselhos dos ímpios, de parar nos caminhos dos pecadores e de se assentar com zombadores (v.1), o justo demonstra uma decisão consciente. Ele escolhe ativamente nutrir sua vida com a verdade divina, em vez de se deixar levar por influências que o afastariam dos propósitos de Deus.",
    "A imagem da árvore plantada junto a ribeiros (v.3) ilustra vividamente os resultados dessa vida: estabilidade, fruto no tempo certo e vitalidade constante. Assim é aquele que se deleita e medita na Palavra: ele prospera, não necessariamente em termos materiais, mas em realizar os propósitos de Deus, experimentando a verdadeira vida.",
    "Portanto, o Salmo 1 não apenas contrasta o caminho dos justos e dos ímpios, mas fundamentalmente nos chama a encontrar alegria, orientação e propósito duradouro ao mergulhar continuamente na Palavra de Deus, permitindo que ela seja a luz para o nosso caminho e o alicerce da nossa vida."
]

# Texto bíblico de Salmos 1 com numeração (NVI)
salmos1_verses = [
    (1, "Bem-aventurado aquele que não anda segundo o conselho dos ímpios, não se detém no caminho dos pecadores, nem se assenta na companhia dos zombadores."),
    (2, "Ao contrário, a sua satisfação está na lei do Senhor, e na sua lei medita dia e noite."),
    (3, "É como árvore plantada junto a ribeiros: dá fruto no tempo certo e as suas folhas não murcham. Tudo o que ele faz prospera."),
    (4, "Não é o caso dos ímpios! São como palha que o vento leva."),
    (5, "Por isso, os ímpios não resistirão no julgamento, nem os pecadores na comunidade dos justos."),
    (6, "Porque o Senhor conhece o caminho dos justos, mas o caminho dos ímpios leva à destruição!")
]

def salmos1():
    current_path = "/salmos01"
    
    prev_study, next_study = get_prev_next(current_path)
    total_blocks = len(text_blocks_salmos1)

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
        for i, block in enumerate(text_blocks_salmos1)
    ]

    return Html(
        Head(
            Title("Salmos 1: O Caminho para Viver os Propósitos de Deus"), # Título ajustado
            Link(rel="stylesheet", href="/static/styles.css"),
            Script(src="/static/scroll-handler.js", type="text/javascript")
        ),
        Body(
            Div(
                Div(
                    Div(
                        H1("Salmos 1"),
                        Div(
                            *[P(f"{num}. {text}") for num, text in salmos1_verses],
                            _class="verse-box"
                        ),
                        A("← Voltar para a página inicial", href="/", _class="back-link"),
                        _class="post-fixed-column"
                    ),
                    Div(
                        H1("Reflexão: Vivendo os Propósitos de Deus pela Sua Palavra"), # H1 da reflexão ajustado
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