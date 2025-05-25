from fasthtml.common import *
from components.footer import footer
from components.navigation import get_prev_next

# Texto formatado em blocos
text_blocks = [
    "Este versículo é um chamado à vigilância espiritual contínua. Em Provérbios 4:23, a sabedoria de Deus nos ensina que o coração — o centro das nossas decisões, emoções e vontades — é a origem de tudo o que flui na vida.",
    "Na tradição reformada, sabemos que o coração humano é, por natureza, corrompido pelo pecado (Jeremias 17:9), mas também é o local onde Deus opera a regeneração pelo Espírito Santo. Por isso, guardar o coração não é apenas evitar o pecado, mas também alimentá-lo com a Palavra, oração e temor do Senhor.",
    "O crente não vive de impulsos, mas de discernimento. Guardar o coração significa cultivar aquilo que honra a Deus: pensamentos santos, desejos corretos e emoções santificadas. Isso requer vigilância constante, pois tudo o que deixamos entrar — ideias, palavras, desejos — afetará o que sai: ações, decisões e palavras.",
    "A Bíblia ensina que \"a boca fala do que está cheio o coração\" (Lucas 6:45). Se queremos ter uma fala cheia de graça, devemos primeiro ter um coração cheio de Cristo."
]

application_text = """
**Aplicação**: Que sua oração diária seja: \"Senhor, guarda meu coração em Ti, que eu não me desvie para caminhos maus.\" Invista em sua comunhão com Deus, pois tudo na sua vida será afetado pelo que você cultiva no coração.
"""

def prov4_23():
    current_path = "/prov423"
    prev_study, next_study = get_prev_next(current_path)

    return Html(
        Head(
            Title("Provérbios 4:23 - Guarda o Teu Coração"),
            Link(rel="stylesheet", href="/static/styles.css")
        ),
        Body(
            Div(
                Div(
                    Div(
                        H1("Provérbios 4:23"),
                        Div('"Acima de tudo, guarde o seu coração, pois dele depende toda a sua vida.”', _class="verse-box"),
                        A("← Voltar para a página inicial", href="/", _class="back-link"),
                        _class="post-fixed-column"
                    ),
                    Div(
                        H1("Guarda o Teu Coração"),
                        *[P(para, _class="post-commentary") for para in text_blocks],
                        Div(application_text, _class="application-box"),
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