#!/usr/bin/env python3
"""Gera HTML da Aula 1.1 (Módulo 1) — O que são indicadores?"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo1" / "aula1"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 1
MODULE_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA_LABEL = "Aula 1"
AULA_TITLE = "O que são indicadores?"
AULA2_TITLE = "Atributos desejáveis e seleção de indicadores"

# URL do vídeo NIPPIS — substituir quando disponível (YouTube watch?v=...)
NIPPIS_VIDEO_URL = ""

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("Indicadores sociais: conceitos e usos", "Indicadores sociais: conceitos e usos"),
    ("Indicadores de saúde", "Indicadores de saúde"),
    ("Formas de classificação de indicadores", "Formas de classificação de indicadores"),
    ("Referências", "Referências"),
]

OBJECTIVES = [
    "Conhecer os principais conceitos e definições relacionados a indicadores, indicadores sociais e indicadores de saúde;",
    "Apreender formas de classificar indicadores.",
]

AUTHORS = [
    (
        "Aline Pinto Marques",
        "Doutora em Epidemiologia em Saúde Pública. Instituto de Comunicação e Informação "
        "Científica e Tecnológica em Saúde (Icict) da Fundação Oswaldo Cruz (Fiocruz).",
    ),
    (
        "Carolina de Campos Carvalho",
        "Doutora e Mestre em Saúde Pública, Analista Técnica de Políticas Sociais. Instituto de "
        "Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da Fundação "
        "Oswaldo Cruz (Fiocruz).",
    ),
]

REFERENCES = [
    'BARCELLOS, C.; XAVIER, D. R. As diferentes fases, os seus impactos e os desafios da pandemia de COVID-19 no Brasil. <strong>RECIIS – Revista Eletrônica de Comunicação, Informação e Inovação em Saúde</strong>, [S. l.], v. 16, n. 2, 2022. Disponível em: <a href="https://www.reciis.icict.fiocruz.br/index.php/reciis/article/view/3349" target="_blank" rel="noopener noreferrer">https://www.reciis.icict.fiocruz.br/index.php/reciis/article/view/3349</a>. Acesso em: 14 fev. 2026. DOI: <a href="https://doi.org/10.29397/reciis.v16i2.3349" target="_blank" rel="noopener noreferrer">https://doi.org/10.29397/reciis.v16i2.3349</a>.',
    'DONABEDIAN, A. Evaluating the quality of medical care. <strong>The Milbank Memorial Fund Quarterly</strong>, v. 44, n. 3, p. 166–206, 1966. Suplemento. Reimpresso em: <strong>Milbank Quarterly</strong>, v. 83, n. 4, p. 691–729, 2005.',
    'JANNUZZI, P. de M. <strong>Indicadores sociais no Brasil</strong>. 6. ed. Campinas: Alínea, 2017. 3. impr. 2024.',
    'ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). <strong>Indicators for policy management: a guide for enhancing the statistical capacity of policy-makers for effective monitoring of the MDGs at the country level</strong>. New York: United Nations, 2005.',
    'ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE (OPAS). <strong>Indicadores de saúde: elementos conceituais e práticos</strong>. Washington, DC: OPAS, 2018. Disponível em: <a href="https://iris.paho.org/bitstream/handle/10665.2/49057/9789275720059_por.pdf" target="_blank" rel="noopener noreferrer">https://iris.paho.org/bitstream/handle/10665.2/49057/9789275720059_por.pdf</a>. Acesso em: 14 fev. 2026.',
    'REDE INTERAGENCIAL DE INFORMAÇÃO PARA A SAÚDE (RIPSA). <strong>Indicadores básicos para a saúde no Brasil: conceitos e aplicações</strong>. Brasília, DF: Organização Pan-Americana da Saúde, 2008. 349 p. Disponível em: <a href="https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/" target="_blank" rel="noopener noreferrer">https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/</a>. Acesso em: 14 fev. 2026.',
    'ROMERO, D.; MARQUES, A.; MUZY, J. <strong>Informação e indicadores: conceitos, fontes e aplicações para a saúde do idoso e envelhecimento</strong> [recurso eletrônico]. Rio de Janeiro: Edições Livres, 2021.',
    'ROUQUAYROL, M. Z.; ALMEIDA FILHO, N. (org.). <strong>Epidemiologia e saúde</strong>. 5. ed. Rio de Janeiro: MEDSI, 1999.',
]


def row(inner: str, mb: str = "mb-5") -> str:
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 {mb}">'
        f"{inner}</div></div>\n"
    )


def p(text: str) -> str:
    return f"<p>{text}</p>"


def heading(topic_num: int, title: str) -> str:
    return row(
        f'<div class="heading__block"><span class="small">Tópico {topic_num}</span>'
        f'<h3 class="heading__title">{title}</h3></div>',
        "mb-5",
    )


def subheading(title: str, tag: str = "h4") -> str:
    return row(f'<div class="heading__block"><{tag} class="heading__title">{title}</{tag}></div>', "mb-4")


def box_html(kind: str, label: str, body_html: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f"{body_html}</div></div></div>"
    )


def box(kind: str, label: str, body: str) -> str:
    return box_html(kind, label, f'<p class="mb-0">{body}</p>')


ATENCAO_DIVIDER = (
    '<div class="custom-shape-divider-top-1720289331">'
    '<svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">'
    '<path d="M1200 120L0 16.48 0 0 1200 0 1200 120z" class="shape-fill"></path>'
    "</svg></div>"
)


def atencao_box(body_html: str) -> str:
    return row(
        '<div class="box" data-box="Atenção">'
        '<div class="card aos-init aos-animate" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="600">'
        '<div class="card-header">'
        '<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        '<span class="label">Atenção</span></div>'
        '<div class="card-body">'
        f"{ATENCAO_DIVIDER}<div>{body_html}</div>"
        "</div></div></div>"
    )


def bullet_list(items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"<ul>{lis}</ul>"


def list_group(items: list[str]) -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{item}</li>' for item in items
    )
    return row(f'<div class="list"><ul class="list-group">{lis}</ul></div>')


def quotation_block(quote: str, author: str = "", intro: str = "") -> str:
    intro_html = f"{intro} " if intro else ""
    author_html = f'<span class="quotation-autor">{author}</span>' if author else ""
    return row(
        '<div class="quotation"><blockquote>'
        '<div class="quotation-body"><span class="quotation-mark fa1"></span>'
        f"<p>{intro_html}<em>{quote}</em></p>"
        f"{author_html}"
        '</div><span class="quotation-mark fa2"></span>'
        "</blockquote></div>"
    )


def flipcard(card_id: str, title: str, back_html: str, *, col: str = "col-12 col-md-6") -> str:
    return (
        f'<div class="{col}"><div class="flipcard"><div class="flip-card">'
        f'<input type="checkbox" id="{card_id}" class="more" aria-hidden="true" />'
        f'<div class="flip-card-inner"><div class="card shadow flip-card-front fundo1">'
        f'<div class="h-100 bg-transparent border-0 text-center"><div class="card-body justify-content-center d-flex flex-column">'
        f'<span class="h5 card-title">{title}</span></div>'
        f'<div class="card-footer text-white"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-primary" aria-hidden="true">'
        f'<img src="{ASSETS}media/templates/flipcard-icon-dark.svg" alt="" width="36" /> Confira</label>'
        f"</div></div></div></div>"
        f'<div class="card flip-card-back"><div class="h-100 bg-transparent border-0 text-center">'
        f'<div class="card-body justify-content-center d-flex flex-column">'
        f'<span class="h5 card-title">{title}</span>'
        f'<div class="scrollable text-start">{back_html}</div></div>'
        f'<div class="card-footer"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-secondary return" aria-hidden="true">'
        f'<span class="material-symbols-rounded">arrow_back</span></label></div></div></div></div></div></div></div></div>'
    )


def flip_row(*cards: str) -> str:
    return (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8">'
        '<div class="row g-4 mb-5">'
        + "".join(cards)
        + "</div></div></div>"
    )


def video_embed(youtube_url: str, title: str = "Vídeo") -> str:
    if "embed/" in youtube_url:
        src = youtube_url
    else:
        vid = youtube_url.split("v=")[-1].split("&")[0]
        src = f"https://www.youtube.com/embed/{vid}"
    return (
        f'<div class="ratio ratio-16x9"><iframe src="{src}" '
        f'title="{title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        f'gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe></div>'
    )


def video_box(intro: str, title: str = "Indicadores sociais — NIPPIS") -> str:
    if NIPPIS_VIDEO_URL:
        body = f'<p class="mb-3">{intro}</p>{video_embed(NIPPIS_VIDEO_URL, title)}'
    else:
        body = (
            f'<p class="mb-3">{intro}</p>'
            '<p class="mb-0"><em>Link do vídeo a ser inserido.</em></p>'
        )
    return box_html("Para Assistir", "Para Assistir!", body)


def topic_list_html(current: int) -> str:
    items = []
    for i, (label, _) in enumerate(TOPICS, 1):
        status = ' status="visited"' if i < current else ""
        aria = 'aria-label="Tópico concluído"' if i < current else 'aria-label="Tópico não concluído"'
        items.append(
            f'\t\t\t\t\t\t\t<a href="topico{i}.html" tabindex="0" role="link" class="topic-list__item" {aria}{status}>'
            f'<span class="material-symbols-rounded"></span>{label}</a>'
        )
    return "\n".join(items)


def page_nav(num: int) -> str:
    parts = []
    if num > 1:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num - 1}.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        )
    if num < len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num + 1}.html" rel="next">Próximo tópico '
            f'<span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    else:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../aula2/topico1.html" rel="next">Próxima aula '
            '<span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    inner = "".join(parts)
    return (
        f'\t\t\t<section><div class="container"><div class="row justify-content-center">'
        f'<div class="col-12 col-md-10 col-lg-8"><div class="page-nav d-flex justify-content-evenly flex-wrap gap-3">'
        f"{inner}</div></div></div></div></section>\n"
    )


def build_sidebar(current: int) -> str:
    topics = topic_list_html(current)
    return f"""				<div class="sidebar__group d-lg-none">
					<div class="sidebar__group-item">
						<div class="sidebar__header">
							<span>Curso</span>
							<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
						</div>
					</div>
					<div class="sidebar__group-item"><div class="sidebar__title"><h1>{COURSE_TITLE}</h1></div></div>
					<div class="sidebar__group-item">
						<ul class="nav">
							<li class="nav-item"><a href="{ASSETS}index.html" class="nav-link" tabindex="0"><span class="icon material-symbols-rounded" aria-hidden="true">home</span>Início</a></li>
							<li class="nav-item"><a href="#" class="nav-link" tabindex="0" data-bs-toggle="modal" data-bs-target="#modal-creditos"><span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>Créditos</a></li>
						</ul>
					</div>
				</div>
				<div class="sidebar__group">
					<div class="sidebar__group-item">
						<div class="dropend">
							<button id="dropdown-modulos" type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">grid_view</span><span class="label">Módulos</span>
							</button>
							<ul class="dropdown-menu" aria-labelledby="dropdown-modulos">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />{MODULE_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />Calculando indicadores</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo3/aula1/topico1.html"><strong>Módulo 3</strong><br />Uso de indicadores</a></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="divider"><hr /></div>
				<div class="sidebar__group">
					<div class="sidebar__group-item"><span class="text module">Módulo <br class="d-none d-lg-block" /><span>{MODULE_NUM}</span></span></div>
					<div class="sidebar__group-item">
						<div class="dropend">
							<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">apps</span><span class="label">Conteúdo</span>
							</button>
							<ul class="dropdown-menu">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__title"><span class="label">Módulo {MODULE_NUM}</span><span class="title">{MODULE_TITLE}</span></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>{AULA2_TITLE}</a></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="divider"><hr /></div>
				<div class="sidebar__group">
					<div class="sidebar__group-item"><span class="text class">{AULA_LABEL}</span></div>
					<div class="sidebar__group-item">
						<div class="dropend">
							<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span><span class="label">Tópicos</span>
							</button>
							<ul class="dropdown-menu">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__title"><span class="label">{AULA_LABEL}</span><span class="title">{AULA_TITLE}</span></li>
								<li class="dropdown-menu__item"><nav class="topic-list">
{topics}
							</nav></li>
							</ul>
						</div>
					</div>
				</div>"""


def build_page(num: int, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=yes" />
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="robots" content="noindex" />
	<meta name="author" content="Fiocruz, Campus Virtual" />
	<meta name="description" content="Curso {COURSE_TITLE}" />
	<link rel="apple-touch-icon" sizes="180x180" href="{ASSETS}media/icons/apple-icon-180x180.png" />
	<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}media/icons/favicon-32x32.png" />
	<link rel="manifest" href="../media/icons/manifest.json" />
	<meta name="theme-color" content="#001833" />
	<title>Curso {COURSE_TITLE} | Mod {MODULE_NUM} | {AULA_LABEL}</title>
	<link rel="stylesheet" href="{ASSETS}source/bootstrap-5.1.3/css/bootstrap.min.css" />
	<link rel="stylesheet" href="{ASSETS}assets/css/style.css" />
</head>
<body>
	<header class="header">
		<div class="mobile-toggle-open"><a class="mobile-toggle__button" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></div>
		<div class="brand"><img class="img-fluid logo-black" src="{ASSETS}media/logos/header-fiocruz-campus-virtual.png" alt="Campus Virtual Fiocruz" /></div>
		<div class="title"><h1>{COURSE_TITLE}</h1></div>
		<ul class="nav nav-pills">
			<li class="nav-item"><a href="{ASSETS}index.html" class="nav-link">Início</a></li>
			<li class="nav-item"><a href="#" class="nav-link" data-bs-toggle="modal" data-bs-target="#modal-creditos">Créditos</a></li>
		</ul>
	</header>
	<div class="main">
		<div class="sidebar" role="navigation">
			<div class="sidebar__inner" style="position: relative">
{build_sidebar(num)}
			</div>
		</div>
		<div class="content">
			<div id="page-title"><div class="container"><div class="row align-items-center hstify-content-center justify-content-xxl-start ms-lg-5"><div class="col-12 col-md-10 col-lg-11"><h2 class="title"><span class="label">Módulo {MODULE_NUM} | {AULA_LABEL}</span><br />{AULA_TITLE}</h2></div></div></div></div>
			<div id="page-content" class="">
				<section><div class="container">
{content}				</div></section>
			</div>
{page_nav(num)}		</div>
		<footer>
			<div class="container-fluid">
				<div class="row justify-content-center align-items-center linha-de-marcas">
					<div class="col-12 text-center py-3">
						<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: Campus Virtual Fiocruz, Fiocruz, SUS Digital, SUS 35 Anos, Ministério da Saúde e Governo do Brasil" />
					</div>
				</div>
			</div>
		</footer>
	</div>
	<script src="{ASSETS}source/bootstrap-5.1.3/js/bootstrap.bundle.min.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/ResizeSensor.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/sticky-sidebar.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/sidebar.js"></script>
	<script type="text/javascript">var sidebar = new StickySidebar(".sidebar", {{ topSpacing: 0, bottomSpacing: 0, containerSelector: ".main", innerWrapperSelector: ".sidebar__inner", minWidth: 991 }});</script>
	<script type="text/javascript" src="{ASSETS}assets/js/scripts.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/custom-anime.js"></script>
	<script type="text/javascript" src="{ASSETS}source/animate/aos/dist/aos.js"></script>
	<script>AOS.init();</script>
</body>
</html>
"""


def content_topico1() -> str:
    objs = "".join(
        f'<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" '
        f'data-aos-easing="ease-out" data-aos-duration="1200">{o}</li>'
        for o in OBJECTIVES
    )
    auth_blocks = "".join(
        row(f"<p><strong>{name}</strong></p><p>{bio}</p>") for name, bio in AUTHORS
    )
    return (
        heading(1, TOPICS[0][1])
        + row(p('Seja bem-vindo e bem-vinda à aula <strong>"O que são indicadores?"</strong>.'))
        + row(
            p(
                "Nesta aula, serão apresentados os conceitos fundamentais relacionados a indicadores, "
                "com foco nos indicadores sociais e de saúde. O objetivo é oferecer uma compreensão inicial "
                "sobre o que são indicadores, para que servem e como são utilizados na análise de diferentes "
                "dimensões da realidade social e sanitária."
            )
        )
        + row(
            "<p>Ao final dessa aula, você será capaz de:</p>"
            '<div class="list"><ul class="list-group">'
            + objs
            + "</ul></div>"
        )
        + subheading("Autoria")
        + auth_blocks
    )


def content_topico2() -> str:
    jannuzzi_quote = (
        "um indicador social é uma medida, em geral, quantitativa, dotada de significado social substantivo, "
        "e é usado para aproximar, quantificar ou operacionalizar um conceito social abstrato, de interesse "
        "teórico (para pesquisa acadêmica) ou programático (para formulação de políticas); ele aponta, "
        "aproxima, traduz em termos operacionais as dimensões sociais de interesse definidas com base em "
        "escolhas teóricas ou políticas realizadas anteriormente"
    )
    functions = [
        "Permitem conhecer melhor a realidade social;",
        "Possibilitam identificar desigualdades entre grupos populacionais;",
        "Ajudam a monitorar e avaliar programas e políticas públicas;",
        "Subsidiam pesquisas acadêmicas;",
        "Orientam ações governamentais e institucionais.",
    ]
    return (
        heading(2, TOPICS[1][1])
        + row(
            p(
                "Os indicadores sociais constituem instrumentos fundamentais para compreender, monitorar "
                "e avaliar diferentes dimensões da vida em sociedade. Eles são particularmente importantes "
                "nas áreas de políticas públicas, planejamento governamental, pesquisa social e avaliação "
                "de programas. Em termos gerais, indicadores são medidas que sintetizam aspectos relevantes "
                "da realidade, permitindo observar tendências, identificar problemas e subsidiar tomadas de "
                "decisão mais precisas. Os indicadores sociais surgem da necessidade de transformar dados "
                "brutos em informações significativas, capazes de orientar intervenções e análises mais robustas."
            )
        )
        + row(
            p(
                "<strong>Indicadores são medidas síntese que refletem determinado aspecto da realidade.</strong> Eles são "
                "constituídos por dados ou variáveis que informam sobre um fenômeno, evento, ou dimensão "
                "da realidade."
            )
        )
        + row(
            p(
                "Dados e indicadores possuem significados diferentes e é muito importante a diferenciação "
                "de ambos os conceitos. Os dados são registros não processados e brutos, utilizados como "
                "matéria-prima na elaboração de indicadores. Já os indicadores são medidas derivadas e "
                "construídas a partir dos dados para fornecer uma visão mais significativa, interpretativa e "
                "contextualizada de um fenômeno específico."
            )
        )
        + row(
            p(
                "Nesta aula, nosso foco será nos indicadores sociais, em especial naqueles utilizados no "
                "campo da saúde pública. Conheça a definição de indicador social segundo o pesquisador "
                "Paulo de Martino Jannuzzi:"
            )
        )
        + quotation_block(jannuzzi_quote, "(JANNUZZI, 2024, P.21).")
        + row(
            p(
                'Tomemos como exemplo um "conceito social abstrato": o desemprego. Embora o desemprego seja um '
                "fenômeno social abstrato, ele é operacionalizado por meio da taxa de desocupação, que calcula "
                "o percentual de pessoas na força de trabalho que se encontram sem emprego, mas estão disponíveis "
                "e procurando trabalho. Para isso, utiliza-se uma definição específica — como a do IBGE<sup>1</sup>, "
                "que considera desempregada a pessoa com idade para trabalhar (acima de 14 anos), que não exerce "
                "atividade remunerada, mas está disponível e tentando conseguir trabalho."
            )
        )
        + row(
            p(
                "A partir dessa definição, dados brutos são coletados e transformados em um indicador que "
                "permite avaliar as condições do mercado de trabalho, o impacto de crises econômicas e a "
                "efetividade de políticas de emprego. Esse processo demonstra como os indicadores sociais "
                "resultam da soma entre dados empíricos e escolhas teóricas ou metodológicas."
            )
        )
        + row(
            p(
                "Dessa forma, a partir de um evento empírico da realidade e da operacionalização de um "
                "conceito, podemos agregar e sintetizar os dados em um indicador social, o que permite a "
                "quantificação e a avaliação das informações produzidas."
            )
        )
        + row(bullet_list(functions))
        + row(
            p(
                "No contexto da administração pública, os indicadores cumprem papel ainda mais estratégico. "
                "Eles permitem a comunicação mais eficiente entre a população e as instituições governamentais, "
                "além de possibilitar comparações entre diferentes períodos, localidades ou grupos sociais. "
                "Essa capacidade comparativa torna os indicadores essenciais para a avaliação e o "
                "acompanhamento de políticas públicas, bem como para a identificação de desigualdades, "
                "necessidades sociais e tendências populacionais. Não por acaso, ao longo do tempo, inúmeros "
                "indicadores foram consolidados como medidas robustas e amplamente reconhecidas, como a taxa "
                "de mortalidade infantil — simples, de fácil interpretação e utilizada em escala internacional."
            )
        )
        + row(
            p(
                "Contudo, é importante destacar que o uso de indicadores demanda atenção a diversos aspectos "
                "técnicos. Diferenças nas definições, métodos de cálculo, fontes de dados, formas de coleta e "
                "tempo de processamento podem gerar variações significativas nos resultados. Por isso, ao "
                "comparar indicadores produzidos por diferentes instituições ou países, é fundamental considerar "
                "esses elementos."
            )
        )
        + video_box(
            "Agora assista ao vídeo produzido pelo Núcleo de Informação, Políticas Públicas e Inclusão Social "
            "(NIPPIS) sobre indicadores sociais:"
        )
        + row(
            '<p class="small"><sup>1</sup> Instituto Brasileiro de Geografia e Estatística.</p>',
            "mb-5",
        )
    )


def content_topico3() -> str:
    return (
        heading(3, TOPICS[2][1])
        + row(
            p(
                "Os indicadores de saúde são amplamente utilizados para analisar a situação de saúde, "
                "acompanhar políticas e ações, além de apoiar atividades administrativas, como a geração de "
                "relatórios e documentos técnicos. Diversos sistemas de informação organizam e disponibilizam "
                "dados essenciais para sua construção, sendo constantemente aprimorados para fins de pesquisa "
                "e gestão. Com o crescimento da disponibilidade de dados em saúde, várias instituições "
                "desenvolveram definições próprias para esses indicadores."
            )
        )
        + row(
            p(
                "Para a Organização Pan-Americana da Saúde (OPAS, 2018) indicadores de saúde são medidas-síntese "
                "que tornam visíveis e mensuráveis situações que, isoladamente, não se apresentam de forma "
                "evidente. Os indicadores convertem fenômenos complexos em informações objetivas, contemplando "
                "diferentes dimensões da saúde e descrevendo aspectos relacionados às condições de saúde de uma "
                "população e ao funcionamento dos sistemas de saúde."
            )
        )
        + row(
            p(
                "A Rede Interagencial de Informações para a Saúde (RIPSA, 2008), por sua vez, define os "
                "indicadores como medidas-síntese que reúnem informações essenciais sobre atributos e dimensões "
                "específicas do estado de saúde de uma população. Para a rede, esses instrumentos são valiosos "
                "tanto no acompanhamento contínuo quanto na avaliação de eventos e processos relacionados à saúde."
            )
        )
        + row(
            p(
                "De maneira geral, os indicadores de saúde revelam aspectos da situação sanitária de uma "
                "população, sempre referenciados no tempo e no espaço, facilitando o olhar analítico por meio "
                "de sua apresentação estruturada e por séries históricas que permitem acompanhar tendências. "
                "Sua utilidade depende diretamente da qualidade dos dados que lhes dão origem — informações "
                "válidas e confiáveis são indispensáveis para gerar indicadores robustos e adequados às "
                "necessidades de pesquisa e gestão."
            )
        )
        + row(
            p(
                "Além disso, muitos indicadores não são, necessariamente, exclusivos do setor saúde. Indicadores "
                "sociais, econômicos e ambientais também fornecem insumos valiosos para compreender determinantes "
                "da saúde, uma vez que esta é influenciada por múltiplas dimensões do contexto de vida das "
                "populações. Indicadores construídos segundo critérios geográficos, por exemplo, tornam evidentes "
                "desigualdades entre países, cidades e regiões, enquanto indicadores calculados para grupos sociais "
                "específicos permitem analisar desigualdades dentro de um mesmo território. Para garantir "
                "comparabilidade, é essencial padronizar todas as etapas do trabalho: coleta, armazenamento, "
                "manipulação e análise de dados, esclarecendo sempre a localização geográfica, o período de "
                "referência e a abrangência do indicador."
            )
        )
        + row(
            p(
                "Devemos ainda ter em mente que a elaboração de indicadores de saúde é um processo dinâmico. "
                "À medida que as sociedades mudam, novos problemas de saúde ganham relevância. A pandemia da "
                "Covid-19, por exemplo, trouxe diferentes desafios para o sistema de saúde dos países, inclusive "
                "em relação à adoção de indicadores para monitorar a evolução da situação de saúde da população, "
                'conforme discutido neste <a href="https://www.reciis.icict.fiocruz.br/index.php/reciis/article/view/3349" '
                'target="_blank" rel="noopener noreferrer">artigo</a>.'
            )
        )
    )


def content_topico4() -> str:
    dsd_items = [
        "Ambiente (ex.: exposição a poluentes atmosféricos);",
        "Condições econômicas (ex.: taxa de informalidade — proporção de trabalhadores sem carteira de trabalho assinada ou registro formal);",
        "Características urbanas (ex.: densidade de áreas verdes).",
    ]
    jannuzzi_class = [
        "<strong>Indicadores-insumo:</strong> medidas associadas aos recursos humanos, financeiros e de equipamentos disponíveis.",
        "<strong>Indicadores-processo:</strong> medidas de processos intermediários, que referem-se ao esforço da alocação dos insumos para a obtenção de melhorias efetivas.",
        "<strong>Indicadores-produto:</strong> medidas referentes às entregas dos programas e políticas.",
        "<strong>Indicadores-resultado:</strong> medidas vinculadas ao cumprimento dos objetivos dos programas e políticas; permitem avaliar a eficácia do cumprimento das metas.",
        "<strong>Indicadores-impacto:</strong> medidas relacionadas às consequências e desdobramentos mais gerais dos programas e políticas.",
    ]
    return (
        heading(4, TOPICS[3][1])
        + row(
            p(
                "Existem diversas formas de classificar indicadores, cada uma permitindo analisar diferentes "
                "aspectos da realidade observada. Essas classificações facilitam a interpretação das informações "
                "ao explicitar o que o indicador é capaz de medir e quais dimensões estão contempladas. Os "
                "indicadores podem ser classificados segundo diferentes critérios, tais como exemplificado a seguir."
            )
        )
        + subheading("Por tema ou dimensão")
        + row(
            p(
                "Os indicadores podem ser classificados conforme a dimensão social da realidade a qual se referem, "
                "e quanto a temas específicos, conforme o arcabouço conceitual ou programático adotado. Podemos ter "
                "indicadores demográficos, socioeconômicos, de infraestrutura, educação, meio ambiente, saúde, entre "
                "outros. Cada tema ou dimensão também pode ser subdividido: a saúde, por exemplo, pode se desdobrar "
                "em aspectos de mortalidade, morbidade e estado funcional. Ressalte-se que um mesmo indicador pode se "
                "enquadrar em mais de uma dimensão."
            )
        )
        + atencao_box(
            "<p>Na saúde pública, não acompanhamos apenas os indicadores produzidos pelo setor saúde ou "
            'classificados como “de saúde”. Os indicadores classificados como <strong>Determinantes Sociais da '
            "Saúde</strong>, por exemplo, ampliam o olhar para além do setor saúde, alinhando-se ao conceito de "
            "saúde como fenômeno social multicausal. Enfatizam dimensões que influenciam diretamente as condições de "
            f"saúde da população, como:</p>{bullet_list(dsd_items)}"
        )
        + subheading("Analíticos ou sintéticos")
        + row(
            p(
                "Os indicadores analíticos (ou primários) concentram-se em uma dimensão específica e geralmente "
                "capturam apenas um fenômeno ou variável. São adequados para diagnósticos mais precisos. Um exemplo "
                "é a taxa de detecção de hanseníase, que representa a ocorrência de novos casos da doença em um "
                "território e permite avaliar diretamente a dinâmica de transmissão e os esforços de vigilância "
                "epidemiológica."
            )
        )
        + row(
            p(
                "Os indicadores sintéticos — também chamados de compostos ou de índices — agregam várias dimensões em "
                "uma medida única, a partir da aglutinação de dois ou mais indicadores analíticos. Eles são úteis para "
                "sintetizar fenômenos complexos, integrando vários aspectos da realidade. Um exemplo é o Índice de "
                "Desenvolvimento Humano (IDH), que mede o grau de desenvolvimento de uma determinada sociedade a partir "
                "da ponderação de indicadores de três áreas: educação, saúde e renda. A construção de índices será "
                "abordada no próximo módulo."
            )
        )
        + subheading("Descritivos ou normativos")
        + row(
            p(
                "Indicadores descritivos expressam características observáveis da realidade com base em critérios "
                "mínimos e consensuais. Um exemplo é a proporção de gestantes com pelo menos seis consultas de "
                "pré-natal, que descreve a cobertura da assistência pré-natal sem envolver juízo de valor explícito. "
                "Indicadores normativos, por outro lado, dependem de critérios conceituais ou juízos de valor explícitos, "
                "como no exemplo anterior da taxa de desocupação, que depende de uma definição metodológica sobre "
                "ocupação econômica."
            )
        )
        + subheading("Objetivos ou subjetivos")
        + row(
            p(
                "Os indicadores objetivos (ou quantitativos) referem-se à ocorrência concreta de algum fenômeno, e são "
                "construídos a partir das estatísticas públicas, a exemplo da taxa de evasão escolar. Os indicadores "
                "subjetivos (ou qualitativos), por sua vez, são construídos a partir da avaliação de indivíduos ou "
                "especialistas sobre aspectos da realidade, como o índice de satisfação com um serviço público."
            )
        )
        + subheading("Diretos ou indiretos")
        + row(
            p(
                "Os indicadores diretos medem exatamente o que se propõem, de maneira objetiva e lógica, a exemplo do "
                "percentual de crianças vacinadas conforme o preconizado para cada faixa etária. Já os indiretos "
                "funcionam como aproximações para conceitos abstratos ou difíceis de mensurar diretamente, e são usados "
                "quando a medição direta não é possível ou é mais custosa. Por exemplo, a proporção de domicílios com "
                "acesso regular a água potável pode ser utilizada como indicador indireto das condições ambientais que "
                "influenciam a saúde, ainda que não esgote o conceito de saneamento ambiental adequado."
            )
        )
        + subheading("Quanto à natureza processual do indicador")
        + row(
            p(
                "Derivados do modelo de Donabedian, amplamente aplicado na avaliação de serviços de saúde, os "
                "indicadores são classificados em três tipos:"
            )
        )
        + list_group(
            [
                "<strong>Indicadores de estrutura ou insumo:</strong> mede recursos disponíveis "
                "(ex.: número de médicos por mil habitantes).",
                "<strong>Indicadores de processo:</strong> avalia como as ações são realizadas "
                "(ex.: número de consultas médicas realizadas por mil habitantes).",
                "<strong>Indicadores de produto ou resultado:</strong> mensura efeitos das ações sobre a saúde "
                "(ex.: proporção das pessoas acompanhadas com controle adequado da pressão arterial).",
            ]
        )
        + row(
            p(
                "Essa classificação permite avaliar não apenas o que o serviço alcança, mas também como e com quais "
                "condições."
            )
        )
        + atencao_box(
            "<p>No monitoramento de programas e políticas públicas, costuma-se adotar a seguinte classificação "
            "(Jannuzzi, 2024):</p><ul>"
            + "".join(f"<li>{item}</li>" for item in jannuzzi_class)
            + "</ul>"
        )
        + subheading("Quanto ao desempenho do programa ou política pública (Eficiência, Eficácia, Efetividade e Equidade)")
        + row(
            p(
                "Cada dimensão analítica responde a uma pergunta distinta sobre o desempenho de programas, políticas "
                "públicas e serviços e traz elementos importantes para os processos avaliativos:"
            )
        )
        + flip_row(
            flipcard(
                "m1a1ef1",
                "Eficiência",
                "<p>Relação entre os meios e recursos utilizados e os resultados alcançados.</p>"
                "<p class=\"mb-0\"><strong>Exemplo:</strong> custo por procedimento ambulatorial realizado.</p>",
            ),
            flipcard(
                "m1a1ef2",
                "Eficácia",
                "<p>Atingimento das metas e objetivos do programa ou política.</p>"
                "<p class=\"mb-0\"><strong>Exemplo:</strong> cobertura vacinal de 95% da população-alvo com "
                "determinado imunobiológico.</p>",
            ),
            flipcard(
                "m1a1ef3",
                "Efetividade",
                "<p>Impacto social sobre a dimensão que se buscou intervir.</p>"
                "<p class=\"mb-0\"><strong>Exemplo:</strong> redução da mortalidade por doenças cardiovasculares após "
                "ampliação de unidades de saúde.</p>",
            ),
            flipcard(
                "m1a1ef4",
                "Equidade",
                "<p>Mede justiça distributiva e acesso.</p>"
                "<p class=\"mb-0\"><strong>Exemplo:</strong> diferença na cobertura vacinal entre grupos de renda.</p>",
            ),
        )
        + box(
            "Leitura Complementar",
            "Leitura Complementar",
            "Para saber mais sobre os assuntos abordados nessa aula e nesse curso, recomendamos a leitura do livro "
            "<strong>Indicadores Sociais no Brasil: Conceitos, Fontes de Dados e Aplicações</strong>, de Paulo de "
            "Martino Jannuzzi.",
        )
    )


def content_topico5() -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{r}</li>' for r in REFERENCES
    )
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5 referencias-aula">'
        f'<div class="heading__block"><span class="small">Tópico 5</span>'
        f'<h3 class="heading__title">Referências</h3></div>'
        f'<div class="list"><ul class="list-group">{lis}</ul></div>'
        f"</div></div>"
    )


