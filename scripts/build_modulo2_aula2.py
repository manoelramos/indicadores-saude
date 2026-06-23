#!/usr/bin/env python3
"""Gera HTML da Aula 2.2 (Módulo 2) — Medidas relativas para a análise de dados de saúde."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula2"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 2
MODULE_TITLE = "Calculando indicadores"
MODULE1_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA1_TITLE = "Dados, medidas e indicadores: valores absolutos e relativos"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Medidas relativas para a análise de dados de saúde"
AULA3_TITLE = "Índices: conceitos, construção e usos"
AULA4_TITLE = "Ficha de Qualificação de Indicadores"

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("Tipos de medidas relativas", "Tipos de medidas relativas"),
    ("Padronização de taxas", "Padronização de taxas"),
    ("Erros comuns na interpretação de indicadores", "Erros comuns na interpretação de indicadores"),
    ("Referências", "Referências"),
]

OBJECTIVES = [
    "Diferenciar conceitualmente proporção, razão e taxa, reconhecendo suas aplicações "
    "específicas na área da saúde;",
    "Realizar o cálculo básico dessas medidas relativas e interpretar corretamente seus resultados;",
    "Compreender o papel da padronização de taxas na comparação entre populações com "
    "estruturas demográficas distintas;",
    "Reconhecer erros frequentes na interpretação de indicadores construídos a partir de "
    "valores absolutos e relativos.",
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
    "MEDRONHO, R. A. et al. <strong>Epidemiologia</strong>. 2. ed. São Paulo: Atheneu, 2009.",
    "TRIOLA, M. F. <strong>Introdução à estatística</strong>. 13. ed. Rio de Janeiro: LTC, 2019.",
]

OLD_AULA2_TITLE = "Dados populacionais e o Censo Demográfico"


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


def numbered_list(items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return row(f"<ol>{lis}</ol>")


def rate_formula_line(
    label_html: str,
    numerator: str,
    denominator: str,
    result: str,
    *,
    arrow: str = "",
    arrow_color: str = "",
) -> str:
    arrow_html = ""
    if arrow:
        arrow_html = (
            f'<span class="material-symbols-rounded" aria-hidden="true" '
            f"style=\"color: {arrow_color}; font-size: 2.5rem; font-variation-settings: 'FILL' 1;\">"
            f"{arrow}</span>"
        )
    return (
        f'<p class="d-flex align-items-center justify-content-center flex-wrap gap-2 mb-4">'
        f"<span>{label_html} =</span>"
        f'<span class="d-inline-flex flex-column align-items-stretch text-center px-2" '
        f'style="min-width: 7.5rem; line-height: 1.2;">'
        f"<span>{numerator}</span>"
        f'<span style="border-top: 1px solid currentColor;"></span>'
        f"<span>{denominator}</span>"
        f"</span>"
        f"<span>× 1.000 = {result}</span>"
        f"{arrow_html}"
        f"</p>"
    )


def tbm_formula_line(
    country: str, numerator: str, denominator: str, result: str, arrow: str, arrow_color: str
) -> str:
    return rate_formula_line(
        f"TBM<sub>{country}</sub>", numerator, denominator, result, arrow=arrow, arrow_color=arrow_color
    )


def tbm_calculos_brutos() -> str:
    return row(
        '<div class="text-center">'
        + tbm_formula_line("Brasil", "1.528.202", "214.583.750", "7,1", "south", "#2b6cb0")
        + tbm_formula_line("Portugal", "101.151", "11.049.635", "9,2", "north", "#e67e22")
        + "</div>"
    )


def tmp_calculo_portugal() -> str:
    return row(
        '<div class="text-center">'
        + rate_formula_line("TMP<sub>Portugal</sub>", "1.257.160", "214.583.750", "5,9")
        + "</div>"
    )


def fraction_span(numerator: str, denominator: str, *, min_width: str = "7.5rem") -> str:
    return (
        f'<span class="d-inline-flex flex-column align-items-stretch text-center px-2" '
        f'style="min-width: {min_width}; line-height: 1.2;">'
        f"<span>{numerator}</span>"
        f'<span style="border-top: 1px solid currentColor;"></span>'
        f"<span>{denominator}</span>"
        f"</span>"
    )


def rmp_calculo_portugal() -> str:
    return row(
        '<div class="text-center"><p class="d-flex align-items-center justify-content-center '
        'flex-wrap gap-2 mb-4">'
        "<span>RMP<sub>Portugal</sub> =</span>"
        + fraction_span("óbitos observados", "óbitos esperados", min_width="9rem")
        + "<span>× 100 =</span>"
        + fraction_span("101.151", "115.101")
        + "<span>× 100 = 88%</span>"
        "</p></div>"
    )


def taxa_comparacao(label: str, arrow: str, arrow_color: str) -> str:
    return row(
        '<p class="mb-3">'
        f"<strong>{label}</strong> "
        f'<span class="material-symbols-rounded align-middle" aria-hidden="true" '
        f"style=\"color: {arrow_color}; font-size: 2rem; font-variation-settings: 'FILL' 1;\">"
        f"{arrow}</span></p>"
    )


def usos_limitacoes(usos: list[str], limitacoes: list[str]) -> str:
    usos_lis = "".join(f"<li>{item}</li>" for item in usos)
    lim_lis = "".join(f"<li>{item}</li>" for item in limitacoes)
    return row(
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Usos</th><th scope="col">Limitações</th>'
        "</tr></thead><tbody><tr>"
        f'<td><ul class="mb-0 ps-3">{usos_lis}</ul></td>'
        f'<td><ul class="mb-0 ps-3">{lim_lis}</ul></td>'
        "</tr></tbody></table></div>"
    )


def flipcard(card_id: str, title: str, back_html: str, *, col: str = "col-12 col-md-4") -> str:
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


def quadro_comparativo_indicadores() -> str:
    rows = [
        (
            "Valor absoluto",
            "Quando se deseja conhecer o volume total de eventos.",
            "Dimensionar magnitude bruta do problema.",
            "Número de óbitos maternos em um município.",
            "Não permite comparação entre populações de tamanhos diferentes.",
        ),
        (
            "Proporção",
            "Quando se analisa composição ou distribuição de eventos.",
            "Avaliar participação de um grupo dentro do total.",
            "Proporção de cesarianas; proporção de gestantes com ≥7 consultas.",
            "Não mede risco nem considera tempo.",
        ),
        (
            "Razão",
            "Quando se comparam grupos distintos.",
            "Identificar desigualdades ou relações estruturais.",
            "Razão médico/habitante; razão homens/mulheres.",
            "Pode ser abstrata para público leigo; não expressa probabilidade.",
        ),
        (
            "Taxa",
            "Quando se deseja medir ocorrência ao longo do tempo.",
            "Estimar risco de adoecimento ou morte.",
            "Taxa de mortalidade infantil; taxa de incidência de TB.",
            "Depende da qualidade dos dados e da definição correta da população.",
        ),
        (
            "Prevalência",
            "Quando o foco é a carga total da doença.",
            "Planejar serviços e recursos assistenciais.",
            "Prevalência de diabetes ou hipertensão.",
            "Não diferencia casos novos de antigos.",
        ),
        (
            "Incidência",
            "Quando o interesse é surgimento de novos casos.",
            "Avaliar risco e dinâmica de transmissão.",
            "Incidência de dengue ou COVID-19.",
            "Requer acompanhamento temporal adequado.",
        ),
        (
            "Taxa padronizada",
            "Quando se comparam populações com estruturas demográficas diferentes.",
            "Garantir comparabilidade justa.",
            "Mortalidade entre regiões com diferentes perfis etários.",
            "Exige dados mais detalhados e pode ser metodologicamente mais complexa.",
        ),
    ]
    body = "".join(
        "<tr>"
        f'<th scope="row">{tipo}</th>'
        f"<td>{quando}</td><td>{objetivo}</td><td>{exemplo}</td><td>{atencao}</td>"
        "</tr>"
        for tipo, quando, objetivo, exemplo, atencao in rows
    )
    return row(
        "<p class='mb-2'><strong>Quadro 1: Quadro comparativo — Quando usar cada tipo de indicador.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Tipo de indicador</th>'
        '<th scope="col">Quando utilizar</th>'
        '<th scope="col">Objetivo principal</th>'
        '<th scope="col">Exemplo de aplicação na saúde</th>'
        '<th scope="col">Atenção / Limitação</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelo autor.</p>'
    )


def tabela1_populacao_obitos() -> str:
    rows = [
        ("0 – 19", "59.026.342", "54.723", "1.365.204", "471"),
        ("20 – 59", "121.387.791", "381.236", "6.783.020", "9.802"),
        ("60 +", "34.169.617", "1.092.243", "2.901.412", "90.878"),
        ("Total", "214.583.750", "1.528.202", "11.049.635", "101.151"),
    ]
    body = "".join(
        "<tr>"
        f"<td>{faixa}</td>"
        f'<td class="text-end">{br_pop}</td><td class="text-end">{br_ob}</td>'
        f'<td class="text-end">{pt_pop}</td><td class="text-end">{pt_ob}</td>'
        "</tr>"
        for faixa, br_pop, br_ob, pt_pop, pt_ob in rows
    )
    return row(
        "<p class='mb-2'><strong>Tabela 1: População e total de óbitos segundo faixas etárias. "
        "Brasil e Portugal, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col" rowspan="2">Faixa etária</th>'
        '<th scope="col" colspan="2" class="text-center">Brasil</th>'
        '<th scope="col" colspan="2" class="text-center">Portugal</th>'
        "</tr><tr class='bg-primary text-white'>"
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">Óbitos</th>'
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">Óbitos</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">'
        "Obs.: Dados fictícios. Fonte: Elaborado pelos autores.</p>"
    )


def tabela2_taxas_especificas() -> str:
    rows = [
        ("0 – 19", "0,9", "0,3"),
        ("20 – 59", "3,1", "1,4"),
        ("60 +", "32,0", "31,3"),
    ]
    body = "".join(
        f"<tr><td>{faixa}</td><td class='text-end'>{br}</td><td class='text-end'>{pt}</td></tr>"
        for faixa, br, pt in rows
    )
    brasil_header = (
        'Brasil <span class="material-symbols-rounded align-middle" aria-hidden="true" '
        "style=\"color: #e67e22; font-size: 1.25rem; font-variation-settings: 'FILL' 1;\">north</span>"
    )
    portugal_header = (
        'Portugal <span class="material-symbols-rounded align-middle" aria-hidden="true" '
        "style=\"color: #2b6cb0; font-size: 1.25rem; font-variation-settings: 'FILL' 1;\">south</span>"
    )
    return row(
        "<p class='mb-2'><strong>Tabela 2: Taxas específicas de mortalidade (por mil habitantes) "
        "segundo faixa etária. Brasil e Portugal, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col" rowspan="2">Faixa etária</th>'
        '<th scope="col" colspan="2" class="text-center">Taxa específica (/1.000)</th>'
        "</tr><tr class='bg-primary text-white'>"
        f'<th scope="col" class="text-end">{brasil_header}</th>'
        f'<th scope="col" class="text-end">{portugal_header}</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelo autor.</p>'
    )


def tabela3_distribuicao_populacional() -> str:
    rows = [
        ("0 – 19", "59.026.342", "27,5", "1.365.204", "12,4"),
        ("20 – 59", "121.387.791", "56,6", "6.783.020", "61,4"),
        ("60 +", "34.169.617", "15,9", "2.901.412", "26,3"),
        ("Total", "214.583.750", "100,0", "11.049.635", "100,0"),
    ]
    body = "".join(
        "<tr>"
        f"<td>{faixa}</td>"
        f'<td class="text-end">{br_pop}</td><td class="text-end">{br_pct}</td>'
        f'<td class="text-end">{pt_pop}</td><td class="text-end">{pt_pct}</td>'
        "</tr>"
        for faixa, br_pop, br_pct, pt_pop, pt_pct in rows
    )
    return row(
        "<p class='mb-2'><strong>Tabela 3: Distribuição populacional segundo faixa etária. "
        "Brasil e Portugal, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col" rowspan="2">Faixa etária</th>'
        '<th scope="col" colspan="2" class="text-center">Brasil</th>'
        '<th scope="col" colspan="2" class="text-center">Portugal</th>'
        "</tr><tr class='bg-primary text-white'>"
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">%</th>'
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">%</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelo autor.</p>'
    )


def tabela4_padronizacao_direta() -> str:
    rows = [
        ("0 – 19", "59.026.342", "0,3", "17.708"),
        ("20 – 59", "121.387.791", "1,4", "169.943"),
        ("60 +", "34.169.617", "31,3", "1.069.509"),
        ("Total", "214.583.750", "–", "1.257.160"),
    ]
    body = "".join(
        "<tr>"
        f"<td>{faixa}</td>"
        f'<td class="text-end">{pop}</td>'
        f'<td class="text-end">{taxa}</td>'
        f'<td class="text-end">{obitos}</td>'
        "</tr>"
        for faixa, pop, taxa, obitos in rows
    )
    return row(
        "<p class='mb-2'><strong>Tabela 4: População-padrão (Brasil), taxa específica de mortalidade "
        "e óbitos esperados de Portugal por faixa etária, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Faixa etária</th>'
        '<th scope="col" class="text-end">População-padrão<br />(Brasil)</th>'
        '<th scope="col" class="text-end">Taxa específica<br />de Portugal<br />(por mil hab.)</th>'
        '<th scope="col" class="text-end">Óbitos esperados<br />para Portugal</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelo autor.</p>'
    )


def tabela5_obitos_parciais() -> str:
    rows = [
        ("0 – 19", "59.026.342", "54.723", "1.365.204", "–"),
        ("20 – 59", "121.387.791", "381.236", "6.783.020", "–"),
        ("60 +", "34.169.617", "1.092.243", "2.901.412", "–"),
        ("Total", "214.583.750", "1.528.202", "11.049.635", "101.151"),
    ]
    body = "".join(
        "<tr>"
        f"<td>{faixa}</td>"
        f'<td class="text-end">{br_pop}</td><td class="text-end">{br_ob}</td>'
        f'<td class="text-end">{pt_pop}</td><td class="text-end">{pt_ob}</td>'
        "</tr>"
        for faixa, br_pop, br_ob, pt_pop, pt_ob in rows
    )
    return row(
        "<p class='mb-2'><strong>Tabela 5: População e total de óbitos segundo faixas etárias. "
        "Brasil e Portugal, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col" rowspan="2">Faixa etária</th>'
        '<th scope="col" colspan="2" class="text-center">Brasil</th>'
        '<th scope="col" colspan="2" class="text-center">Portugal</th>'
        "</tr><tr class='bg-primary text-white'>"
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">Óbitos</th>'
        '<th scope="col" class="text-end">População</th><th scope="col" class="text-end">Óbitos</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">'
        "Obs.: Dados fictícios. Fonte: Elaborado pelo autor.</p>"
    )


def tabela6_padronizacao_indireta() -> str:
    rows = [
        ("0 – 19", "0,9", "1.365.204", "1.229"),
        ("20 – 59", "3,1", "6.783.020", "21.027"),
        ("60 +", "32,0", "2.901.412", "92.845"),
        ("Total", "–", "11.049.635", "115.101"),
    ]
    body = "".join(
        "<tr>"
        f"<td>{faixa}</td>"
        f'<td class="text-end">{taxa}</td>'
        f'<td class="text-end">{pop}</td>'
        f'<td class="text-end">{obitos}</td>'
        "</tr>"
        for faixa, taxa, pop, obitos in rows
    )
    return row(
        "<p class='mb-2'><strong>Tabela 6: Taxa específica de mortalidade da população-padrão (Brasil), "
        "população e óbitos esperados de Portugal, 2024.</strong></p>"
        '<div class="table-responsive">'
        '<table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        '<th scope="col">Faixa etária</th>'
        '<th scope="col" class="text-end">Taxa específica da<br />população-padrão (Brasil)<br />(por mil hab.)</th>'
        '<th scope="col" class="text-end">População<br />de Portugal</th>'
        '<th scope="col" class="text-end">Óbitos esperados<br />para Portugal</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
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
    else:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="../aula1/topico6.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Aula anterior</a>'
        )
    if num < len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num + 1}.html" rel="next">Próximo tópico '
            f'<span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    else:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../aula3/topico1.html" rel="next">Próxima aula '
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
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA1_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>{AULA_TITLE}</a></li>
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
        + row(p(f'Seja bem-vindo e bem-vinda à aula “<strong>{AULA_TITLE}</strong>”.'))
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
    prop_usos = [
        "Analisar perfil sociodemográfico;",
        "Avaliar distribuição de características em uma população;",
        "Monitorar cobertura de serviços;",
        "Examinar a composição de eventos ou procedimentos;",
        "Descrever a estrutura de grupos populacionais.",
    ]
    prop_lim = [
        "Não expressam risco de adoecer ou morrer;",
        "Não incorporam o fator tempo;",
        "Dependem fortemente da qualidade do denominador;",
        "Não permitem inferir velocidade ou probabilidade de ocorrência de eventos.",
    ]
    raz_usos = [
        "Comparar grupos populacionais;",
        "Expressar disponibilidade de recursos;",
        "Avaliar relações entre categorias distintas;",
        "Analisar desigualdades estruturais.",
    ]
    raz_lim = [
        "Não expressam risco;",
        "Não incorporam o fator tempo;",
        "Dependem da qualidade dos dois componentes comparados;",
        "Podem ser interpretadas erroneamente como proporções ou taxas.",
    ]
    tax_usos = [
        "Estimar risco de adoecimento ou morte;",
        "Comparar territórios e grupos populacionais;",
        "Acompanhar tendências temporais;",
        "Subsidiar ações de vigilância epidemiológica;",
        "Orientar políticas públicas.",
    ]
    tax_lim = [
        "Dependem fortemente da qualidade do numerador e do denominador;",
        "Podem ser influenciadas por flutuações aleatórias em populações pequenas;",
        "Exigem atenção à escolha correta da população exposta;",
        "Frequentemente necessitam de padronização para comparações adequadas.",
    ]
    inc_usos = [
        "Estimar risco de adoecimento;",
        "Monitorar a ocorrência de agravos ao longo do tempo;",
        "Identificar surtos e epidemias;",
        "Avaliar efetividade de ações de prevenção;",
        "Apoiar decisões em vigilância epidemiológica.",
    ]
    inc_lim = [
        "Depende de sistemas de notificação sensíveis e oportunos;",
        "Pode ser subestimada em contextos de subdiagnóstico;",
        "Exige definição clara da população exposta;",
        "É influenciada por mudanças nos critérios diagnósticos ou na vigilância.",
    ]
    prev_usos = [
        "Estimar carga de doenças crônicas;",
        "Planejar serviços assistenciais;",
        "Dimensionar necessidade de medicamentos e acompanhamento;",
        "Avaliar impacto de condições de longa duração;",
        "Apoiar organização da rede de cuidados.",
    ]
    prev_lim = [
        "Não informa sobre risco de adoecimento;",
        "É influenciada tanto pela incidência quanto pela duração da doença;",
        "Pode ser afetada por óbitos ou curas;",
        "Depende da qualidade do diagnóstico e do registro dos casos.",
    ]
    return (
        heading(2, TOPICS[1][1])
        + row(
            p(
                "A análise adequada de fenômenos em saúde depende não apenas da disponibilidade de "
                "dados, mas, sobretudo, da escolha correta das medidas utilizadas para expressá-los. "
                "Entre as medidas relativas, temos as proporções, razões e taxas, que são amplamente "
                "empregadas em epidemiologia, vigilância em saúde e gestão de serviços por permitirem "
                "estimar frequência, risco e intensidade de eventos."
            )
        )
        + row(
            p(
                "No entanto, diferenças conceituais entre esses formatos, bem como a necessidade de "
                "padronização de taxas, são frequentemente negligenciadas na prática, o que pode "
                "comprometer comparações entre populações e períodos distintos. Além disso, o uso "
                "inadequado de valores absolutos ou relativos pode levar a interpretações equivocadas "
                "e decisões mal fundamentadas."
            )
        )
        + row(
            p(
                "Esta aula aborda esses aspectos, apresentando os principais tipos de medidas relativas, "
                "os fundamentos da padronização de taxas e os erros mais comuns na interpretação de "
                "indicadores de saúde."
            )
        )
        + subheading("Proporções", tag="h5")
        + subheading("O que são proporções?", tag="h5")
        + row(
            p(
                "A proporção é um tipo de medida relativa em que o numerador está contido no denominador. "
                "Em outras palavras, expressa a relação entre uma parte e o todo, sendo o numerador sempre "
                "um subconjunto do denominador. Do ponto de vista conceitual, as proporções descrevem "
                "a estrutura interna de um conjunto e respondem à pergunta fundamental:"
            )
        )
        + subheading("“Qual fração do total apresenta determinada característica?”", tag="h6")
        + row(
            p(
                "As proporções não expressam risco nem velocidade de ocorrência de eventos, mas sim "
                "a participação relativa de um grupo ou característica dentro de um total. Geralmente, "
                "são apresentadas na forma de percentual (%)."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("A estrutura básica do cálculo é:"))
        + row(p("<strong>Proporção = (parte ÷ total) × 100</strong>"))
        + subheading("Exemplo", tag="h6")
        + bullet_list(
            [
                "60 mulheres entre 150 pacientes atendidos em uma unidade de saúde:<br />"
                "(60 ÷ 150) × 100 = 40%",
            ]
        )
        + usos_limitacoes(prop_usos, prop_lim)
        + row(
            p(
                "Em síntese, as proporções oferecem uma visão clara da participação relativa dos eventos "
                "dentro de um todo, constituindo um recurso essencial para descrever e compreender a "
                "composição de fenômenos em saúde."
            )
        )
        + subheading("Razão", tag="h5")
        + subheading("O que é razão?", tag="h5")
        + row(
            p(
                "A razão é uma medida relativa que expressa a relação entre duas grandezas distintas, "
                "nas quais o numerador não está contido no denominador. Diferentemente da proporção, "
                "as duas partes comparadas pertencem a conjuntos diferentes. Do ponto de vista conceitual, "
                "a razão responde à pergunta:"
            )
        )
        + subheading("“Quanto de um grupo existe em relação a outro?”", tag="h6")
        + row(
            p(
                "As razões são utilizadas para comparar magnitudes entre grupos e não para estimar risco "
                "ou frequência de eventos ao longo do tempo."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("A estrutura geral é:"))
        + row(p("<strong>Razão = quantidade A ÷ quantidade B</strong>"))
        + row(p("Pode ser expressa como número simples ou acompanhada de texto explicativo."))
        + subheading("Exemplo", tag="h6")
        + bullet_list(
            [
                "Razão entre número de leitos hospitalares (300) por habitante (150.000) em uma cidade:<br />"
                "(300 ÷ 150.000) = 0,002. Interpretação: há 2 leitos para cada 1.000 habitantes.",
            ]
        )
        + row(
            p(
                "Assim como as proporções, as razões são essencialmente descritivas e devem ser utilizadas "
                "com cautela em análises epidemiológicas."
            )
        )
        + usos_limitacoes(raz_usos, raz_lim)
        + subheading("Taxas", tag="h5")
        + subheading("O que são taxas?", tag="h5")
        + row(
            p(
                "As taxas são medidas relativas que expressam a ocorrência de eventos em uma população "
                "ao longo do tempo. Diferenciam-se das proporções e razões por incorporarem explicitamente "
                "a dimensão temporal e uma população exposta ao risco. Do ponto de vista conceitual, "
                "as taxas respondem à pergunta:"
            )
        )
        + subheading("“Com que frequência um evento ocorre em determinada população e período?”", tag="h6")
        + row(
            p(
                "São amplamente utilizadas em epidemiologia para estimar risco e monitorar a dinâmica de "
                "doenças e agravos."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("<strong>Taxa = (número de eventos ÷ população exposta) × constante</strong>"))
        + row(
            p(
                "A constante (1.000, 10.000 ou 100.000) é definida conforme o tipo de evento, visando "
                "facilitar a interpretação."
            )
        )
        + subheading("Exemplos", tag="h6")
        + bullet_list(
            [
                "50 óbitos em uma população de 80.000 habitantes em um ano:<br />"
                "(50 ÷ 80.000) × 100.000 = 62,5 óbitos por 100.000 habitantes",
            ]
        )
        + usos_limitacoes(tax_usos, tax_lim)
        + row(
            p(
                "Entre os indicadores calculados sob a forma de taxas mais utilizados em epidemiologia "
                "destacam-se a <strong>incidência e a prevalência</strong>, que, embora frequentemente confundidas, "
                "expressam dimensões distintas do processo saúde-doença."
            )
        )
        + subheading("Incidência", tag="h5")
        + subheading("O que é incidência?", tag="h5")
        + row(
            p(
                "A incidência é uma medida epidemiológica que expressa o número de casos novos de uma "
                "determinada condição em uma população definida durante um período específico. "
                "Trata-se de uma forma particular de taxa, pois incorpora explicitamente o fator tempo e "
                "a população exposta ao risco. Refere-se ao número de casos novos de uma condição em "
                "uma população definida durante determinado período, sendo especialmente útil para avaliar "
                "o risco de adoecimento e a dinâmica de transmissão de agravos. Do ponto de vista conceitual, "
                "a incidência responde à pergunta:"
            )
        )
        + subheading("“Quantas pessoas adoeceram em determinado período?”", tag="h6")
        + row(
            p(
                "É a principal medida utilizada para estimar risco e avaliar a dinâmica de ocorrência "
                "de doenças e agravos."
            )
        )
        + subheading("Forma de cálculo", tag="h6")
        + row(p("<strong>Incidência = (número de casos novos ÷ população exposta) × constante</strong>"))
        + row(
            p(
                "A constante (1.000, 10.000 ou 100.000) é escolhida conforme a frequência do evento."
            )
        )
        + subheading("Exemplo", tag="h6")
        + bullet_list(
            [
                "120 casos novos de tuberculose em uma população de 200.000 habitantes:<br />"
                "(120 ÷ 200.000) × 100.000 = 60 casos por 100.000 habitantes",
            ]
        )
        + usos_limitacoes(inc_usos, inc_lim)
        + subheading("Prevalência", tag="h5")
        + subheading("O que é prevalência?", tag="h5")
        + row(
            p(
                "A prevalência expressa o total de casos existentes (novos e antigos) de uma condição em "
                "uma população definida, em um ponto específico do tempo ou em determinado período. "
                "Diferentemente da incidência, a prevalência não mede risco, mas sim a carga da doença na "
                "população; enquanto a incidência está relacionada aos determinantes do adoecimento, "
                "a prevalência é influenciada tanto pela incidência quanto pela duração da doença, sendo "
                "particularmente relevante para o planejamento assistencial e a organização da rede de "
                "cuidados. Do ponto de vista conceitual, a prevalência responde à pergunta:"
            )
        )
        + subheading("“Quantas pessoas convivem com essa condição neste momento?”", tag="h6")
        + subheading("Forma de cálculo", tag="h6")
        + row(p("<strong>Prevalência = (total de casos existentes ÷ população total) × constante</strong>"))
        + row(p("Geralmente expressa em percentual ou por 1.000 ou 100.000 habitantes."))
        + subheading("Exemplo", tag="h6")
        + bullet_list(
            [
                "500 pessoas com diabetes em uma população de 10.000 habitantes:<br />"
                "(500 ÷ 10.000) × 100 = 5%",
            ]
        )
        + usos_limitacoes(prev_usos, prev_lim)
        + quadro_comparativo_indicadores()
    )


def content_topico3() -> str:
    fc_bruta = (
        "<p class='mb-0'><strong>Taxa bruta:</strong> razão entre o total de eventos ocorridos em uma "
        "população e o total da população em risco. Não considera diferenças na composição etária ou "
        "demográfica. Por isso, quando populações possuem estruturas diferentes (por exemplo, uma "
        "população mais envelhecida que outra), a taxa bruta pode levar a comparações inadequadas.</p>"
    )
    fc_especifica = (
        "<p class='mb-0'><strong>Taxa específica:</strong> calculada dentro de subgrupos bem definidos "
        "(por idade, sexo, faixa etária, entre outros). Ao analisar grupos homogêneos, reduz a influência "
        "da estrutura demográfica global da população e permite comparações mais adequadas entre grupos "
        "equivalentes.</p>"
    )
    fc_padronizada = (
        "<p class='mb-0'><strong>Taxa padronizada:</strong> taxa ajustada para eliminar o efeito das "
        "diferenças na estrutura demográfica entre populações. Representa o valor que seria observado "
        "caso todas as populações tivessem a mesma composição (por exemplo, mesma distribuição etária). "
        "Seu principal objetivo é permitir comparações mais justas entre populações distintas.</p>"
    )
    return (
        heading(3, TOPICS[2][1])
        + subheading("Por que padronizar?", tag="h5")
        + row(
            p(
                "Como já foi discutido anteriormente, as taxas utilizadas em epidemiologia e saúde pública "
                "podem ser fortemente influenciadas pela estrutura da população analisada, "
                "especialmente pela distribuição etária, mas também por sexo, raça/cor ou outras "
                "características demográficas."
            )
        )
        + row(
            p(
                "Populações com maior proporção de idosos, por exemplo, tendem a apresentar taxas de "
                "mortalidade mais elevadas, independentemente das reais condições de saúde. Assim, "
                "comparar diretamente taxas entre populações com perfis distintos pode levar a "
                "interpretações equivocadas."
            )
        )
        + row(
            p(
                "A padronização é um procedimento estatístico que visa eliminar o efeito dessas diferenças "
                "estruturais, permitindo comparações mais justas entre populações ou entre diferentes "
                "períodos temporais. Em outras palavras, busca-se responder à pergunta:"
            )
        )
        + subheading(
            "“Qual seria a taxa observada se todas as populações tivessem a mesma composição demográfica?”",
            tag="h6",
        )
        + row(
            p(
                "Sem a padronização, diferenças aparentes podem refletir apenas variações demográficas, e "
                "não diferenças reais no risco ou na ocorrência do evento."
            )
        )
        + subheading("Tipos de taxas e comparabilidade", tag="h5")
        + row(
            p(
                "Antes de compreender a padronização, é importante revisar os principais tipos de taxas e "
                "entender suas implicações para comparação entre populações:"
            )
        )
        + flip_row(
            flipcard("m2a2fc1", "Taxa bruta", fc_bruta),
            flipcard("m2a2fc2", "Taxa específica", fc_especifica),
            flipcard("m2a2fc3", "Taxa padronizada", fc_padronizada),
        )
        + row(
            p(
                "Comparações diretas entre taxas podem ser distorcidas por diferenças na estrutura etária ou "
                "demográfica das populações. A padronização busca eliminar esse efeito. Esse procedimento "
                "é especialmente importante na comparação de indicadores de mortalidade e morbidade, pois "
                "apresentam forte associação com a idade."
            )
        )
        + row(
            p(
                "Mas como, na prática, eliminamos esse efeito da estrutura etária? É isso que veremos na "
                "próxima seção sobre métodos de padronização."
            )
        )
        + subheading("Métodos de padronização", tag="h5")
        + row(p("Os dois métodos mais utilizados de padronização de taxas são:"))
        + list_group(["Padronização direta;", "Padronização indireta."])
        + row(
            p(
                "A escolha do método depende principalmente da disponibilidade dos dados e da estabilidade "
                "das taxas específicas. Em situações em que as taxas por faixa etária são confiáveis e "
                "baseadas em populações suficientemente grandes, o método direto é preferível. Quando isso "
                "não ocorre, opta-se, em geral, pelo método indireto."
            )
        )
        + subheading("Método direto de padronização", tag="h5")
        + row(p("No método direto de padronização:"))
        + list_group(
            [
                "Assume-se que as taxas específicas da população em estudo são confiáveis;",
                "Utiliza-se uma população-padrão como referência comum.",
            ]
        )
        + row(
            p(
                "Esse método consiste em aplicar as taxas específicas da população estudada a uma "
                "população-padrão, estimando quantos eventos ocorreriam caso ambas tivessem a mesma "
                "distribuição etária."
            )
        )
        + row(
            p(
                "Para realizar a padronização, é necessário escolher uma população-padrão, que servirá como "
                "referência comum. Essa população-padrão pode ser real, como uma das populações "
                "envolvidas na comparação, ou a de um outro país, ou ser fictícia, como por exemplo, a média "
                "ou a soma das populações envolvidas na análise."
            )
        )
        + row(
            p(
                "O resultado obtido corresponde a uma taxa hipotética, que representa o valor que seria "
                "observado se a população estudada tivesse a mesma estrutura etária da população-padrão. "
                "Após a padronização, a taxa pode ser maior ou menor que a taxa bruta, justamente porque o "
                "efeito da estrutura etária foi removido."
            )
        )
        + subheading("Passo a passo do método direto (exemplo por faixa etária)", tag="h6")
        + numbered_list(
            [
                "Calcular as taxas específicas por faixa etária na população de estudo;",
                "Aplicar essas taxas à população-padrão;",
                "Calcular o número esperado de eventos em cada faixa etária;",
                "Somar os eventos esperados;",
                "Dividir o total de eventos esperados pelo total da população-padrão, obtendo a taxa padronizada.",
            ]
        )
        + subheading("Exemplo prático", tag="h5")
        + row(p("A pergunta aqui é:"))
        + subheading(
            "Qual dos países tem melhores condições de saúde, considerando o risco de óbito?",
            tag="h5",
        )
        + tabela1_populacao_obitos()
        + row(
            p(
                "Para avaliar o risco de óbito de cada país vamos calcular a Taxa Bruta de Mortalidade (TBM) "
                "por mil habitantes:"
            )
        )
        + tbm_calculos_brutos()
        + row(
            p(
                "<strong>Taxa Bruta de Mortalidade maior em Portugal &gt; Maior risco de óbito em Portugal &gt; "
                "Sugere melhores condições de saúde no Brasil</strong>"
            )
        )
        + row(
            p(
                "Contudo, sabemos que a mortalidade é influenciada pela faixa etária da população, então, "
                "vamos avaliar as taxas específicas de mortalidade por faixa etária:"
            )
        )
        + tabela2_taxas_especificas()
        + row(
            p(
                "Taxas específicas maiores no Brasil em todas as faixas etárias &gt; Maior risco de óbito no "
                "Brasil em todas as faixas etárias &gt; Sugere melhores condições de saúde em Portugal"
            )
        )
        + row(
            p(
                "Ficamos com uma discordância entre as análises baseadas nas taxas brutas e específicas. "
                "O que fazer? Vamos olhar a distribuição da população por faixa etária nos dois países:"
            )
        )
        + tabela3_distribuicao_populacional()
        + row(
            p(
                "As populações apresentam diferenças na estrutura etária. O Brasil tem a população mais "
                "jovem do que a de Portugal, desta forma, para comparar os dois países de forma adequada é "
                "necessário padronizar as taxas. Como temos a informação de óbito detalhada por faixa "
                "etária para os dois países, podemos aplicar o método direto de padronização."
            )
        )
        + subheading("Padronizando pelo método direto", tag="h5")
        + row(
            p(
                "Para facilitar, vamos utilizar como população-padrão a do Brasil de 2024 (a mesma "
                "considerada na comparação). Para calcular a Taxa de Mortalidade Padronizada (TMP) de "
                "Portugal precisamos calcular o total de óbitos esperados, considerando a população padrão."
            )
        )
        + tabela4_padronizacao_direta()
        + tmp_calculo_portugal()
        + row(
            p(
                "Como o Brasil foi a população padrão devemos comparar o valor padronizado de Portugal "
                "com o valor bruto do Brasil, não há necessidade de padronizá-lo."
            )
        )
        + taxa_comparacao("Taxa de mortalidade (Brasil) = 7,1 por mil hab.", "north", "#e67e22")
        + taxa_comparacao(
            "Taxa de mortalidade padronizada (Portugal) = 5,9 por mil hab.", "south", "#2b6cb0"
        )
        + row(
            p(
                "Essa taxa simula uma situação na qual a estrutura etária da população de Portugal seria "
                "idêntica à do Brasil em 2024, mantendo-se as taxas específicas por idade observadas "
                "em Portugal."
            )
        )
        + row(
            p(
                "Com estes resultados concluímos que, comparando as taxas padronizadas por faixa etária, "
                "o <strong>Brasil apresentou o maior risco de óbito</strong>, e consequentemente "
                "<strong>piores condições de saúde, comparado à Portugal</strong> no ano avaliado."
            )
        )
        + row(
            p(
                "Se tivéssemos comparado as taxas brutas, Portugal teria apresentado risco maior de óbito "
                "em 2024 (Brasil: 7,1/1.000 hab.; Portugal: 9,2/1.000 hab.) e estaríamos interpretando "
                "erroneamente a relação entre Brasil e Portugal."
            )
        )
        + subheading("Método indireto de padronização", tag="h5")
        + row(p("O método indireto de padronização é indicado quando:"))
        + list_group(
            [
                "Não se dispõe de taxas específicas confiáveis na população em estudo;",
                "Apenas o total de eventos é conhecido;",
                "Os contingentes populacionais são pequenos, o que gera instabilidade nas taxas específicas.",
            ]
        )
        + row(
            p(
                "Nessas situações, em vez de utilizar as taxas da população estudada, utilizam-se as taxas "
                "específicas da população-padrão. Essas taxas são então aplicadas à estrutura etária da "
                "população em estudo, permitindo calcular o número esperado de eventos."
            )
        )
        + row(
            p(
                "A partir dessa comparação entre eventos observados e esperados, obtém-se, em geral, "
                "a Razão de Mortalidade Padronizada (RMP) ou indicador equivalente."
            )
        )
        + row(
            p(
                "Esse método é especialmente útil em análises de pequenas áreas geográficas, serviços de "
                "saúde específicos ou populações reduzidas, nas quais as taxas específicas apresentam "
                "grande variabilidade."
            )
        )
        + subheading("Exemplo prático", tag="h5")
        + row(p("Vamos manter a mesma pergunta do exemplo anterior:"))
        + subheading(
            "Qual dos países tem melhores condições de saúde, considerando o risco de óbito?",
            tag="h5",
        )
        + row(
            p(
                "Porém agora, vamos supor que não temos a informação sobre os óbitos por faixa etária, "
                "apenas o total de óbitos de Portugal."
            )
        )
        + tabela5_obitos_parciais()
        + row(
            p(
                "Como faríamos para comparar, sabendo que há necessidade de padronização por conta "
                "da diferença na estrutura etária da população?"
            )
        )
        + row(p("Em situações como esta aplicamos o método indireto de padronização."))
        + subheading("Padronizando pelo método indireto", tag="h5")
        + row(
            p(
                "Neste caso, aplicamos a taxa específica da população padrão (Brasil) na população "
                "de Portugal para encontrar os óbitos esperados e calcular a Razão de Mortalidade "
                "Padronizada (RMP):"
            )
        )
        + tabela6_padronizacao_indireta()
        + rmp_calculo_portugal()
        + row(
            p(
                "Este resultado é interpretado da seguinte forma: para cada 88 óbitos observados em "
                "Portugal no ano 2024, dadas as condições de saúde lá vigentes, espera-se a ocorrência "
                "de 100 óbitos, caso a população de Portugal estivesse exposta às condições de saúde "
                "existentes no Brasil, neste mesmo ano."
            )
        )
        + row(
            p(
                "Conclui-se assim, que o <strong>Brasil tem maior risco de óbito</strong>, e consequentemente, "
                "<strong>piores condições de saúde do que em Portugal</strong> no ano de 2024."
            )
        )
        + subheading("Conclusões sobre padronização", tag="h5")
        + list_group(
            [
                "Duas populações podem apresentar taxas específicas de mortalidade idênticas, mas, se "
                "tiverem distribuições etárias diferentes, produzirão taxas brutas distintas.",
                "Em contextos de envelhecimento populacional, a taxa bruta de mortalidade de um país "
                "pode aumentar mesmo que suas taxas específicas permaneçam estáveis. Isso não significa, "
                "necessariamente, piora nas condições de saúde, mas sim mudança na estrutura etária.",
                "A padronização é o procedimento que permite controlar esse efeito da estrutura "
                "demográfica, tornando as comparações mais adequadas.",
                "A escolha entre padronização direta e indireta depende das informações disponíveis "
                "e da estabilidade das taxas específicas.",
                "Os resultados obtidos pelos métodos direto e indireto não são idênticos, pois partem "
                "de pressupostos distintos:"
                "<ul class='mb-0 mt-2 ps-3'>"
                "<li>A padronização direta utiliza uma população-padrão;</li>"
                "<li>A padronização indireta utiliza um conjunto de taxas específicas padrão.</li>"
                "</ul>",
                "Não existe um método perfeito para comparar taxas entre populações distintas. Entretanto, "
                "quando há informação detalhada e taxas específicas estáveis, a padronização direta é "
                "geralmente preferível por permitir comparações mais consistentes entre múltiplas populações.",
            ]
        )
    )


def content_topico4() -> str:
    return (
        heading(4, TOPICS[3][1])
        + row(
            p(
                "Na análise de indicadores em saúde, alguns equívocos são recorrentes e podem comprometer "
                "significativamente a interpretação dos resultados. Entre os mais frequentes estão a "
                "comparação de valores absolutos entre populações diferentes, a desconsideração do "
                "denominador, o uso de taxas sem compreender sua base de cálculo e a falta de atenção ao "
                "tamanho ou às mudanças na estrutura populacional ao longo do tempo."
            )
        )
        + row(
            p(
                "Comparar apenas números absolutos pode gerar interpretações equivocadas, pois "
                "populações maiores tendem naturalmente a apresentar maior número de eventos. Da mesma "
                "forma, ignorar o denominador impede a compreensão do risco real. Utilizar uma taxa sem "
                "conhecer sua constante, sua fonte de dados ou o período analisado também compromete a "
                "validade da análise."
            )
        )
        + row(
            p(
                "Uma prática analítica adequada exige sempre verificar o que está sendo contado (numerador), "
                "qual é a população em risco (denominador), qual constante foi utilizada, qual a fonte dos "
                "dados e qual o período de referência. Esses elementos são fundamentais para garantir "
                "transparência, comparabilidade e coerência interpretativa."
            )
        )
        + row(
            p(
                "Ao longo deste módulo, vimos que valores absolutos e medidas relativas cumprem funções "
                "distintas e complementares. Enquanto os valores absolutos expressam magnitude e "
                "dimensionamento de problemas, as medidas relativas permitem avaliar risco, desigualdades "
                "e realizar comparações entre populações. A escolha da forma de cálculo influencia "
                "diretamente a interpretação dos resultados e, consequentemente, a tomada de decisão "
                "em saúde."
            )
        )
        + row(
            p(
                "Quando existem diferenças estruturais entre populações, especialmente relacionadas à "
                "idade, a padronização torna-se essencial para garantir comparações mais justas. Assim, "
                "compreender os conceitos, métodos, aplicações e limitações das medidas relativas é condição "
                "indispensável para análises consistentes e produção de evidências confiáveis."
            )
        )
        + row(
            p(
                "Encerrar esta aula compreendendo a diferença entre “quantos existem” e “qual é o risco” "
                "significa avançar um passo decisivo na transformação de dados em informação qualificada, "
                "e de informação qualificada em ação em saúde."
            )
        )
    )


def content_topico5() -> str:
    lis = "".join(
        f'<li class="list-group-item" list-style="default">{ref}</li>' for ref in REFERENCES
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


def generate_all() -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        created.append(path)
        print(f"Criado: {path.relative_to(ROOT)}")
    for orphan in OUT_DIR.glob("topico*.html"):
        if orphan not in created:
            orphan.unlink()
            print(f"Removido: {orphan.relative_to(ROOT)}")
    return created


def update_modulo2_aula2_references() -> int:
    """Atualiza referências legadas à aula 2 do módulo 2 em outras páginas."""
    count = 0
    for html in (ROOT / "modulo2").rglob("*.html"):
        if html.parent == OUT_DIR:
            continue
        text = html.read_text(encoding="utf-8")
        original = text
        text = text.replace(OLD_AULA2_TITLE, AULA_TITLE)
        text = text.replace(
            f"<strong>Aula 2: </strong>{OLD_AULA2_TITLE}",
            f"<strong>Aula 2: </strong>{AULA_TITLE}",
        )
        if text != original:
            html.write_text(text, encoding="utf-8")
            count += 1
    print(f"Referências à aula 2 atualizadas em {count} arquivos do módulo 2")
    return count


def main() -> None:
    print("=== Gerando modulo2/aula2 ===")
    files = generate_all()
    print("\n=== Atualizando referências legadas da aula 2 ===")
    update_modulo2_aula2_references()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()
