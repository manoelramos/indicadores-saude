#!/usr/bin/env python3
"""Gera HTML da Aula 2.4 (Módulo 2) — Ficha de Qualificação de Indicadores."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula4"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 2
MODULE_TITLE = "Calculando indicadores"
MODULE1_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA1_TITLE = "Dados, medidas e indicadores: valores absolutos e relativos"
AULA2_TITLE = "Medidas relativas para a análise de dados de saúde"
AULA3_TITLE = "Índices: conceitos, construção e usos"
AULA_LABEL = "Aula 4"
AULA_TITLE = "Ficha de Qualificação de Indicadores"

TOPICS = [
    "Sobre esta aula",
    "O que é uma Ficha de Qualificação de Indicadores (FQI)?",
    "A Rede Interagencial de Informações para a Saúde (Ripsa)",
    "As Fichas de Qualificação dos Indicadores da Ripsa",
    "Campos complementares para FQI",
    "Bibliografia",
]


def row(*blocks: str) -> str:
    inner = "".join(blocks)
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5">'
        f"{inner}</div></div>"
    )


def row_mb4(*blocks: str) -> str:
    inner = "".join(blocks)
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-4">'
        f"{inner}</div></div>"
    )


def heading_block(title: str, *, small: str | None = None, tag: str = "h3") -> str:
    small_html = f'<span class="small">{small}</span>' if small else ""
    return f'<div class="heading__block">{small_html}<{tag} class="heading__title">{title}</{tag}></div>'


def p(text: str) -> str:
    return f"<p>{text}</p>"


def list_group(items: list[str]) -> str:
    lis = "".join(
        f'<li class="list-group-item aos-init aos-animate" list-style="default" '
        f'data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">{item}</li>'
        for item in items
    )
    return f'<div class="list"><ul class="list-group">{lis}</ul></div>'


def figure(img: str, alt: str, caption: str, *, strong_caption: str | None = None) -> str:
    cap = strong_caption or caption
    return (
        f'<p class="mb-2"><strong>{cap}</strong></p>'
        f'<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{ASSETS}{img}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{caption}</p>'
    )


def flipcard(card_id: str, title: str, body: str) -> str:
    return (
        f'<div class="col-12 col-md-6"><div class="flipcard"><div class="flip-card">'
        f'<input type="checkbox" id="{card_id}" class="more" aria-hidden="true" />'
        f'<div class="flip-card-inner">'
        f'<div class="card shadow flip-card-front fundo1"><div class="h-100 bg-transparent border-0 text-center">'
        f'<div class="card-body justify-content-center d-flex flex-column"><span class="h5 card-title">{title}</span></div>'
        f'<div class="card-footer text-white"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-primary" aria-hidden="true">'
        f'<img src="{ASSETS}media/templates/flipcard-icon-dark.svg" alt="" width="36" /> Confira</label>'
        f"</div></div></div></div>"
        f'<div class="card flip-card-back"><div class="h-100 bg-transparent border-0 text-center">'
        f'<div class="card-body justify-content-center d-flex flex-column">'
        f'<span class="h5">{title}</span>'
        f'<div class="scrollable text-start">{body}</div></div>'
        f'<div class="card-footer"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-secondary return" aria-hidden="true">'
        f'<span class="material-symbols-rounded">arrow_back</span></label>'
        f"</div></div></div></div></div></div></div></div>"
    )


def flipcard_row(cards: list[tuple[str, str, str]]) -> str:
    cols = "".join(flipcard(cid, title, body) for cid, title, body in cards)
    return f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8"><div class="row g-4 mb-5">{cols}</div></div></div>'


def box_para_assistir(body: str) -> str:
    return (
        f'<div class="box" data-box="Para Assistir"><div class="card">'
        f'<div class="card-header"><span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">Para Assistir!</span></div>'
        f'<div class="card-body">{body}</div></div></div>'
    )


def box_saiba_mais(body: str, *, collapse_id: str = "m2a4sm1") -> str:
    return (
        f'<div class="saiba-mais pb-5"><div class="row aos-init aos-animate" data-aos="fade-left" '
        f'data-aos-easing="ease-out" data-aos-duration="600">'
        f'<div class="col-12 d-flex justify-content-center">'
        f'<button class="saiba-mais fio-button button-md fio-button-secondary collapsed" type="button" '
        f'data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="false" '
        f'aria-controls="{collapse_id}">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span> Saiba Mais</button>'
        f"</div>"
        f'<div class="col-12"><div class="mt-3 collapse" id="{collapse_id}">{body}</div></div>'
        f"</div></div>"
    )


def box_atencao(body: str) -> str:
    return (
        f'<div class="box" data-box="Atenção"><div class="card aos-init aos-animate" '
        f'data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<div class="card-header"><span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">Atenção</span></div>'
        f'<div class="card-body"><div class="custom-shape-divider-top-1720289331">'
        f'<svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">'
        f'<path d="M1200 120L0 16.48 0 0 1200 0 1200 120z" class="shape-fill"></path></svg></div>'
        f"<div>{body}</div></div></div></div>"
    )


def fqi_field_body(description: str, examples: list[str] | str | None = None) -> str:
    body = f"<p>{description}</p>"
    if examples:
        body += "<p><strong>Exemplo:</strong></p>"
        if isinstance(examples, str):
            body += examples
        else:
            items = "".join(f"<li>{item}</li>" for item in examples)
            body += f"<ul>{items}</ul>"
    return body


def accordion_item(parent_id: str, item_id: str, title: str, body: str) -> str:
    header_id = f"{item_id}-h"
    collapse_id = f"{item_id}-c"
    return (
        f'<div class="accordion-item">'
        f'<h5 class="accordion-header" id="{header_id}">'
        f'<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" '
        f'data-bs-target="#{collapse_id}" aria-expanded="false" aria-controls="{collapse_id}">'
        f"{title}</button></h5>"
        f'<div id="{collapse_id}" class="accordion-collapse collapse" aria-labelledby="{header_id}" '
        f'data-bs-parent="#{parent_id}">'
        f'<div class="accordion-body">{body}</div></div></div>'
    )


def accordion_block(parent_id: str, items: list[tuple[str, str, list[str] | str | None]]) -> str:
    items_html = "".join(
        accordion_item(parent_id, f"{parent_id}-{i}", title.upper(), fqi_field_body(desc, ex))
        for i, (title, desc, ex) in enumerate(items, start=1)
    )
    return (
        f'<div class="accordion accordion-flush aos-init aos-animate" id="{parent_id}" '
        f'data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">{items_html}</div>'
    )


def accordion_row(parent_id: str, items: list[tuple[str, str, list[str] | str | None]]) -> str:
    return row(accordion_block(parent_id, items))


def row_columns(text_html: str, image_html: str) -> str:
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5">'
        f'<div class="row g-4 align-items-center">'
        f'<div class="col-12 col-md-6">{text_html}</div>'
        f'<div class="col-12 col-md-6">{image_html}</div>'
        f"</div></div></div>"
    )


COMPLEMENTARY_FLIPCARDS = [
    (
        "m2a4fc1",
        "Tipo de indicador",
        "<p class='mb-0'>Campo para informar se é número absoluto, taxa, proporção, etc.</p>",
    ),
    (
        "m2a4fc2",
        "Unidade de medida",
        "<p class='mb-0'>Campo destinado ao registro da unidade de medida (óbito, habitante, internações, casos de uma doença etc.).</p>",
    ),
    (
        "m2a4fc3",
        "Polaridade",
        "<p class='mb-0'>Campo destinado ao registro do sentido do indicador: quanto maior o valor do indicador, melhor (maior-melhor); quanto menor o valor do indicador, melhor (menor-melhor) ou não se aplica um padrão (sem polaridade).</p>",
    ),
    (
        "m2a4fc4",
        "Periodicidade de monitoramento ou avaliação",
        "<p class='mb-0'>Campo destinado a indicar a periodicidade com que o indicador é acompanhado de forma sistemática ou tem seu resultado avaliado ao longo do tempo.</p>",
    ),
    (
        "m2a4fc5",
        "Indicadores relacionados",
        "<p class='mb-0'>Identificação de indicadores que guardam relação com o indicador em questão, considerando aqueles cujo objeto de mensuração está associado e é relevante para a análise do problema.</p>",
    ),
    (
        "m2a4fc6",
        "Valor de referência ou parâmetro de referência",
        "<p class='mb-0'>Campo destinado à especificar o padrão, a referência ou a regra utilizada para estabelecer critérios de comparação e avaliação da evolução do indicador ao longo do tempo.</p>",
    ),
    (
        "m2a4fc7",
        "Classificação gerencial",
        "<p class='mb-0'>Campo destinado a classificar o indicador segundo sua natureza gerencial e função no monitoramento e na avaliação de políticas, programas, projetos ou ações — indicador de insumo, indicador de processo, indicador de produto, indicador de resultado ou indicador de impacto.</p>",
    ),
    (
        "m2a4fc8",
        "Palavras-chave ou marcadores",
        "<p class='mb-0'>Campo destinado ao registro de palavras-chave que associam o indicador a temas estratégicos, facilitando sua identificação, busca e utilização nos sistemas de informação.</p>",
    ),
]


def content_topico1() -> str:
    return (
        row(heading_block("Sobre esta aula", small="Tópico 1"))
        + row(
            p('Seja bem-vindo e bem-vinda à aula "<strong>Ficha de Qualificação de Indicadores</strong>".'),
            p(
                "Nas últimas aulas, você conheceu as diferentes formas utilizadas na construção de indicadores. "
                "Agora é hora de aprender a documentar a construção dos indicadores, um processo essencial para "
                "garantir a transparência metodológica e o uso qualificado de indicadores."
            ),
        )
        + row(
            p("Ao final dessa aula, você será capaz de:"),
            list_group(
                [
                    "Reconhecer a importância das fichas de qualificação dos indicadores;",
                    "Conhecer a iniciativa da Rede Interagencial de Informações para a Saúde (Ripsa);",
                    "Compreender os principais campos utilizados em fichas de qualificação dos indicadores.",
                ]
            ),
        )
        + row_mb4(heading_block("Autoria", tag="h4"))
        + row(
            p("<strong>Carolina de Campos Carvalho</strong>"),
            p(
                "Doutora e Mestre em Saúde Pública, Analista Técnica de Políticas Sociais. "
                "Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da "
                "Fundação Oswaldo Cruz (Fiocruz)."
            ),
            p("<strong>Aline Pinto Marques</strong>"),
            p(
                "Doutora em Epidemiologia em Saúde Pública. Instituto de Comunicação e Informação Científica "
                "e Tecnológica em Saúde (Icict) da Fundação Oswaldo Cruz (Fiocruz)."
            ),
        )
    )


def content_topico2() -> str:
    return (
        row(heading_block("O que é uma Ficha de Qualificação de Indicadores (FQI)?", small="Tópico 2"))
        + row(
            p(
                "A Ficha de Qualificação do Indicador (FQI) é um instrumento fundamental para garantir a "
                "transparência metodológica e a padronização das informações utilizadas na construção e "
                "interpretação dos indicadores em saúde. Seu objetivo central é descrever de forma clara a "
                "conceituação, a interpretação, o cálculo, as limitações e os usos de cada indicador, entre "
                "outras informações relevantes, permitindo que diferentes usuários compreendam exatamente o que "
                "está sendo mensurado, como o cálculo foi realizado e quais cuidados são necessários ao interpretar "
                "seus resultados."
            ),
            p(
                "Essa sistematização assegura que o uso dos indicadores seja tecnicamente consistente e comparável "
                "ao longo do tempo e entre diferentes contextos."
            ),
            p(
                "Além disso, a FQI cumpre um papel estratégico ao qualificar o uso dos indicadores em saúde, sendo "
                "essencial para promover a reprodutibilidade, evitar interpretações equivocadas e fortalecer a "
                "governança da informação no âmbito do Sistema Único de Saúde (SUS). Trata-se de um instrumento de "
                "orientação técnica e de caracterização dos indicadores, com o objetivo de explicitar os critérios, "
                "conceitos e escolhas adotadas, bem como apontar as possíveis limitações do indicador."
            ),
        )
        + row(
            figure(
                "media/modulo2/mod2-a4-fig1-ficha-qualificacao.png",
                "Mão preenchendo formulário em prancheta intitulado Ficha de qualificação do indicador, com campos para título, conceituação, interpretação, usos, limitações, fontes e método de cálculo.",
                "Fonte: Elaboração própria.",
                strong_caption="Figura 1 – Ficha de Qualificação do Indicador.",
            )
        )
    )


def content_topico3() -> str:
    return (
        row(heading_block("A Rede Interagencial de Informações para a Saúde (Ripsa)", small="Tópico 3"))
        + row_mb4(heading_block("A Ripsa e os indicadores para a saúde", tag="h5"))
        + row(
            p(
                "A Rede Interagencial de Informações para a Saúde foi criada em 1996, através de cooperação entre "
                "o Ministério da Saúde e a Organização Pan-Americana da Saúde/Organização Mundial da Saúde (OPAS/OMS). "
                "A Rede conforma-se como uma iniciativa colaborativa que reúne instituições governamentais e não "
                "governamentais com o objetivo de gerar, analisar e disseminar informações para a saúde pública."
            ),
            p(
                "Após quase 10 anos de paralisação, a Ripsa foi reativada em 2023, por iniciativa do Ministério da "
                "Saúde, em parceria com a OPAS/OMS, o Conselho Nacional de Secretários de Saúde (Conass) e o Conselho "
                "Nacional de Secretarias Municipais de Saúde (Conasems), que formam a Secretaria Técnica da Rede. "
                "Atualmente, é composta por mais de quarenta instituições participantes. Conheça quais "
                '<a href="https://www.ripsa.org.br/" target="_blank" rel="noopener noreferrer">nesta</a> página.'
            ),
            p(
                "Uma das instâncias técnicas da Ripsa são os "
                '<a href="https://www.ripsa.org.br/comites/cgi/" target="_blank" rel="noopener noreferrer">'
                "Comitês de Gestão de Indicadores (CGI)</a>, "
                "constituídos por representantes de instituições envolvidas com a produção e o uso de indicadores. "
                "Atualmente, existem sete subconjuntos temáticos: Demográfico, Socioeconômico, Morbidade, Mortalidade, "
                "Cobertura, Recursos e Fatores de risco e proteção. Os CGI pautam seu trabalho pela construção de "
                "consensos sobre conceitos, métodos e critérios para o uso de diferentes bases de dados e construção "
                "de indicadores."
            ),
        )
        + row(
            box_atencao(
                "<p>A partir da produção de cada CGI, foi construída a <strong>matriz de indicadores da Ripsa</strong>, "
                "que passa por revisão e atualização periódicas, o que inclui alterações, acréscimos e supressões de "
                "indicadores. São critérios para a construção da matriz:</p>"
                "<p>i) relevância para a compreensão da situação de saúde, suas causas e consequências;<br />"
                "ii) validade para orientar decisões políticas e apoiar o controle social;<br />"
                "iii) identidade com processos de gestão do Sistema Único de Saúde (SUS); e<br />"
                'iv) disponibilidade de fontes regulares" (Rede, 2026, p.39).</p>'
            )
        )
        + row(
            p(
                "Além dos CGI, a Ripsa possui outros grupos de trabalho, denominados Comitês Temáticos "
                "Interdisciplinares (CTIs). São grupos temporários, com o objetivo de abordar temas específicos e "
                "prioritários."
            )
        )
        + row(
            box_saiba_mais(
                "<p class=\"mb-0\">Leia o artigo "
                '<a href="https://doi.org/10.1590/S1413-81232006000400025" target="_blank" rel="noopener noreferrer">'
                "“Informação em saúde no Brasil: a contribuição da Ripsa”</a>, escrito por João Baptista Risi Júnior, "
                "sobre a criação da Ripsa.</p>"
            )
        )
    )


def content_topico4() -> str:
    metodo_exemplo = (
        "<ul>"
        "<li><strong>Numerador:</strong> Número de internações hospitalares – acessar o SIH/SUS, considerar a "
        "quantidade de internações (IDENT = 1), segundo o município de residência (MUNIC_RES) e o ano de internação "
        "(DT_INTER – quatro primeiros dígitos), com ESPEC fora da faixa 09 a 14. Para seleção do tipo de especialidade, "
        "utilizar as seguintes seleções: Clínica (ESPEC = 03); Cirúrgica (ESPEC = 01); Pediátrica (ESPEC = 07); "
        "Obstétrica (ESPEC = 02); e Outras (ESPEC = 04 – Cuidados Prolongados, 05 – Psiquiatria, 06 – Tisiologia, "
        "08 – Reabilitação, 87 – Saúde Mental, 17 – Estabelecimento Exclusivo UTI SUS).</li>"
        "<li><strong>Denominador:</strong> População total residente.</li>"
        "<li><strong>Multiplicador:</strong> 100.</li>"
        "<li><strong>Notas:</strong>"
        "<ul>"
        "<li>As internações em hospital-dia não estão contabilizadas nesse indicador.</li>"
        "<li>A taxa de internações hospitalares pediátricas foi calculada sobre a população estimada de zero a 19 anos de idade.</li>"
        "<li>A taxa de internações hospitalares obstétricas foi calculada sobre a população feminina estimada de 10 a 49 anos de idade.</li>"
        "<li>As internações foram contabilizadas segundo município de residência do paciente e ano de internação.</li>"
        "</ul></li></ul>"
    )
    interpretacao_exemplo = (
        "<ul>"
        "<li>Mede a relação entre a produção de internações hospitalares com financiamento pelo SUS e a população "
        "residente na mesma área geográfica.</li>"
        "<li>É influenciada por: i) fatores socioeconômicos, epidemiológicos e demográficos, tais como nível de renda, "
        "perfil de morbidade e composição etária; ii) infraestrutura de serviços, com relação à disponibilidade de "
        "recursos humanos, materiais, tecnológicos e financeiros; iii) políticas públicas assistenciais e preventivas, "
        "tais como a regionalização e hierarquização do sistema de saúde e critérios técnico-administrativos de pagamento "
        "adotados no âmbito do SUS; iv) políticas públicas intersetoriais e gestão em saúde; v) processos de trabalho "
        "das equipes; e vi) necessidades de saúde das populações.</li>"
        "</ul>"
    )
    usos_exemplo = (
        "<ul>"
        "<li>Analisar variações geográficas e temporais na distribuição das internações hospitalares realizadas no SUS, "
        "identificando-se situações de desigualdade e tendências que demandem ações e estudos específicos.</li>"
        "<li>Contribuir para se avaliar a adequação do volume de internações às necessidades da população atendida.</li>"
        "<li>Subsidiar processos de planejamento, gestão, monitoramento e avaliação de políticas públicas voltadas para "
        "a assistência médico-hospitalar de responsabilidade do SUS.</li>"
        "</ul>"
    )
    limitacoes_exemplo = (
        "<ul>"
        "<li>Pode não incluir todas as internações efetivamente realizadas pelo SUS, em função de limites definidos "
        "pela programação física e financeira do sistema público de saúde.</li>"
        "<li>Há possibilidade de subnotificação do número de internações realizadas em hospitais públicos financiados "
        "por transferência direta de recursos e não por produção de serviços.</li>"
        "<li>Não inclui as internações realizadas em unidades hospitalares sem vínculo com o SUS, embora o denominador "
        "seja a população total. Não estão contabilizadas, portanto, as internações que correspondem à saúde "
        "suplementar, à assistência aos servidores públicos civis e militares, a recursos próprios da unidade de "
        "internação e a serviços prestados mediante desembolso direto (exclusivamente privados).</li>"
        "<li>Transferências e reinternações podem estar contadas como novas internações.</li>"
        "</ul>"
    )

    fqi_fields = [
        (
            "Código da Ripsa",
            "Traz a identificação com a sigla da dimensão (Demográfico, Socioeconômico, Morbidade, Mortalidade, "
            "Cobertura, Recursos ou Fatores de risco e proteção) e do número do indicador específico.",
            ["COB.2.01"],
        ),
        (
            "Título completo",
            "Descrição do que está sendo mensurado, incluindo as intenções de dimensionamento.",
            ["Taxa de internações hospitalares (SUS) por 100 habitantes"],
        ),
        (
            "Título resumido",
            "Deve expressar de forma concisa o que está sendo mensurado pelo indicador para uso em tabelas, "
            "quadros, gráficos e painéis.",
            ["Taxa de internações hospitalares (SUS) por 100 habitantes"],
        ),
        (
            "Conceito",
            "Especifica os conceitos utilizados no indicador, definindo sua natureza e forma de expressão. "
            "Deve incluir elementos que facilitem a compreensão do que está sendo mensurado.",
            [
                "Número de internações hospitalares financiadas pelo Sistema Único de Saúde (SUS), por 100 habitantes, "
                "na população residente, em um local e ano de referência."
            ],
        ),
        (
            "Interpretação",
            "Orienta a análise e compreensão dos dados do indicador, oferecendo uma explicação sucinta sobre o "
            "tipo de informação obtida e seu significado para a saúde.",
            interpretacao_exemplo,
        ),
        (
            "Usos",
            "Descreve as principais formas e razões para a utilização dos dados e informações do indicador.",
            usos_exemplo,
        ),
        (
            "Limitações",
            "Indica os fatores que podem restringir a interpretação e aplicação do indicador. Essas limitações "
            "podem estar relacionadas à apuração dos dados, fonte, fórmula de cálculo, interpretação ou "
            "temporalidade, influenciando a avaliação da situação analisada.",
            limitacoes_exemplo,
        ),
        (
            "Fonte de dados",
            "Refere-se à base de origem dos dados utilizados no cálculo.",
            [
                "Sistema de Informações Hospitalares (SIH).",
                "Projeções da população do Brasil e das Unidades da Federação: estimativas e projeções.",
            ],
        ),
        (
            "Fórmula de cálculo",
            "Trata-se da expressão matemática que combina as variáveis e os elementos de um indicador para obtenção de resultado.",
            [
                "Número de internações hospitalares financiadas pelo SUS, em um local e ano de referência / "
                "População total residente, em um local e ano de referência × 100"
            ],
        ),
        (
            "Método de cálculo",
            "Descreve o procedimento necessário para calcular o indicador, detalhando os processos envolvidos. "
            "Deve garantir a possibilidade de reprodutibilidade por equipe de tecnologia da informação autorizada, "
            "considerando-se a eventual confidencialidade dos dados.",
            metodo_exemplo,
        ),
        (
            "Variáveis e categorias de análise",
            "Representam a segmentação do indicador para análises específicas, apresentando as variáveis como sexo, "
            "faixa etária, território, cor ou raça, estabelecimento de saúde com suas respectivas categorias, entre outros.",
            ["Tipo de especialidade: Clínica; Cirúrgica; Pediátrica; Obstétrica; e Outras."],
        ),
        (
            "Granularidade",
            "Define o recorte espacial/territorial de referência do indicador recomendado para desagregação máxima do "
            "dado (menor grau da informação), dentro do prazo previsto para atualização do indicador.",
            ["Município."],
        ),
        (
            "Periodicidade de atualização",
            "Refere-se à frequência com que os dados são atualizados no banco de dados (diária, bimensal, mensal, anual, semestral).",
            ["Anual."],
        ),
        (
            "Responsabilidade gerencial",
            "Identifica a unidade gestora encarregada de promover o acompanhamento sistemático e contínuo do indicador, "
            "assim como de proceder à tomada de decisão em relação ao resultado obtido.",
            [
                "Departamento de Regulação Assistencial e Controle da Secretaria de Atenção Especializada à Saúde "
                "do Ministério da Saúde (DRAC/SAES/MS)."
            ],
        ),
        (
            "Notas",
            "É o campo aberto para informações complementares não contempladas nos demais campos, permitindo o registro "
            "de contextualizações adicionais, observações metodológicas ou alertas específicos para os usuários.",
            ["Não se aplica."],
        ),
        (
            "Análise descritiva do indicador",
            "Este é um componente especialmente diferencial da FQI da Ripsa. Vai além da definição técnica, apresentando "
            "uma descrição geral do indicador, um breve relato sobre a situação de saúde a ele referente e a forma como "
            "será representado nas análises descritivas, acompanhados das respectivas visualizações (figuras, tabelas, "
            "quadros, gráficos etc.). Essas visualizações são imediatamente precedidas de suas descrições, oferecendo aos "
            "usuários uma compreensão prática e contextualizada do comportamento do indicador na realidade do SUS. Este "
            "campo transforma a ficha de um documento técnico em uma ferramenta narrativa e analítica, enriquecendo "
            "significativamente a interpretação e a divulgação dos dados.",
            ["Tabela acompanhada de parágrafo descritivo."],
        ),
    ]

    return (
        row(heading_block("As Fichas de Qualificação dos Indicadores da Ripsa", small="Tópico 4"))
        + row(
            p(
                "Um eixo central no trabalho da Rede é a elaboração das Fichas de Qualificação do Indicador (FQIs), "
                "adotadas como ferramentas de padronização e transparência metodológica. A FQI da Ripsa é composta por "
                "16 campos, detalhados a seguir. Para exemplificar o preenchimento, selecionamos a ficha do indicador "
                "COB.2.01 – Taxa de internações hospitalares (SUS) por 100 habitantes, elaborada pelo CGI Cobertura."
            )
        )
        + accordion_row("m2a4fqi-acc", fqi_fields)
        + row(
            box_atencao(
                "<p>O modelo atual de FQI na Ripsa está alinhado ao proposto para o "
                "<strong>Módulo de Gestão de Dados e Indicadores (MGDI)</strong> do Ministério da Saúde (MS). "
                "Trata-se de uma iniciativa que tem como objetivo promover a sistematização, gestão e uso de dados "
                "e indicadores para a saúde pública. O MGDI conta com um modelo próprio de Ficha de Qualificação, "
                "e centraliza o cadastro de indicadores utilizados por gestores de saúde e secretarias do MS.</p>"
            )
        )
        + row_columns(
            p(
                "Consulte a 3ª edição do livro "
                '<a href="https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/" '
                'target="_blank" rel="noopener noreferrer">Indicadores Básicos para a Saúde no Brasil</a>, '
                "conheça as fichas de qualificação de indicadores e aprenda mais sobre a Ripsa. Consulte também as "
                '<a href="https://www.ripsa.org.br/indicadores-basicos-para-a-saude-no-brasil-livro-verde/" '
                'target="_blank" rel="noopener noreferrer">demais edições</a> do chamado “Livro Verde” e outros '
                "produtos da Rede."
            )
            + p(
                "Os indicadores da Ripsa também são publicizados para consulta através do "
                '<a href="https://www.ripsa.org.br/" target="_blank" rel="noopener noreferrer">portal da Ripsa</a>, do '
                '<a href="https://tabnet.datasus.gov.br/" target="_blank" rel="noopener noreferrer">TabNet</a>, da '
                '<a href="https://novasage.saude.gov.br/" target="_blank" rel="noopener noreferrer">SAGE</a> e do '
                '<a href="https://dados.gov.br/dados/conjuntos-dados/sistema-unico-de-saude-sus" target="_blank" '
                'rel="noopener noreferrer">Portal de Dados Abertos do SUS</a>.'
            ),
            (
                f'<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
                f'data-aos-duration="600">'
                f'<img class="img-fluid mx-auto d-block rounded border" '
                f'src="{ASSETS}media/modulo2/mod2-a4-livro-verde-ripsa-3ed.png" '
                f'alt="Capa da 3ª edição do livro Indicadores Básicos para a Saúde no Brasil: conceitos e aplicações" '
                f'loading="lazy" /></figure>'
            ),
        )
        + row(
            box_para_assistir(
                '<p class="mb-3">Assista ao vídeo do Centro de Estudos do Icict que apresentou as principais '
                "estratégias da Ripsa para a disseminação da informação em saúde.</p>"
                '<div class="ratio ratio-16x9"><iframe src="https://www.youtube.com/embed/eSIGDZJzKS8" '
                'title="Estratégias da Ripsa para disseminação da informação em saúde" '
                'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
                'allowfullscreen loading="lazy"></iframe></div>'
            )
        )
    )


def content_topico5() -> str:
    flipcards = flipcard_row(COMPLEMENTARY_FLIPCARDS)
    return (
        row(heading_block("Campos complementares para FQI", small="Tópico 5"))
        + row(
            p(
                "Além dos campos utilizados no modelo da Ripsa, outros campos podem ser úteis para compor uma ficha de "
                "qualificação de indicador. A seleção dos campos deve considerar as necessidades de transparência "
                "metodológica e inteligibilidade, e os usos pretendidos e potenciais usuários das fichas e indicadores. "
                "A seguir são apresentados alguns campos complementares:"
            )
        )
        + flipcards
        + row(
            p(
                "Agora que você já percorreu todo o processo de construção e documentação de indicadores, é hora de seguir "
                "adiante! No próximo módulo, vamos explorar juntos como esses indicadores podem ser usados para o "
                "monitoramento e a avaliação de políticas públicas e de saúde. Você está avançando de forma consistente — "
                "e cada passo amplia ainda mais sua capacidade de compreender, analisar e transformar realidades por meio "
                "da informação em saúde. Vamos em frente?"
            )
        )
    )


REFERENCES = [
    "OPAS. Organização Pan-Americana da Saúde. <strong>Indicadores de saúde. Elementos conceituais e práticos.</strong> Washington, D.C.: OPAS; 2018. Disponível em: <a href=\"https://iris.paho.org/bitstream/handle/10665.2/49057/9789275720059_por.pdf?sequence=5&isAllowed=y\" target=\"_blank\" rel=\"noopener noreferrer\">https://iris.paho.org/bitstream/handle/10665.2/49057/9789275720059_por.pdf?sequence=5&amp;isAllowed=y</a>. Acesso em 18 fevereiro 2026.",
    "REDE Interagencial de Informações para a Saúde. <strong>Indicadores básicos para a saúde no Brasil: conceitos e aplicações</strong> / Rede Interagencial de Informações para a Saúde – Ripsa. – 3.ed. – Brasília: Organização Pan-americana da Saúde, 2026.",
    "RISI JÚNIOR, J. B. Informação em saúde no Brasil: a contribuição da Ripsa. <strong>Ciência &amp; Saúde Coletiva</strong>, v. 11, n. 4, p. 1049–1053, out. 2006. <a href=\"https://doi.org/10.1590/S1413-81232006000400025\" target=\"_blank\" rel=\"noopener noreferrer\">https://doi.org/10.1590/S1413-81232006000400025</a>. Acesso em 18 fevereiro 2026.",
]


def content_topico6() -> str:
    refs = "".join(f'<li class="list-group-item" list-style="default">{ref}</li>' for ref in REFERENCES)
    return (
        row(
            '<div class="referencias-aula">'
            + heading_block("Bibliografia", small="Tópico 6")
            + f'<div class="list"><ul class="list-group">{refs}</ul></div></div>'
        )
    )


CONTENT_BUILDERS = [
    content_topico1,
    content_topico2,
    content_topico3,
    content_topico4,
    content_topico5,
    content_topico6,
]


def topic_nav(current: int) -> str:
    items = []
    for i, title in enumerate(TOPICS, start=1):
        status = 'status="visited"' if i <= current else ""
        aria = "Tópico atual" if i == current else ("Tópico concluído" if i < current else "Tópico não concluído")
        items.append(
            f'<a href="topico{i}.html" tabindex="0" role="link" class="topic-list__item" '
            f'aria-label="{aria}" {status}><span class="material-symbols-rounded"></span>{title}</a>'
        )
    return "\n\t\t\t\t\t\t\t".join(items)


def page_nav(current: int) -> str:
    parts = []
    if current == 1:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="../aula3/topico5.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Aula anterior</a>'
        )
    else:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{current - 1}.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        )
    if current == len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="../../modulo3/aula1/topico1.html" rel="next">'
            f'Módulo 3 <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    else:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{current + 1}.html" rel="next">'
            f'Próximo tópico <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    return (
        '<section><div class="container"><div class="row justify-content-center">'
        f'<div class="col-12 col-md-10 col-lg-8"><div class="page-nav d-flex justify-content-evenly flex-wrap gap-3">'
        f'{"".join(parts)}</div></div></div></div></section>'
    )


def render_page(topic_index: int) -> str:
    current = topic_index + 1
    content = CONTENT_BUILDERS[topic_index]()
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
\t<meta charset="utf-8" />
\t<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=yes" />
\t<meta http-equiv="content-type" content="text/html; charset=utf-8" />
\t<meta name="robots" content="noindex" />
\t<meta name="author" content="Fiocruz, Campus Virtual" />
\t<meta name="description" content="Curso {COURSE_TITLE}" />
\t<link rel="apple-touch-icon" sizes="180x180" href="{ASSETS}media/icons/apple-icon-180x180.png" />
\t<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}media/icons/favicon-32x32.png" />
\t<link rel="manifest" href="../media/icons/manifest.json" />
\t<meta name="theme-color" content="#001833" />
\t<title>Curso {COURSE_TITLE} | Mod {MODULE_NUM} | {AULA_LABEL}</title>
\t<link rel="stylesheet" href="{ASSETS}source/bootstrap-5.1.3/css/bootstrap.min.css" />
\t<link rel="stylesheet" href="{ASSETS}assets/css/style.css" />
</head>
<body>
\t<header class="header">
\t\t<div class="mobile-toggle-open"><a class="mobile-toggle__button" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></div>
\t\t<div class="brand"><img class="img-fluid logo-black" src="{ASSETS}media/logos/header-fiocruz-campus-virtual.png" alt="Campus Virtual Fiocruz" /></div>
\t\t<div class="title"><h1>{COURSE_TITLE}</h1></div>
\t\t<ul class="nav nav-pills">
\t\t\t<li class="nav-item"><a href="{ASSETS}index.html" class="nav-link">Início</a></li>
\t\t\t<li class="nav-item"><a href="#" class="nav-link" data-bs-toggle="modal" data-bs-target="#modal-creditos">Créditos</a></li>
\t\t</ul>
\t</header>
\t<div class="main">
\t\t<div class="sidebar" role="navigation">
\t\t\t<div class="sidebar__inner" style="position: relative">
\t\t\t\t<div class="sidebar__group d-lg-none">
\t\t\t\t\t<div class="sidebar__group-item">
\t\t\t\t\t\t<div class="sidebar__header">
\t\t\t\t\t\t\t<span>Curso</span>
\t\t\t\t\t\t\t<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t\t<div class="sidebar__group-item"><div class="sidebar__title"><h1>{COURSE_TITLE}</h1></div></div>
\t\t\t\t\t<div class="sidebar__group-item">
\t\t\t\t\t\t<ul class="nav">
\t\t\t\t\t\t\t<li class="nav-item"><a href="{ASSETS}index.html" class="nav-link" tabindex="0"><span class="icon material-symbols-rounded" aria-hidden="true">home</span>Início</a></li>
\t\t\t\t\t\t\t<li class="nav-item"><a href="#" class="nav-link" tabindex="0" data-bs-toggle="modal" data-bs-target="#modal-creditos"><span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>Créditos</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t\t<div class="sidebar__group">
\t\t\t\t\t<div class="sidebar__group-item">
\t\t\t\t\t\t<div class="dropend">
\t\t\t\t\t\t\t<button id="dropdown-modulos" type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
\t\t\t\t\t\t\t\t<span class="icon material-symbols-rounded" aria-hidden="true">grid_view</span><span class="label">Módulos</span>
\t\t\t\t\t\t\t</button>
\t\t\t\t\t\t\t<ul class="dropdown-menu" aria-labelledby="dropdown-modulos">
\t\t\t\t\t\t\t\t<li class="d-lg-none dropdown-menu__header">
\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
\t\t\t\t\t\t\t\t\t<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />{MODULE1_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />{MODULE_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="{ASSETS}modulo3/aula1/topico1.html"><strong>Módulo 3</strong><br />Uso de indicadores</a></li>
\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t\t<div class="divider"><hr /></div>
\t\t\t\t<div class="sidebar__group">
\t\t\t\t\t<div class="sidebar__group-item"><span class="text module">Módulo <br class="d-none d-lg-block" /><span>{MODULE_NUM}</span></span></div>
\t\t\t\t\t<div class="sidebar__group-item">
\t\t\t\t\t\t<div class="dropend">
\t\t\t\t\t\t\t<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
\t\t\t\t\t\t\t\t<span class="icon material-symbols-rounded" aria-hidden="true">apps</span><span class="label">Conteúdo</span>
\t\t\t\t\t\t\t</button>
\t\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t\t<li class="d-lg-none dropdown-menu__header">
\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
\t\t\t\t\t\t\t\t\t<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__title"><span class="label">Módulo {MODULE_NUM}</span><span class="title">{MODULE_TITLE}</span></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA1_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>{AULA2_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula3/topico1.html"><strong>Aula 3: </strong>{AULA3_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="topico1.html"><strong>Aula 4: </strong>{AULA_TITLE}</a></li>
\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t\t<div class="divider"><hr /></div>
\t\t\t\t<div class="sidebar__group">
\t\t\t\t\t<div class="sidebar__group-item"><span class="text class">{AULA_LABEL}</span></div>
\t\t\t\t\t<div class="sidebar__group-item">
\t\t\t\t\t\t<div class="dropend">
\t\t\t\t\t\t\t<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
\t\t\t\t\t\t\t\t<span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span><span class="label">Tópicos</span>
\t\t\t\t\t\t\t</button>
\t\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t\t<li class="d-lg-none dropdown-menu__header">
\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
\t\t\t\t\t\t\t\t\t<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__title"><span class="label">{AULA_LABEL}</span><span class="title">{AULA_TITLE}</span></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><nav class="topic-list">
\t\t\t\t\t\t\t{topic_nav(current)}
\t\t\t\t\t\t\t</nav></li>
\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>
\t\t<div class="content">
\t\t\t<div id="page-title"><div class="container"><div class="row align-items-center hstify-content-center justify-content-xxl-start ms-lg-5"><div class="col-12 col-md-10 col-lg-11"><h2 class="title"><span class="label">Módulo {MODULE_NUM} | {AULA_LABEL}</span><br />{AULA_TITLE}</h2></div></div></div></div>
\t\t\t<div id="page-content" class="">
\t\t\t\t<section><div class="container">
{content}
\t\t\t\t</div></section>
\t\t\t</div>
\t\t\t{page_nav(current)}
\t\t</div>
\t\t<footer>
\t\t\t<div class="container-fluid">
\t\t\t\t<div class="row justify-content-center align-items-center linha-de-marcas">
\t\t\t\t\t<div class="col-12 text-center py-3">
\t\t\t\t\t\t<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: Campus Virtual Fiocruz, Fiocruz, SUS Digital, SUS 35 Anos, Ministério da Saúde e Governo do Brasil" />
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</footer>
\t</div>
\t<script src="{ASSETS}source/bootstrap-5.1.3/js/bootstrap.bundle.min.js"></script>
\t<script type="text/javascript" src="{ASSETS}assets/js/ResizeSensor.js"></script>
\t<script type="text/javascript" src="{ASSETS}assets/js/sticky-sidebar.js"></script>
\t<script type="text/javascript" src="{ASSETS}assets/js/sidebar.js"></script>
\t<script type="text/javascript">var sidebar = new StickySidebar(".sidebar", {{ topSpacing: 0, bottomSpacing: 0, containerSelector: ".main", innerWrapperSelector: ".sidebar__inner", minWidth: 991 }});</script>
\t<script type="text/javascript" src="{ASSETS}assets/js/scripts.js"></script>
\t<script type="text/javascript" src="{ASSETS}assets/js/custom-anime.js"></script>
\t<script type="text/javascript" src="{ASSETS}source/animate/aos/dist/aos.js"></script>
\t<script>AOS.init();</script>
</body>
</html>
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i in range(len(TOPICS)):
        path = OUT_DIR / f"topico{i + 1}.html"
        path.write_text(render_page(i), encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