CONTENT_BUILDERS = [
    content_topico1,
    content_topico2,
    content_topico3,
    content_topico4,
    content_topico5,
]

ORPHAN_TOPICS = [6, 7, 8]

OLD_COURSE = "Fontes de Dados e Sistemas de Informação para o SUS"
OLD_MOD1 = "Introdução à Informação em Saúde no SUS"


def generate_all() -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        created.append(path)
        print(f"Criado: {path.relative_to(ROOT)}")
    for n in ORPHAN_TOPICS:
        orphan = OUT_DIR / f"topico{n}.html"
        if orphan.exists():
            orphan.unlink()
            print(f"Removido: {orphan.relative_to(ROOT)}")
    return created


def update_modulo1_headers() -> int:
    """Atualiza título do curso e módulo 1 em páginas legadas do módulo 1."""
    count = 0
    for html in (ROOT / "modulo1").rglob("*.html"):
        if html.parent == OUT_DIR:
            continue
        text = html.read_text(encoding="utf-8")
        original = text
        text = text.replace(OLD_COURSE, COURSE_TITLE)
        text = text.replace(OLD_MOD1, MODULE_TITLE)
        text = text.replace(
            "<strong>Aula 1: </strong>Introdução à Informação em Saúde no SUS",
            f"<strong>Aula 1: </strong>{AULA_TITLE}",
        )
        text = text.replace(
            "<strong>Aula 2: </strong>A Política Nacional de Informação e Informática em Saúde (PNIIS)",
            f"<strong>Aula 2: </strong>{AULA2_TITLE}",
        )
        if text != original:
            html.write_text(text, encoding="utf-8")
            count += 1
    print(f"Cabeçalhos atualizados em {count} arquivos do módulo 1")
    return count


MOD4_ITEM_RE = re.compile(
    r'\s*<li class="dropdown-menu__item"><a class="dropdown-menu__item-link"[^>]*href="[^"]*modulo4/aula1/topico1\.html"[^>]*>'
    r"<strong>Módulo 4</strong><br\s*/>[^<]+</a>\s*</li>",
    re.IGNORECASE,
)


def strip_modulo4_from_sidebars() -> int:
    count = 0
    for mod in ("modulo1", "modulo2", "modulo3"):
        for html in (ROOT / mod).rglob("*.html"):
            text = html.read_text(encoding="utf-8")
            new_text, n = MOD4_ITEM_RE.subn("", text)
            if n:
                html.write_text(new_text, encoding="utf-8")
                count += 1
    print(f"Removido Módulo 4 de {count} sidebars")
    return count


def main() -> None:
    print("=== Gerando modulo1/aula1 ===")
    files = generate_all()
    print("\n=== Atualizando cabeçalhos legados do módulo 1 ===")
    update_modulo1_headers()
    print("\n=== Removendo Módulo 4 de sidebars (mod1–3) ===")
    strip_modulo4_from_sidebars()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()
