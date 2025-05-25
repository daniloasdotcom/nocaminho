from fasthtml.common import *
from components.footer import footer
from components.navigation import get_prev_next

# Texto de reflexão dividido em fragmentos
text_blocks = [
    "Tiago inicia este trecho com uma advertência aos que desejam ser mestres, lembrando que seremos julgados com mais rigor. O que falamos importa, e quem ensina carrega grande responsabilidade pelas palavras que profere.",
    "Ele compara a língua aos pequenos instrumentos que controlam grandes estruturas: o freio na boca do cavalo, o leme que dirige o navio. Do mesmo modo, a língua pode direcionar toda a nossa vida — para o bem ou para o mal.",
    "Tiago alerta que, apesar de pequena, a língua pode causar grande destruição, como uma fagulha que incendeia uma floresta. Palavras impensadas podem ferir, dividir, destruir reputações e relacionamentos.",
    "Com tristeza, ele aponta a contradição humana: com a mesma língua bendizemos a Deus e amaldiçoamos pessoas feitas à Sua imagem. Isso não deve ser assim. Fontes não produzem águas doces e amargas ao mesmo tempo.",
    "O chamado final de Tiago é por coerência. Somos chamados a dominar a língua, buscando sabedoria do alto para que nossas palavras sejam fontes de vida, e não de destruição. Isso exige humildade e disciplina espiritual."
]

# Texto bíblico de Tiago 3:1–12 com numeração
tiago_verses = [
    (1, "Meus irmãos, não sejam muitos de vocês mestres, sabendo que seremos julgados com mais rigor."),
    (2, "Pois todos tropeçamos em muitas coisas. Se alguém não tropeça no falar, é um homem perfeito, capaz de refrear também todo o corpo."),
    (3, "Ora, se pomos freios na boca dos cavalos para que nos obedeçam, também lhes dirigimos o corpo inteiro."),
    (4, "Vejam também os navios: sendo tão grandes e impelidos por fortes ventos, são dirigidos por um pequeno leme conforme a vontade do piloto."),
    (5, "Assim também a língua é um pequeno órgão do corpo, mas se gaba de grandes feitos. Vejam como uma pequena chama incendeia uma grande floresta."),
    (6, "A língua também é um fogo; é um mundo de iniquidade. Ela está situada entre os nossos membros, contamina o corpo inteiro e incendeia o curso da existência humana, sendo por sua vez incendiada pelo inferno."),
    (7, "Pois toda espécie de feras, aves, répteis e seres do mar se doma e tem sido domada pelo ser humano,"),
    (8, "mas a língua, nenhum dos homens é capaz de domar. É um mal incontrolável, carregado de veneno mortífero."),
    (9, "Com ela, bendizemos o Senhor e Pai; e com ela, amaldiçoamos os homens, feitos à semelhança de Deus."),
    (10, "Da mesma boca procedem bênção e maldição. Meus irmãos, isso não deveria ser assim."),
    (11, "Acaso pode uma fonte jorrar do mesmo lugar o que é doce e o que é amargo?"),
    (12, "Meus irmãos, acaso a figueira pode produzir azeitonas, ou a videira figos? Tampouco uma fonte de água salgada pode dar água doce.")
]

def tiago3():
    current_path = "/tiago3"
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
            Title("Tiago 3: O Poder da Língua"),
            Link(rel="stylesheet", href="/static/styles.css"),
            Script(src="/static/scroll-handler.js", type="text/javascript")
        ),
        Body(
            Div(
                Div(
                    Div(
                        H1("Tiago 3:1–12"),
                        Div(
                            *[P(f"{num}. {text}") for num, text in tiago_verses],
                            _class="verse-box"
                        ),
                        A("← Voltar para a página inicial", href="/", _class="back-link"),
                        _class="post-fixed-column"
                    ),
                    Div(
                        H1("Reflexão sobre o Poder da Língua"),
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