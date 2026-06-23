#!/usr/bin/env python3
"""Gera HTML da Aula 1.2 (Módulo 1) — Atributos desejáveis e seleção de indicadores."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo1" / "aula2"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 1
MODULE_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Atributos desejáveis e seleção de indicadores"
AULA1_TITLE = "O que são indicadores?"

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("O que são atributos desejáveis dos indicadores?", "O que são atributos desejáveis dos indicadores?"),
    ("Quais são os atributos desejáveis dos indicadores?", "Quais são os atributos desejáveis dos indicadores?"),
    ("Critérios de seleção de indicadores", "Critérios de seleção de indicadores"),
    ("Referências", "Referências"),
]

OBJECTIVES = [
    "Conhecer os atributos desejáveis dos indicadores.",
    "Distinguir entre as características dos indicadores.",
    "Selecionar indicadores considerando seus atributos.",
]

AUTHORS = [
    (
        "Carolina de Campos Carvalho",
        "Doutora e Mestre em Saúde Pública, Analista Técnica de Políticas Sociais. Instituto de "
        "Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da Fundação "
        "Oswaldo Cruz (Fiocruz).",
    ),
    (
        "Aline Pinto Marques",
        "Doutora em Epidemiologia em Saúde Pública. Instituto de Comunicação e Informação "
        "Científica e Tecnológica em Saúde (Icict) da Fundação Oswaldo Cruz (Fiocruz).",
    ),
]

JANNUZZI_ATTRIBUTES: list[tuple[str, str]] = [
    (
        "Relevância",
        "O indicador deve responder a prioridades sociais e/ou de saúde e ser significativo e útil "
        "para os usuários e tomadores de decisão. Jannuzzi (2009) utiliza o termo “relevância social”, "
        "que diz respeito à pertinência de produção e uso do indicador.",
    ),
    (
        "Validade",
        "Diz respeito à capacidade do indicador de medir aquilo que ele se propõe a medir; é o grau "
        "de proximidade entre o conceito e a medida.",
    ),
    (
        "Confiabilidade",
        "Refere-se à qualidade do levantamento dos dados utilizados no cálculo do indicador. Refere-se "
        "à fonte de informação utilizada; fontes confiáveis devem utilizar métodos de coleta e "
        "processamento de dados válidos e sistemáticos para garantir, assim, sua qualidade.",
    ),
    (
        "Mensurabilidade",
        "Diz respeito à existência de uma forma de atribuir valor ao indicador, à capacidade de ser "
        "quantificável por dados disponíveis.",
    ),
    (
        "Boa cobertura",
        "Os dados devem ter uma cobertura espacial e populacional adequada, representando, assim, "
        "toda a realidade empírica em análise.",
    ),
    (
        "Sensibilidade",
        "Capacidade do indicador de detectar mudanças ou variações no fenômeno ou dimensão social "
        "que está sendo medida.",
    ),
    (
        "Especificidade",
        "O indicador deve detectar mudanças apenas no fenômeno ou dimensão social que está sendo "
        "medida, diferenciando-o de outros fenômenos e dimensões.",
    ),
    (
        "Reprodutibilidade",
        "Os resultados devem ser iguais quando são obtidos por pessoas diferentes ou em diferentes "
        "contextos, usando o mesmo método.",
    ),
    (
        "Comunicabilidade/compreensibilidade",
        "O indicador deve ter transparência, ser compreensível pelos usuários e ser comunicado "
        "com clareza.",
    ),
    (
        "Periodicidade",
        "Os dados devem ter regularidade no levantamento e atualização, com custo e esforço compatíveis.",
    ),
    (
        "Desagregabilidade",
        "Refere-se à possibilidade de o indicador ser analisado e apresentado de forma detalhada e "
        "segmentada em partes menores ou específicas, como por faixa etária, sexo, raça/cor, "
        "escolaridade, perfil socioeconômico, entre outras categorias de análise relevantes.",
    ),
    (
        "Historicidade/comparabilidade temporal",
        "Diz respeito à possibilidade de séries históricas extensas e comparáveis, para que seja "
        "possível comparar períodos no tempo e avaliar efeitos de programas e políticas.",
    ),
]

EXTRA_ATTRIBUTES: list[tuple[str, str]] = [
    (
        "Inteligibilidade",
        "Deve haver transparência na metodologia de construção do indicador. Relaciona-se também "
        "com a comunicabilidade/ compreensibilidade.",
    ),
    (
        "Oportunidade/tempestividade",
        "Diz respeito à capacidade de coleta e notificação dos dados em tempo hábil. Está relacionada "
        "com a periodicidade.",
    ),
    (
        "Custo-efetividade/economicidade",
        "Os resultados devem justificar o investimento de tempo e recursos. O custo para obtenção do "
        "indicador não deve ser maior que o benefício gerado pela sua utilização.",
    ),
    (
        "Sustentabilidade",
        "Diz respeito à existência de condições necessárias para a estimativa contínua.",
    ),
    (
        "Viabilidade",
        "O indicador deve basear-se em dados disponíveis ou possíveis de conseguir. Esse aspecto "
        "relaciona-se com a mensurabilidade.",
    ),
]

REFERENCES = [
    (
        "BRASIL. Ministério do Planejamento, Desenvolvimento e Gestão. Secretaria de Planejamento e "
        "Assuntos Econômicos. <strong>Indicadores: orientações básicas aplicadas à gestão pública</strong>. "
        "3. ed. Brasília, DF: MP, 2018. 36 p. il. color. Disponível em: "
        '<a href="https://www.gov.br/gestao/pt-br/acesso-a-informacao/estrategia-e-governanca/'
        'planejamento_estrategico_arquivos/livros_guias_publicacoes/guia-metodologico-para-indicadores-mp-2018.pdf" '
        'target="_blank" rel="noopener noreferrer">guia-metodologico-para-indicadores-mp-2018.pdf</a>. '
        "Acesso em: 16 fev. 2026."
    ),
    (
        "COBO, B.; ATHIAS, L. Produção de dados desagregados para “não deixar ninguém para trás”. In: "
        "KRONEMBERGER, D.; ATHIAS, L.; COBO, B. (org.). <strong>Reflexões sobre a Agenda 2030: 10 anos "
        "dos Objetivos de Desenvolvimento Sustentável</strong>. Rio de Janeiro: IBGE, 2025. p. 99–113. "
        "(Estudos e análises: informação demográfica e socioeconômica, n. 10). ISBN 978-85-240-4670-4. "
        "Disponível em: "
        '<a href="https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=2102207" '
        'target="_blank" rel="noopener noreferrer">https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo'
        "?view=detalhes&amp;id=2102207</a>. Acesso em: 16 fev. 2026."
    ),
    "JANNUZZI, P. de M. <strong>Indicadores sociais no Brasil</strong>. 6. ed. Campinas: Alínea, 2017. 3. impr. 2024.",
    (
        "ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE (OPAS). <strong>Indicadores de saúde: elementos conceituais e "
        "práticos</strong>. Washington, DC: OPAS, 2018. Disponível em: "
        '<a href="https://iris.paho.org/bitstream/handle/10665.2/49057/9789275720059_por.pdf" '
        'target="_blank" rel="noopener noreferrer">https://iris.paho.org/bitstream/handle/10665.2/49057/'
        "9789275720059_por.pdf</a>. Acesso em: 16 fev. 2026."
    ),
    (
        "REDE INTERAGENCIAL DE INFORMAÇÃO PARA A SAÚDE (RIPSA). <strong>Indicadores básicos para a saúde no "
        "Brasil: conceitos e aplicações</strong>. Brasília, DF: Organização Pan-Americana da Saúde, 2008. "
        "349 p. Disponível em: "
        '<a href="https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/" '
        'target="_blank" rel="noopener noreferrer">https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/</a>. '
        "Acesso em: 16 fev. 2026."
    ),
    (
        "RUA, M. G. <strong>Desmistificando o problema: uma rápida introdução ao estudo dos indicadores</strong>. "
        "Brasília, DF: Escola Nacional de Administração Pública (ENAP), 2004."
    ),
]

COBO_ATHIAS_URL = (
    "https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=2102207"
)

INDICATOR_1_LABEL = (
    "Indicador 1: Prevalência de diabetes mellitus autorreferida em indivíduos com 18 anos "
    "ou mais de idade. Fonte: Pesquisa Nacional de Saúde (PNS)."
)
INDICATOR_2_LABEL = (
    "Indicador 2: Taxa de internação por diabetes mellitus por 100 mil habitantes de 18 anos "
    "ou mais de idade. Fonte: Sistema de Informações Hospitalares (SIH-SUS)."
)


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


def list_group(items: list[str]) -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{item}</li>' for item in items
    )
    return row(f'<div class="list"><ul class="list-group">{lis}</ul></div>')


def bullet_list(items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return row(f"<ul>{lis}</ul>")


def voce_sabia_box(body_html: str) -> str:
    return box_html("Você sabia?", "Você sabia?", body_html)


def figure_image(src: str, alt: str, fonte: str = "") -> str:
    fonte_html = (
        f'<p class="figure-caption fonte text-center small mt-2 mb-0">{fonte}</p>' if fonte else ""
    )
    return row(
        f'<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
        f'data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded" src="{src}" alt="{alt}" loading="lazy" />'
        f"</figure>{fonte_html}"
    )


def flipcard(card_id: str, title: str, back_html: str, *, col: str = "col-12 col-md-6") -> str:
    back = f'<p class="mb-0">{back_html}</p>' if not back_html.startswith("<") else back_html
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
        f'<div class="scrollable text-start">{back}</div></div>'
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


def accordion(accordion_id: str, items: list[tuple[str, str]]) -> str:
    parts = [f'<div class="accordion accordion-flush" id="{accordion_id}">']
    for i, (title, body) in enumerate(items):
        hid = f"{accordion_id}-{i}-h"
        cid = f"{accordion_id}-{i}-c"
        parts.append(
            f'<div class="accordion-item"><h5 class="accordion-header" id="{hid}">'
            f'<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" '
            f'data-bs-target="#{cid}" aria-expanded="false" aria-controls="{cid}">{title}</button></h5>'
            f'<div id="{cid}" class="accordion-collapse collapse" aria-labelledby="{hid}" '
            f'data-bs-parent="#{accordion_id}"><div class="accordion-body">{body}</div></div></div>'
        )
    parts.append("</div>")
    return row("".join(parts))


def extra_attributes_flipcards() -> str:
    attrs = dict(EXTRA_ATTRIBUTES)
    return (
        flip_row(
            flipcard("m1a2e1", "Viabilidade", attrs["Viabilidade"]),
            flipcard("m1a2e2", "Sustentabilidade", attrs["Sustentabilidade"]),
        )
        + flip_row(
            flipcard("m1a2e3", "Oportunidade/ tempestividade", attrs["Oportunidade/tempestividade"]),
            flipcard("m1a2e4", "Inteligibilidade", attrs["Inteligibilidade"]),
        )
        + flip_row(
            flipcard(
                "m1a2e5",
                "Custo-efetividade/ economicidade",
                attrs["Custo-efetividade/economicidade"],
            ),
        )
    )


def matrix_quadro1() -> str:
    return row(
        '<p class="mb-2"><strong>Quadro 1: Matriz de seleção de indicadores segundo atributos e ponderações.</strong></p>'
        '<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
        'data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded" src="{ASSETS}media/modulo1/aula2-topico4-quadro1-matriz.png" '
        'alt="Quadro 1 — matriz de seleção de indicadores segundo atributos e ponderações, com colunas '
        'para número, indicador, cinco atributos e nota de priorização." loading="lazy" />'
        "</figure>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaboração própria, a partir de Brasil, 2018.</p>'
    )


def matrix_quadro2() -> str:
    return row(
        '<p class="mb-2"><strong>Quadro 2: Matriz de seleção de indicadores segundo atributos e ponderações '
        "(escala de 0 a 5; nota máxima: 25).</strong></p>"
        '<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
        'data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded" src="{ASSETS}media/modulo1/aula2-topico4-quadro2-matriz.png" '
        'alt="Quadro 2 — matriz de seleção de indicadores preenchida com as pontuações dos indicadores de '
        'prevalência de diabetes (PNS) e taxa de internação por diabetes (SIH-SUS)." loading="lazy" />'
        "</figure>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaboração própria, a partir de Brasil, 2018.</p>'
    )


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
            '<a class="fio-button fio-button-primary" href="../../modulo2/aula1/topico1.html" rel="next">'
            'Módulo 2 <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
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
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA1_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>{AULA_TITLE}</a></li>
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
        + row(p("Seja bem-vindo e bem-vinda!"))
        + row(
            p(
                "Nesta aula, continuaremos o estudo sobre os conceitos fundamentais relacionados a "
                "indicadores, e serão apresentadas as características desejáveis de indicadores sociais "
                "e de saúde e orientações para seleção de indicadores."
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
    return (
        heading(2, TOPICS[1][1])
        + row(
            p(
                "Quando selecionamos um indicador, devemos considerar alguns critérios que garantam que "
                "ele realmente traduza, de forma objetiva, o conceito que desejamos representar. Para isso, "
                "é importante refletir sobre questões como: qual indicador melhor se aproxima do fenômeno "
                "que pretendo analisar? Quais dados, de fato, captam melhor a realidade que quero observar? "
                "Que tipo de indicador será mais útil para o propósito definido?"
            )
        )
        + figure_image(
            f"{ASSETS}media/modulo1/aula2-topico2-selecao-indicadores.png",
            "Profissional analisando informações em um laptop em ambiente de escritório.",
            "Fonte: Freepik",
        )
        + row(
            p(
                "Essas e outras perguntas ajudam a orientar a escolha de um indicador robusto e de qualidade. "
                "A qualidade de um indicador pode ser influenciada pelas características dos componentes "
                "utilizados em sua elaboração, como a frequência de ocorrência dos casos e o tamanho da "
                "população, além da precisão dos sistemas de informação utilizados para registro, coleta e "
                "transmissão dos dados."
            )
        )
        + row(
            p(
                "Para que os indicadores sejam úteis e adequados ao monitoramento e avaliação de programas "
                "e políticas de saúde e para a análise da condição de saúde da população, é desejável que eles "
                "apresentem algumas características técnicas e operacionais, que chamamos também de "
                "atributos ou propriedades desejáveis (Jannuzzi, 2024; OPAS, 2018; Ripsa, 2008)."
            )
        )
    )


def content_topico3() -> str:
    return (
        heading(3, TOPICS[2][1])
        + row(
            p(
                "Existem diferentes definições sobre atributos de um bom indicador. Jannuzzi (2024) "
                "contabiliza 12 propriedades desejáveis dos indicadores sociais. São elas:"
            )
        )
        + accordion(
            "m1a2j-attrs",
            [
                (f"{title}:", f'<p class="mb-0">{text}</p>')
                for title, text in JANNUZZI_ATTRIBUTES
            ],
        )
        + row(
            p(
                "Outras abordagens e autores (Rua, 2004; OPAS, 2008) trazem também como características "
                "desejáveis:"
            )
        )
        + extra_attributes_flipcards()
    )


def content_topico4() -> str:
    ind1_eval = (
        "<p>No atributo relevância, o indicador foi pontuado como altamente relevante, uma vez que "
        "para a distribuição de medicamentos é necessário estimar a prevalência de pessoas com "
        "diabetes. Assim, atribuímos o peso 5.</p>"
        "<p>Quanto à validade, o indicador é adequado, pois quantifica a proporção da população "
        "que vive com diabetes, ou seja, a medida corresponde diretamente ao conceito que se "
        "pretende avaliar. Dessa forma, também atribuímos o peso 5.</p>"
        "<p>Em relação à confiabilidade, consideramos peso 4, já que a base utilizada para o cálculo "
        "é o inquérito domiciliar da PNS, uma pesquisa de abrangência nacional conduzida pelo "
        "IBGE. Contudo, entre as limitações do indicador está ser uma informação autorreferida, "
        "sujeita a um viés de memória.</p>"
        "<p>Quanto à periodicidade, os dados da PNS são coletados a cada seis anos, o que pode "
        "representar um intervalo longo para o monitoramento, por exemplo, da efetividade de "
        "programas ou políticas. Por esse motivo, atribuímos o peso 2 a esse atributo.</p>"
        "<p class=\"mb-0\">Por fim, a viabilidade de cálculo do indicador é baixa tratando-se de um município que "
        "não seja capital, como no nosso exemplo, embora os dados para outras abrangências "
        "sejam públicos e amplamente disponibilizados para uso. A pontuação, portanto, irá "
        "diferir de acordo com o objetivo de uso do indicador.</p>"
    )
    ind2_eval = (
        "<p>O indicador é relevante para realizar um diagnóstico direcionado à dispensação de "
        "medicamentos para diabetes. Assim, atribuímos o peso 5.</p>"
        "<p>Quanto à validade, o indicador recebeu nota 4, pois quantifica apenas as internações "
        "realizadas no Sistema Único de Saúde, não quantificando toda a população que poderá ser "
        "potencialmente abrangida pelo programa em questão.</p>"
        "<p>Em relação à confiabilidade, consideramos peso 5, já que a fonte de dados utilizada "
        "para o cálculo é o Sistema de Informações Hospitalares do SUS, base de dados oficial de "
        "registro de todas as internações.</p>"
        "<p class=\"mb-0\">Quanto à periodicidade e à viabilidade de cálculo, foi dada a nota máxima, pois o SIH é "
        "atualizado mensalmente e os dados são públicos.</p>"
    )
    voce_sabia = (
        "<p>No capítulo “Produção de dados desagregados para ‘não deixar ninguém para trás’”, "
        "Barbara Cobo e Leonardo Athias apresentam a desagregação de dados como uma ferramenta "
        "essencial para combater a invisibilidade estatística e garantir que as políticas públicas "
        "alcancem, de fato, todos os territórios e pessoas.</p>"
        f'<p class="mb-0">Leia o <a href="{COBO_ATHIAS_URL}" target="_blank" rel="noopener noreferrer">texto</a> '
        "e reflita sobre a importância do atributo desagregabilidade para a construção de indicadores de "
        "monitoramento e avaliação dos programas e políticas sociais.</p>"
    )
    return (
        heading(4, TOPICS[3][1])
        + row(
            p(
                "Na prática, nem sempre o indicador possível de ser calculado reúne todos os atributos "
                "desejáveis, especialmente em função das fontes de dados disponíveis e da periodicidade "
                "desejada."
            )
        )
        + row(
            p(
                "Tanto na pesquisa acadêmica quanto na gestão, algumas ferramentas podem ser úteis para "
                "padronizar a seleção e priorização de indicadores. No quadro a seguir, temos um exemplo."
            )
        )
        + row(
            p(
                "Partindo-se dos objetivos de um programa, de uma política, ou de um estudo avaliativo, "
                "por exemplo, deve-se selecionar indicadores factíveis, e então validá-los preliminarmente "
                "com as partes interessadas. Nessa etapa, podem ser convidados membros da equipe e "
                "pessoas especialistas no tema para avaliar a aderência de cada indicador aos atributos "
                "desejáveis. Podem também ser atribuídos pesos diferentes a cada um dos atributos, a depender "
                "dos objetivos de uso do indicador."
            )
        )
        + matrix_quadro1()
        + row(
            p(
                "Imagine que a gestão de um município de 100 mil habitantes precise selecionar indicadores "
                "de monitoramento para a implementação de um novo programa de dispensação de medicamentos "
                "para pessoas com diabetes. A equipe se reúne e entre os indicadores listados previamente "
                "estão os dois abaixo:"
            )
        )
        + bullet_list([INDICATOR_1_LABEL, INDICATOR_2_LABEL])
        + row(p("Agora vejamos quanto aos critérios de avaliação:"))
        + accordion(
            "m1a2-ind-eval",
            [
                (INDICATOR_1_LABEL, ind1_eval),
                (INDICATOR_2_LABEL, ind2_eval),
            ],
        )
        + matrix_quadro2()
        + row(
            p(
                "O primeiro indicador é altamente relevante para o planejamento, por ser uma medida "
                "aproximada da prevalência de pessoas com diabetes, público-alvo do programa. Contudo, "
                "esse não é um indicador desagregável para todos os municípios brasileiros, pois tem como "
                "fonte a PNS, realizada a cada seis anos, o que restringe seu uso para o monitoramento "
                "contínuo de programas."
            )
        )
        + row(
            p(
                "O indicador 2 é um indicador usualmente utilizado como medida de efetividade da "
                "Atenção Primária à Saúde, pois a diabetes é uma condição sensível à APS. O SIH-SUS "
                "tem uma atualização e disponibilização de dados mensal, com dados desagregáveis por "
                "municípios e até mesmo unidades de atenção hospitalar, o que é positivo para a elaboração "
                "de indicadores que exigem um monitoramento contínuo em tempo oportuno."
            )
        )
        + row(
            p(
                "A partir desse exemplo, compreendemos que a seleção de um indicador irá depender "
                "dos objetivos e do contexto de uso."
            )
        )
        + voce_sabia_box(voce_sabia)
        + row(
            p(
                "Por fim, é importante reconhecermos as limitações do indicador construído, e revisitar os "
                "atributos com o tempo para tentar aperfeiçoá-lo na medida em que as fontes de dados "
                "também são atualizadas e aprimoradas. Portanto, o não atendimento a um dos atributos "
                "não deve significar a exclusão do indicador, e é possível reparar fragilidades identificadas "
                "com o uso de indicadores complementares."
            )
        )
        + row(
            p(
                "Pense cada indicador como parte de um kit de ferramentas. Cada uma tem uma função "
                "e uso específico, e podem ser complementares."
            )
        )
        + figure_image(
            f"{ASSETS}media/modulo1/aula2-topico4-kit-ferramentas.png",
            "Conjunto de ferramentas dispostas em círculo, representando o kit de indicadores complementares.",
            "Fonte: Freepik",
        )
        + row(
            p("No próximo módulo, abordaremos o processo de construção dos indicadores."),
            "mb-5",
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
OLD_AULA2 = "A Política Nacional de Informação e Informática em Saúde (PNIIS)"


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
    skip_dirs = {ROOT / "modulo1" / "aula1", OUT_DIR}
    count = 0
    for html in (ROOT / "modulo1").rglob("*.html"):
        if html.parent in skip_dirs:
            continue
        text = html.read_text(encoding="utf-8")
        original = text
        text = text.replace(OLD_COURSE, COURSE_TITLE)
        text = text.replace(OLD_MOD1, MODULE_TITLE)
        text = text.replace(
            "<strong>Aula 1: </strong>Introdução à Informação em Saúde no SUS",
            f"<strong>Aula 1: </strong>{AULA1_TITLE}",
        )
        text = text.replace(
            f"<strong>Aula 2: </strong>{OLD_AULA2}",
            f"<strong>Aula 2: </strong>{AULA_TITLE}",
        )
        if text != original:
            html.write_text(text, encoding="utf-8")
            count += 1
    print(f"Cabeçalhos atualizados em {count} arquivos do módulo 1")
    return count


def main() -> None:
    print("=== Gerando modulo1/aula2 ===")
    files = generate_all()
    print("\n=== Atualizando cabeçalhos legados do módulo 1 ===")
    update_modulo1_headers()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()
