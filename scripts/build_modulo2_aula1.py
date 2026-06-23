#!/usr/bin/env python3
"""Gera HTML da Aula 2.1 (Módulo 2) — Dados, medidas e indicadores: valores absolutos e relativos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula1"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 2
MODULE_TITLE = "Calculando indicadores"
MODULE1_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA_LABEL = "Aula 1"
AULA_TITLE = "Dados, medidas e indicadores: valores absolutos e relativos"
AULA2_TITLE = "Medidas relativas para a análise de dados de saúde"
AULA3_TITLE = "Índices: conceitos, construção e usos"
AULA4_TITLE = "Ficha de Qualificação de Indicadores"

FIGURA_CONCEITOS_URL = ""
FIGURA_DADOS_SAUDE_URL = f"{ASSETS}media/modulo2/aula1-topico2-dados-saude.png"

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("Dados, informação e indicadores em saúde", "Dados, informação e indicadores em saúde"),
    (
        "Valores absolutos e relativos: conceitos fundamentais",
        "Valores absolutos e relativos: conceitos fundamentais",
    ),
    ("Valores absolutos", "Valores absolutos"),
    ("Valores relativos", "Valores relativos"),
    ("Referências", "Referências"),
]

OBJECTIVES = [
    "Identificar valores absolutos e valores relativos;",
    "Reconhecer as diferenças entre essas medidas;",
    "Identificar suas principais aplicações;",
    "Interpretar adequadamente indicadores construídos a partir dessas medidas;",
    "Reconhecer limitações e potenciais vieses analíticos.",
]

AUTHORS = [
    (
        "Wanessa da Silva de Almeida",
        "Doutora em Epidemiologia. Analista de Informação e Comunicação do Laboratório de "
        "Informação em Saúde do Instituto de Comunicação e Informação Científica e Tecnológica "
        "em Saúde da Fundação Oswaldo Cruz (LIS/ICICT/Fiocruz).",
    ),
]

REFERENCES = [
    "BUSSAB, W. O.; MORETTIN, P. A. <strong>Estatística básica</strong>. São Paulo: Saraiva, 2017.",
    (
        "MEDRONHO, R. A. et al. <strong>Epidemiologia</strong>. 2. ed. São Paulo: Atheneu, 2009."
    ),
    (
        "TRIOLA, M. F. <strong>Introdução à estatística</strong>. 13. ed. Rio de Janeiro: LTC, 2019."
    ),
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


def list_group(items: list[str]) -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{item}</li>' for item in items
    )
    return row(f'<div class="list"><ul class="list-group">{lis}</ul></div>')


def bullet_list(items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return row(f"<ul>{lis}</ul>")


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


def tabela1_nascimentos() -> str:
    rows = [
        ("Região Norte", "301.635", "309.362", "289.158", "284.197", "265.670"),
        ("Região Nordeste", "770.688", "766.074", "708.975", "703.448", "667.121"),
        ("Região Sudeste", "1.052.399", "1.009.734", "979.681", "966.160", "904.365"),
        ("Região Sul", "374.949", "362.921", "359.781", "357.612", "336.802"),
        ("Região Centro-Oeste", "230.474", "229.010", "224.327", "226.159", "215.367"),
        ("Brasil", "2.730.145", "2.677.101", "2.561.922", "2.537.576", "2.389.325"),
    ]
    body = "".join(
        "<tr>"
        + "".join(
            f"<td>{cell}</td>"
            if i == 0
            else f'<td class="text-end bg-primary text-white">{cell}</td>'
            if i == len(r) - 1
            else f'<td class="text-end">{cell}</td>'
            for i, cell in enumerate(r)
        )
        + "</tr>"
        for r in rows
    )
    return row(
        '<p class="mb-2"><strong>Tabela 1: Nascimentos por ano segundo região. Brasil, 2020 a 2024.</strong></p>'
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Região</th>'
        '<th scope="col" class="text-end">2020</th>'
        '<th scope="col" class="text-end">2021</th>'
        '<th scope="col" class="text-end">2022</th>'
        '<th scope="col" class="text-end">2023</th>'
        '<th scope="col" class="text-end">2024</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">'
        "Fonte: MS/SVSA/CGIAE - Sistema de Informações sobre Nascidos Vivos – SINASC.</p>"
    )


def tabela2_obitos() -> str:
    rows: list[tuple[str, str, str, str]] = [
        ("Região Norte", "14.287", "96.349", "14.287 ÷ 96.349 × 100 = 14,8"),
        ("Região Nordeste", "50.488", "394.906", "12,8"),
        ("Região Sudeste", "58.042", "691.582", "8,4"),
        ("Região Sul", "23.139", "242.826", "9,5"),
        ("Região Centro-Oeste", "13.578", "106.352", "12,8"),
        ("Brasil", "159.534", "1.532.015", "10,4"),
    ]
    body_parts = []
    for r in rows:
        is_brasil = r[0] == "Brasil"
        cells = []
        for i, cell in enumerate(r):
            if i == 0:
                value = f"<strong>{cell}</strong>" if is_brasil else cell
                cells.append(f"<td>{value}</td>")
            else:
                value = f"<strong>{cell}</strong>" if is_brasil else cell
                cells.append(f'<td class="text-end">{value}</td>')
        body_parts.append("<tr>" + "".join(cells) + "</tr>")
    body = "".join(body_parts)
    return row(
        '<p class="mb-2"><strong>Tabela 2: Total de óbitos, óbitos por causas externas e mortalidade '
        "proporcional por causas externas (valor relativo) segundo região. Brasil, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Região</th>'
        '<th scope="col" class="text-end">Óbitos por<br />causas externas</th>'
        '<th scope="col" class="text-end">Total<br />de óbitos</th>'
        '<th scope="col" class="text-end">Mortalidade<br />proporcional por<br />causas externas (%)</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">'
        "Fonte: MS/SVSA/CGIAE - Sistema de Informações sobre Mortalidade – SIM.</p>"
    )


def quadro_comparativo1() -> str:
    aspect = lambda text: f'<th scope="row">{text}</th>'
    quando_abs = (
        "<ul class='mb-0 ps-3'>"
        "<li>Dimensionar demanda por serviços;</li>"
        "<li>Planejar recursos humanos e materiais;</li>"
        "<li>Monitorar volume de procedimentos;</li>"
        "<li>Avaliar carga total de doenças;</li>"
        "<li>Apoiar a gestão operacional.</li>"
        "</ul>"
    )
    quando_rel = (
        "<ul class='mb-0 ps-3'>"
        "<li>Comparar municípios, estados ou países;</li>"
        "<li>Comparar populações de tamanhos diferentes;</li>"
        "<li>Medir risco;</li>"
        "<li>Identificar desigualdades em saúde;</li>"
        "<li>Avaliar políticas públicas.</li>"
        "</ul>"
    )
    return row(
        "<p class='mb-2'><strong>Quadro comparativo 1: Quando usar valores absolutos e quando usar "
        "valores relativos.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Aspecto</th>'
        '<th scope="col">Valores absolutos</th>'
        '<th scope="col">Valores relativos</th>'
        "</tr></thead><tbody>"
        f"<tr>{aspect('Finalidade principal')}"
        "<td>Dimensionar a magnitude total de eventos e a carga operacional dos serviços</td>"
        "<td>Avaliar frequência, risco e intensidade dos eventos na população</td></tr>"
        f"<tr>{aspect('Pergunta central')}<td>Quantos aconteceram?</td>"
        "<td>Quantos em relação a quê?</td></tr>"
        f"<tr>{aspect('Quando utilizar')}<td>{quando_abs}</td><td>{quando_rel}</td></tr>"
        f"<tr>{aspect('Tipo de análise favorecida')}"
        "<td>Planejamento logístico e organização dos serviços</td>"
        "<td>Epidemiologia, vigilância em saúde e análise comparativa</td></tr>"
        f"<tr>{aspect('Exemplos de perguntas')}"
        "<td>“Quantas consultas foram realizadas?”</td>"
        "<td>“Qual população tem maior risco de óbito materno?”</td></tr>"
        f"<tr>{aspect('Principal limitação')}"
        "<td>“Quantas gestantes precisam ser acompanhadas?”</td>"
        "<td>“Em qual região a incidência é mais elevada?”</td></tr>"
        f"<tr>{aspect('Papel na prática em saúde')}"
        "<td>Não considera o tamanho da população, dificultando comparações</td>"
        "<td>Pode mascarar o volume real de eventos quando analisado isoladamente</td></tr>"
        "</tbody></table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelo autor.</p>'
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
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />{MODULE1_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />{MODULE_TITLE}</a></li>
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
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula3/topico1.html"><strong>Aula 3: </strong>{AULA3_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula4/topico1.html"><strong>Aula 4: </strong>{AULA4_TITLE}</a></li>
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
        + row(
            p(
                f'Seja bem-vindo e bem-vinda à aula “<strong>{AULA_TITLE}</strong>”.'
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
                "Na área da saúde, decisões clínicas, gerenciais e de políticas públicas são fortemente "
                "fundamentadas em dados. Informações provenientes de registros clínicos, sistemas de "
                "informação em saúde, inquéritos populacionais e bases administrativas subsidiam desde o "
                "planejamento local de serviços até a formulação de políticas públicas em nível nacional."
            )
        )
        + figure_image(
            FIGURA_DADOS_SAUDE_URL,
            "Estetoscópio sobre tablet com gráficos e ícones de saúde, representando o uso de dados "
            "em decisões clínicas e de políticas públicas.",
            "Fonte: Freepik",
        )
        + row(
            p(
                "A produção e a análise de dados constituem pilares centrais dos sistemas de saúde "
                "contemporâneos. Nesse contexto, compreender como diferentes formas de medida traduzem "
                "fenômenos em saúde é condição essencial para interpretar corretamente informações, "
                "comparar realidades distintas e apoiar processos decisórios baseados em evidências."
            )
        )
        + row(
            p(
                "Dados isolados raramente possuem significado analítico imediato. Para que se transformem "
                "em informação útil, precisam ser organizados, sistematizados e expressos por meio de "
                "medidas adequadas. Entre as formas mais elementares e, ao mesmo tempo, mais "
                "frequentemente mal interpretadas, estão os valores absolutos e os valores relativos."
            )
        )
        + row(
            p(
                "Esta aula tem como objetivo apresentar os conceitos fundamentais de valores absolutos e "
                "valores relativos, abordando suas definições, formas de cálculo e aplicações práticas na saúde "
                "coletiva, na vigilância epidemiológica e na gestão de serviços. Antes de aprofundar os conceitos "
                "centrais, é importante situá-los no campo mais amplo da análise de dados em saúde."
            )
        )
        + row(
            p(
                "<strong>Dados</strong> correspondem a registros brutos de eventos ou características, como idade, sexo, "
                "diagnóstico ou local de residência. Quando esses dados são organizados e sintetizados, "
                "passam a compor informações. A partir dessas informações, constroem-se indicadores, "
                "que permitem monitorar situações de saúde, avaliar serviços e apoiar processos decisórios."
            )
        )
        + row(
            p(
                "<strong>Indicadores</strong> são medidas sintéticas sobre aspectos específicos da realidade, utilizadas para "
                "descrever, monitorar, comparar e avaliar fenômenos de interesse, especialmente na saúde "
                "pública, epidemiologia, planejamento e gestão. Eles transformam dados brutos em "
                "informações úteis para análise de situação, avaliação de políticas, monitoramento de "
                "tendências e tomada de decisão baseada em evidências."
            )
        )
        + row(p("Os indicadores podem assumir diferentes formatos, dependendo:"))
        + list_group(
            [
                "Do tipo de evento observado;",
                "Da população de referência;",
                "Do objetivo da análise (descrição, comparação, avaliação temporal ou espacial).",
            ]
        )
        + row(
            p(
                "Sua elaboração envolve decisões metodológicas que condicionam diretamente sua "
                "interpretabilidade, comparabilidade e validade analítica."
            )
        )
        + row(
            p(
                "Entre os formatos mais utilizados estão valores absolutos e valores relativos, em forma de "
                "proporções, razões, taxas e índices. Em epidemiologia, destacam-se ainda medidas relativas "
                "específicas como incidência e prevalência."
            )
        )
        + row(p("De modo geral, os indicadores de saúde podem ser expressos como:"))
        + list_group(
            [
                "Valores absolutos;",
                "Medidas relativas (proporções, razões e taxas).",
            ]
        )
        + row(
            p(
                "Cada formato possui finalidades específicas, vantagens e limitações, exigindo compreensão "
                "conceitual para sua aplicação adequada."
            )
        )
    )


def content_topico3() -> str:
    figura = ""
    if FIGURA_CONCEITOS_URL:
        figura = figure_image(
            FIGURA_CONCEITOS_URL,
            "Ilustração sobre dados e indicadores em saúde",
            "Fonte: Freepik",
        )
    return (
        heading(3, TOPICS[2][1])
        + row(
            p(
                "Valores absolutos correspondem à contagem direta de eventos. Exemplos incluem o "
                "número de casos de uma doença, o total de internações ou a quantidade de óbitos "
                "registrados em determinado período ou local."
            )
        )
        + row(
            p(
                "Já os valores relativos relacionam esses eventos a uma população de referência, "
                "permitindo expressar frequência, intensidade ou risco. São obtidos por meio da divisão "
                "do número de eventos pelo tamanho da população exposta, frequentemente multiplicados "
                "por uma constante (como 1.000 ou 100.000)."
            )
        )
        + row(
            p(
                "Apesar de aparentemente simples, a distinção entre essas duas medidas é fundamental "
                "para a interpretação correta de fenômenos em saúde, especialmente quando se busca "
                "comparar territórios, grupos populacionais ou períodos distintos."
            )
        )
        + row(
            p(
                "Valores absolutos informam sobre a magnitude do problema. Valores relativos permitem "
                "avaliar sua intensidade."
            )
        )
        + subheading("Mas por que falar de valores absolutos e relativos?", tag="h5")
        + row(
            p(
                "Na prática profissional, é comum encontrar informações como:"
            )
        )
        + list_group(
            [
                "“Foram registrados 1.200 casos de dengue.”",
                "“A taxa de incidência foi de 350 casos por 100 mil habitantes.”",
            ]
        )
        + row(p("Ambas são informações válidas, mas transmitem mensagens diferentes."))
        + row(
            p(
                "O primeiro exemplo apresenta um valor absoluto: o número total de eventos observados. "
                "O segundo expressa um valor relativo, pois relaciona o número de casos ao tamanho "
                "da população."
            )
        )
        + row(p("Compreender essa diferença é essencial para:"))
        + list_group(
            [
                "Comparar regiões com populações distintas;",
                "Avaliar tendências temporais;",
                "Planejar recursos;",
                "Priorizar ações de saúde.",
            ]
        )
        + row(
            p(
                "Valores absolutos e relativos são componentes estruturantes de praticamente todos os "
                "indicadores utilizados em saúde coletiva. Um número absoluto pode indicar, por exemplo, "
                "quantas internações ocorreram em determinado hospital. Já um valor relativo permite avaliar "
                "a frequência dessas internações em relação à população atendida ou ao total de admissões."
            )
        )
        + row(
            p(
                "A escolha entre utilizar valores absolutos ou relativos depende diretamente do objetivo "
                "da análise. Para fins operacionais, como estimar a necessidade de leitos, insumos ou "
                "profissionais, os valores absolutos são indispensáveis. Para comparações entre localidades "
                "ou avaliação de risco, os valores relativos tornam-se imprescindíveis."
            )
        )
        + row(
            p(
                "Um erro comum é tratar essas duas medidas como equivalentes. Na prática, elas são "
                "complementares: enquanto os valores absolutos expressam magnitude, os valores relativos "
                "expressam intensidade ou risco."
            )
        )
        + figura
    )


def content_topico4() -> str:
    return (
        heading(4, TOPICS[3][1])
        + subheading("O que são valores absolutos?", tag="h5")
        + row(
            p(
                "Valores absolutos correspondem à contagem direta de eventos, indivíduos ou ocorrências em "
                "determinado local e período, sem qualquer tipo de padronização ou relação com o tamanho "
                "da população de referência. Representam o total bruto observado e respondem à pergunta "
                "fundamental:"
            )
        )
        + subheading("“Quantos aconteceram?”", tag="h6")
        + row(
            p(
                "Na área da saúde, são amplamente utilizados para expressar volumes de atendimento, carga "
                "de doenças ou demanda por serviços."
            )
        )
        + row(p("Exemplos frequentes incluem:"))
        + list_group(
            [
                "Número de casos novos de uma doença;",
                "Total de óbitos em um município;",
                "Quantidade de internações hospitalares;",
                "Número de partos realizados em uma maternidade;",
                "Total de notificações de violência;",
                "Número de gestantes acompanhadas no pré-natal.",
            ]
        )
        + row(
            p(
                "Esses valores permitem dimensionar a magnitude bruta de um fenômeno e são "
                "particularmente úteis para o planejamento operacional dos serviços de saúde."
            )
        )
        + subheading("Definição", tag="h6")
        + row(
            p(
                "Valores absolutos representam a contagem simples de eventos ou indivíduos em "
                "determinada população, local ou período. Não estabelecem relação direta com o tamanho "
                "da população exposta ao risco, sendo expressos apenas como números totais."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("Não há cálculo propriamente dito. Trata-se apenas da soma ou contagem dos eventos registrados:"))
        + row(p("<strong>Valor absoluto = total de eventos observados</strong>"))
        + row(p("Não há necessidade de denominador."))
        + row('<p class="small mb-2"><strong>Exemplo</strong></p>')
        + tabela1_nascimentos()
        + subheading("Usos dos valores absolutos", tag="h5")
        + row(p("Os valores absolutos são especialmente úteis para:"))
        + list_group(
            [
                "Dimensionar a magnitude bruta de problemas de saúde;",
                "Planejar recursos (leitos, profissionais, insumos);",
                "Monitorar volumes de atendimento;",
                "Identificar áreas com maior carga total de eventos;",
                "Apoiar a gestão operacional dos serviços.",
            ]
        )
        + row(
            p(
                "Por essa razão, constituem ferramenta fundamental para organização da rede assistencial "
                "e planejamento logístico."
            )
        )
        + subheading("Vantagens", tag="h5")
        + row(p("Entre as principais vantagens dos valores absolutos destacam-se:"))
        + list_group(
            [
                "Simplicidade de compreensão;",
                "Obtenção direta a partir dos registros;",
                "Utilidade para estimar demandas reais;",
                "Relevância para planejamento operacional;",
                "Representação clara da carga de trabalho dos sistemas de saúde.",
            ]
        )
        + subheading("Limitações dos valores absolutos", tag="h5")
        + row(
            p(
                "Apesar de sua utilidade, os valores absolutos apresentam limitações importantes. "
                "A principal delas é não considerar o tamanho da população exposta ao risco e isso pode "
                "levar a interpretações equivocadas. Por exemplo:"
            )
        )
        + row(
            p(
                "Um município A registra 500 casos de tuberculose e outro município B registra 200 casos. "
                "À primeira vista, o município A parece apresentar situação mais grave. Entretanto, se o "
                "município A possui 2 milhões de habitantes e o município B apenas 50 mil, o risco individual "
                "é significativamente maior no município B."
            )
        )
        + row(
            p(
                "Da mesma forma, municípios maiores em termos de população tendem naturalmente "
                "a apresentar maior número de casos de doenças, agravos ou óbitos, mesmo quando o risco "
                "proporcional é baixo."
            )
        )
        + row(
            p(
                "Assim, valores absolutos são inadequados para comparações entre territórios, grupos "
                "populacionais ou períodos com variações populacionais. Seu uso isolado pode induzir "
                "conclusões equivocadas sobre gravidade, prioridade de intervenção ou risco à saúde."
            )
        )
        + subheading("Síntese", tag="h5")
        + row(
            p(
                "Valores absolutos expressam a magnitude total de eventos em determinado espaço e tempo. "
                "São essenciais para o planejamento de serviços e dimensionamento de recursos, mas não "
                "informam sobre frequência ou risco na população. Por isso, devem ser utilizados de forma "
                "complementar aos valores relativos, especialmente quando o objetivo é comparar "
                "realidades distintas."
            )
        )
    )


def content_topico5() -> str:
    return (
        heading(5, TOPICS[4][1])
        + subheading("O que são valores relativos?", tag="h5")
        + row(
            p(
                "Valores relativos expressam a relação entre um evento de interesse e uma quantidade "
                "de referência, geralmente uma população ou um total de eventos. Diferentemente dos "
                "valores absolutos, incorporam um denominador, o que permite padronizar os dados e realizar "
                "comparações mais justas entre territórios, grupos populacionais ou períodos distintos."
            )
        )
        + row(p("Essas medidas respondem à pergunta fundamental:"))
        + subheading("“Quantos em relação a quê?”", tag="h6")
        + row(
            p(
                "Na área da saúde, os valores relativos aparecem principalmente sob a forma de proporções, "
                "razões e taxas. Todos esses formatos têm em comum a divisão de um numerador por "
                "um denominador."
            )
        )
        + subheading("Definição", tag="h6")
        + row(
            p(
                "Valores relativos representam um quantitativo expresso em relação a outro, normalmente "
                "envolvendo:"
            )
        )
        + list_group(
            [
                "Um numerador, correspondente ao evento de interesse (casos, óbitos, internações etc.);",
                "Um denominador, que representa a população ou o grupo de referência;",
                "Uma constante, utilizada para facilitar a leitura e interpretação dos resultados.",
            ]
        )
        + row(
            p(
                "Essa estrutura permite estimar frequência, intensidade ou risco, sendo amplamente utilizada "
                "em epidemiologia, vigilância em saúde e gestão de serviços."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("De forma simplificada:"))
        + row(p("<strong>Valor relativo = (evento ÷ população ou total) × constante</strong>"))
        + row(p("Onde:"))
        + list_group(
            [
                "Numerador: evento que está sendo medido;",
                "Denominador: população total ou grupo de interesse;",
                "Constante: fator de multiplicação (100, 1.000, 10.000 ou 100.000), definido conforme o tipo de indicador.",
            ]
        )
        + tabela2_obitos()
        + subheading("Principais formatos dos valores relativos", tag="h5")
        + row(p("Os valores relativos podem assumir diferentes formatos, conforme o objetivo da análise:"))
        + list_group(
            [
                "Proporções: indicam a fração de um total (ex.: percentual de partos cesáreos).",
                "Razões: relacionam grandezas distintas (ex.: razão médico por habitante).",
                "Taxas: relacionam eventos a uma população incorporando o fator tempo "
                "(ex.: taxa de mortalidade infantil).",
            ]
        )
        + row(
            p(
                "A escolha do denominador deve ser coerente com o fenômeno analisado. Por exemplo, "
                "para óbitos maternos utiliza-se o número de nascidos vivos; para incidência de doenças, "
                "a população residente. Vamos explorar melhor cada formato na próxima aula."
            )
        )
        + subheading("Usos dos valores relativos", tag="h5")
        + row(p("Os valores relativos permitem:"))
        + list_group(
            [
                "Estimar risco ou frequência de eventos;",
                "Comparar territórios e grupos populacionais;",
                "Avaliar desigualdades em saúde;",
                "Monitorar tendências temporais;",
                "Analisar desempenho de serviços.",
            ]
        )
        + row(
            p(
                "São fundamentais para epidemiologia, vigilância em saúde, avaliação de serviços e "
                "formulação de políticas públicas."
            )
        )
        + subheading("Síntese", tag="h5")
        + row(
            p(
                "Enquanto os valores absolutos expressam a magnitude total dos eventos, os valores relativos "
                "permitem avaliar intensidade, frequência e risco. Por incorporarem um denominador, "
                "possibilitam comparações mais adequadas entre realidades distintas. Assim, constituem "
                "instrumento central para análises epidemiológicas e para a tomada de decisão em saúde, "
                "sendo complementares, e não substitutos, dos valores absolutos."
            )
        )
        + quadro_comparativo1()
        + subheading("Exemplos", tag="h5")
        + row(p("Considere dois municípios:"))
        + row(
            p(
                "<strong>Município X:</strong> Casos de dengue: 300 / População: 20.000 habitantes<br />"
                "Valor absoluto: 300 casos<br />"
                "Valor relativo: (300 ÷ 20.000) × 100.000 = 1.500 casos/100.000 habitantes"
            )
        )
        + row(
            p(
                "<strong>Município Y:</strong> Casos de dengue: 500 / População: 200.000 habitantes<br />"
                "Valor absoluto: 500 casos<br />"
                "Valor relativo: (500 ÷ 200.000) × 100.000 = 250 casos/100.000 habitantes"
            )
        )
        + row(
            p(
                "Este exemplo mostra que embora Y apresente maior número absoluto de casos, X possui "
                "risco significativamente maior. Esse tipo de análise demonstra como os valores relativos são "
                "essenciais para definição de prioridades na vigilância epidemiológica."
            )
        )
        + subheading("Outro exemplo", tag="h5")
        + row(p("<strong>Hospital A:</strong> 1.000 partos em um ano."))
        + row(p("<strong>Hospital B:</strong> 600 partos neste mesmo ano."))
        + row(p("Em valores absolutos, A apresenta maior volume."))
        + row(p("Entretanto:"))
        + row(p("<strong>Hospital A:</strong> 300 foram cesarianas = (300 ÷ 1.000) × 100 = 30%"))
        + row(p("<strong>Hospital B:</strong> 300 foram cesarianas = (300 ÷ 600) × 100 = 50%"))
        + row(
            p(
                "Apesar dos hospitais terem realizado o mesmo número de cesarianas no período analisado, "
                "proporcionalmente o hospital B realiza mais cesarianas. O valor relativo revela padrões "
                "assistenciais distintos entre os hospitais."
            )
        )
        + row(p("O % indica que a constante utilizada é 100."))
    )


def content_topico6() -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{ref}</li>' for ref in REFERENCES
    )
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5 referencias-aula">'
        f'<div class="heading__block"><span class="small">Tópico 6</span>'
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
    content_topico6,
]

OLD_COURSE = "Fontes de Dados e Sistemas de Informação para o SUS"
OLD_MOD1 = "Introdução à Informação em Saúde no SUS"
OLD_MOD2 = "Fontes de Dados Socioeconômicos e Demográficos: subsídios para a Saúde"
OLD_AULA1 = (
    "Importância para a Saúde Pública e principais instituições produtoras de "
    "dados populacionais no Brasil"
)


def generate_all() -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        created.append(path)
        print(f"Criado: {path.relative_to(ROOT)}")
    return created


def update_modulo2_headers() -> int:
    """Atualiza título do curso e metadados do módulo 2 em páginas legadas."""
    skip_dirs = {OUT_DIR}
    count = 0
    for html in (ROOT / "modulo2").rglob("*.html"):
        if html.parent in skip_dirs:
            continue
        text = html.read_text(encoding="utf-8")
        original = text
        text = text.replace(OLD_COURSE, COURSE_TITLE)
        text = text.replace(OLD_MOD1, MODULE1_TITLE)
        text = text.replace(OLD_MOD2, MODULE_TITLE)
        text = text.replace(
            f"<strong>Aula 1: </strong>{OLD_AULA1}",
            f"<strong>Aula 1: </strong>{AULA_TITLE}",
        )
        if text != original:
            html.write_text(text, encoding="utf-8")
            count += 1
    print(f"Cabeçalhos atualizados em {count} arquivos do módulo 2")
    return count


def main() -> None:
    print("=== Gerando modulo2/aula1 ===")
    files = generate_all()
    print("\n=== Atualizando cabeçalhos legados do módulo 2 ===")
    update_modulo2_headers()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()
