from fasthtml.common import *

def footer():
    return Div(
        P("© 2024 Meu Aplicativo. Todos os direitos reservados."),
        P(
            A("Todos os Estudos", href="/todos_os_estudos"),
            A("Sobre", href="#"),
            A("Contato", href="#"),
            A("Privacidade", href="#"),
            A("Termos", href="#"),
            A("Facebook", href="https://facebook.com", target="_blank"),
            A("Twitter", href="https://twitter.com", target="_blank"),
            A("Instagram", href="https://instagram.com", target="_blank"),
            _class="footer-links"
        ),
        _class="footer"
    )