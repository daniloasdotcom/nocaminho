from fasthtml.common import *
from components.footer import footer
from components.navigation import get_prev_next

# Texto formatado em blocos separados
text_blocks = [
    "Este provérbio destaca um princípio crucial da vida cristã: a necessidade de prudência e conselho piedoso em decisões importantes.",
    "No contexto antigo, “fazer guerra” envolvia não apenas força, mas estratégia, aliança e discernimento. De forma análoga, o crente hoje enfrenta batalhas espirituais e decisões complexas em sua jornada.",
    "A sabedoria reformada enfatiza que toda verdadeira prudência começa com o temor do Senhor (Pv 1:7). Isso nos leva a buscar orientação na Palavra, na oração e no conselho de irmãos maduros na fé. A multidão de conselheiros não é qualquer grupo de vozes, mas sim pessoas enraizadas na verdade do Evangelho.",
    "Como Calvino ensinou, Deus em Sua providência soberana usa meios — e entre eles, conselhos fiéis — para nos guiar. Rejeitar conselho piedoso é abraçar a presunção; aceitar, porém, é caminhar com humildade e segurança.",
]

application_text = """
**Aplicação**: Antes de tomar grandes decisões, ore, examine as Escrituras e busque irmãos tementes a Deus. Não somos chamados à autonomia espiritual, mas a uma vida em comunidade guiada pela Palavra.
"""

def prov24_6():
    current_path = "/pv246"
    prev_study, next_study = get_prev_next(current_path)

    return Html(
        Head(
            Title("Provérbios 24:6 - Sabedoria e Conselho"),
            Link(rel="stylesheet", href="/static/styles.css")
        ),
        Body(
            Div(
                Div(
                    Div(
                        H1("Provérbios 24:6"),
                        Div(
                            '"Com medidas de prudência farás a guerra; na multidão de conselheiros está a vitória.”',
                            _class="verse-box"
                        ),
                        A("← Voltar para a página inicial", href="/", _class="back-link"),
                        _class="post-fixed-column"
                    ),
                    Div(
                        H1("Sabedoria Reformada: Prudência e Conselho"),
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