#!/usr/bin/env python3
"""Gera HTML da Aula 2.3 (Módulo 2) — Índices: conceitos, construção e usos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula3"
ASSETS = "../../"

COURSE_TITLE = "Indicadores para a saúde: aspectos teóricos e práticos"
MODULE_NUM = 2
MODULE_TITLE = "Calculando indicadores"
MODULE1_TITLE = "Conceitos básicos em indicadores para a saúde"
AULA1_TITLE = "Dados, medidas e indicadores: valores absolutos e relativos"
AULA2_TITLE = "Medidas relativas para a análise de dados de saúde"
AULA_LABEL = "Aula 3"
AULA_TITLE = "Índices: conceitos, construção e usos"
AULA4_TITLE = "Ficha de Qualificação de Indicadores"

TOPICS = [
    "Sobre esta aula",
    "O que é um índice?",
    "Como construir um índice?",
    "Vantagens e desvantagens no uso de índices",
    "Referências",
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


def box_saiba_mais(body: str, *, collapse_id: str = "m2a3sm1") -> str:
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


def quotation(text: str, author: str) -> str:
    return (
        f'<div class="quotation"><blockquote><div class="quotation-body">'
        f'<span class="quotation-mark fa1"></span>'
        f"<p><em>{text}</em></p>"
        f'<span class="quotation-autor">{author}</span></div>'
        f'<span class="quotation-mark fa2"></span></blockquote></div>'
    )


OCDE_STEPS = [
    (
        "m2a3fc1",
        "1. Quadro teórico",
        "<p class='mb-0'>É o ponto de partida, onde se define o fenômeno social a ser medido e seus subcomponentes. Serve de base para a seleção de variáveis e pesos, garantindo que o indicador tenha uma fundamentação sólida e seja adequado ao seu propósito.</p>",
    ),
    (
        "m2a3fc2",
        "2. Seleção de dados",
        "<p class='mb-0'>Os indicadores individuais devem ser escolhidos com base na sua solidez analítica, mensurabilidade, relevância e cobertura. Deve-se verificar a qualidade dos dados disponíveis e documentar as suas potencialidades e limitações.</p>",
    ),
    (
        "m2a3fc3",
        "3. Imputação de dados em falta",
        "<p class='mb-0'>Para obter um conjunto de dados completo, às vezes é necessário estimar os valores ausentes. Isso pode ser feito através de variados métodos de imputação, sendo crucial analisar o impacto dessas estimativas no resultado final.</p>",
    ),
    (
        "m2a3fc4",
        "4. Análise multivariada",
        "<p class='mb-0'>Serve para investigar a estrutura estatística do conjunto de dados e avaliar se os indicadores selecionados descrevem bem o fenômeno. Técnicas como a análise de componentes principais (PCA) ajudam a identificar grupos de indicadores semelhantes e a guiar escolhas metodológicas posteriores.</p>",
    ),
    (
        "m2a3fc5",
        "5. Normalização",
        "<p class='mb-0'>Como os indicadores costumam ter unidades de medida diferentes, a normalização é necessária para torná-los comparáveis, garantindo a coerência. Métodos comuns incluem o ranking, a padronização (z-scores) e o método Min-Max.</p>",
    ),
    (
        "m2a3fc6",
        "6. Ponderação e agregação",
        "<p class='mb-0'>Os indicadores são combinados seguindo o quadro teórico estabelecido. É nesta fase que se decide o peso de cada componente e o método de agregação (como o linear ou geométrico), considerando se um bom desempenho numa dimensão pode compensar falhas em outra. Essa fase pode afetar a interpretabilidade do indicador.</p>",
    ),
    (
        "m2a3fc7",
        "7. Análise de robustez e sensibilidade",
        "<p class='mb-0'>Avalia como as escolhas feitas nas etapas anteriores (normalização, pesos, agregação) afetam as classificações finais das diferentes unidades de análise (como municípios ou países). Ajuda a garantir a transparência e a credibilidade do indicador.</p>",
    ),
    (
        "m2a3fc8",
        "8. Retorno aos dados",
        "<p class='mb-0'>O indicador composto deve ser decomposto para identificar o que define o desempenho de cada unidade de análise.</p>",
    ),
    (
        "m2a3fc9",
        "9. Relação com outros indicadores",
        "<p class='mb-0'>Tenta-se correlacionar o novo indicador composto com outras medidas conhecidas (como o PIB per capita, por exemplo) para testar o seu poder explicativo e desenvolver narrativas baseadas nos dados.</p>",
    ),
    (
        "m2a3fc10",
        "10. Apresentação e visualização",
        "<p class='mb-0'>Os resultados devem ser apresentados de forma clara, acessível e precisa, utilizando ferramentas como tabelas e gráficos.</p>",
    ),
]


def content_topico1() -> str:
    return (
        row(heading_block("Sobre esta aula", small="Tópico 1"))
        + row(
            p("Seja bem-vindo e bem-vinda! Seja bem-vindo e bem-vinda à aula “<strong>Índices: conceitos, construção e usos</strong>”."),
            p(
                "Nas duas últimas aulas, abordamos processos de construção de indicadores simples. Nessa aula, você será apresentado(a) aos indicadores compostos, também chamados de índices."
            ),
        )
        + row(
            p("Ao final dessa aula, você será capaz de:"),
            list_group(
                [
                    "Conhecer o conceito de índice;",
                    "Conhecer as etapas de construção de um índice;",
                    "Conhecer exemplos de índices;",
                    "Apreender vantagens e desvantagens uso de índices.",
                ]
            ),
        )
        + row_mb4(heading_block("Autoria", tag="h4"))
        + row(
            p("<strong>Carolina de Campos Carvalho</strong>"),
            p(
                "Doutora e Mestre em Saúde Pública, Analista Técnica de Políticas Sociais. Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da Fundação Oswaldo Cruz (Fiocruz)."
            ),
            p("<strong>Aline Pinto Marques</strong>"),
            p(
                "Doutora em Epidemiologia em Saúde Pública. Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da Fundação Oswaldo Cruz (Fiocruz)."
            ),
        )
    )


def content_topico2() -> str:
    return (
        row(heading_block("O que é um índice?", small="Tópico 2"))
        + row(
            p(
                "Os índices são também chamados de <strong>indicadores compostos</strong> ou <strong>indicadores sintéticos</strong>. "
                "São calculados a partir da combinação de dois ou mais indicadores simples de uma mesma dimensão ou de mais de uma dimensão social, sintetizados em uma única medida."
            ),
            p(
                "Para o cálculo de um índice é aplicado um método de aglutinação que pode incluir a definição de pesos diferentes aos componentes e variáveis das dimensões selecionadas."
            ),
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig1-construcao-indice.png",
                "Diagrama com três indicadores entrando em um funil de método de aglutinação e resultando em um índice.",
                "Fonte: Elaboração própria, a partir de Jannuzzi, 2024.",
                strong_caption="Figura 1 – Construção de um índice.",
            )
        )
    )


def content_topico3() -> str:
    flipcards = flipcard_row(OCDE_STEPS)
    return (
        row(heading_block("Como construir um índice?", small="Tópico 3"))
        + row(
            p(
                "O guia para construção de indicadores compostos da Organização para a Cooperação e Desenvolvimento Econômico (OCDE) define uma sequência de 10 etapas para a construção de um índice, que vão desde o desenvolvimento do quadro teórico até a disseminação dos resultados. São elas:"
            )
        )
        + flipcards
        + row(
            p(
                "A qualidade do índice resultante desse processo irá depender de dois pilares: i) da qualidade dos indicadores individuais que o compõem, e ii) da qualidade nos procedimentos de construção e disseminação. O primeiro pilar foi abordado quando aprofundamos os atributos desejáveis dos indicadores. O segundo refere-se à necessidade de uma metodologia tecnicamente rigorosa e transparente ao longo de todas as etapas de construção."
            )
        )
        + row_mb4(heading_block("Exemplos de índices", tag="h4"))
        + row(
            p(
                "A seguir, abordaremos a construção e interpretação de dois índices amplamente divulgados: o Índice de Desenvolvimento Humano (IDH) e o Índice de Vulnerabilidade Social."
            )
        )
        + row_mb4(heading_block("O Índice de Desenvolvimento Humano (IDH)", tag="h5"))
        + row(
            p(
                "O IDH é um índice amplamente conhecido e utilizado internacionalmente. Foi criado em 1990, como um contraponto ao uso do indicador Produto Interno Bruto (PIB) per capita como indicador de desenvolvimento, pois este considera apenas a dimensão econômica do desenvolvimento. Baseado em um <strong>conceito de desenvolvimento centrado nas escolhas e bem-estar das pessoas</strong>, o IDH apresenta uma visão mais abrangente do bem-estar, por considerar não apenas fatores econômicos, mas também sociais. É uma medida calculada a partir de três dimensões básicas do desenvolvimento humano: <strong>saúde, educação e renda</strong>."
            ),
            p(
                "Posteriormente, essa metodologia foi adequada ao contexto brasileiro e à disponibilidade de indicadores para avaliar o desenvolvimento dos municípios e regiões metropolitanas brasileiras, resultando no IDHM brasileiro, que é composto pelas mesmas três dimensões do IDH Global (PNUD, 2013). Os resultados do IDHM e dos indicadores que o compõem estão disponíveis na página do <a href=\"http://www.atlasbrasil.org.br/\" target=\"_blank\" rel=\"noopener noreferrer\">Atlas do Desenvolvimento Humano</a>."
            ),
        )
        + row(
            box_para_assistir(
                "<p class=\"mb-3\">Assista ao vídeo para conhecer mais sobre o IDHM e as ferramentas disponíveis no Atlas do Desenvolvimento Humano.</p>"
                "<p class=\"mb-3\"><em>Link do vídeo a ser inserido.</em></p>"
                "<p class=\"mb-0\">Visite também o <a href=\"http://www.atlasbrasil.org.br/\" target=\"_blank\" rel=\"noopener noreferrer\">Painel IDHM do PNUD</a>.</p>"
            )
        )
        + row(
            p(
                "O IDHM utiliza quatro indicadores referentes às três dimensões analisadas. São eles: expectativa de vida ao nascer, escolaridade da população adulta, fluxo escolar da população jovem e renda per capita. É calculada a média geométrica das três dimensões para se chegar ao índice final."
            ),
            p(
                "O resultado do IDHM varia de 0 a 1; e quanto mais próximo a 1, maior o desenvolvimento humano. São cinco faixas de desenvolvimento humano: muito baixo (0-0,499), baixo (0,500-0,599), médio (0,600-0,699), alto (0,700-0,799) e muito alto (0,800-1). Veja na figura abaixo como ler o índice:"
            ),
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig2-como-ler-idhm.png",
                "Escala horizontal de 0 a 1 com cinco faixas coloridas de desenvolvimento humano: muito baixo, baixo, médio, alto e muito alto.",
                "Fonte: Elaborado a partir de PNUD, 2013.",
                strong_caption="Figura 2 – Como ler o IDHM.",
            )
        )
        + row(
            p(
                "Na tabela abaixo, temos o resultado do IDHM 2010 para o Brasil e o município do Rio de Janeiro (RJ). Ambos estão na faixa de alto desenvolvimento humano. Podemos verificar, contudo, que o desenvolvimento humano do país, no que se refere à dimensão Educação, é médio. O município do Rio de Janeiro também apresentou o menor resultado nessa dimensão."
            )
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig3-idhm-2010-br-rj.jpg",
                "Tabela com IDHM e dimensões de renda, longevidade e educação para Brasil e Rio de Janeiro em 2010.",
                "Fonte: Atlas do Desenvolvimento Humano. Consulta em 22 de fevereiro de 2026.",
                strong_caption="Figura 3 – IDHM 2010, Brasil e Rio de Janeiro (RJ).",
            )
        )
        + row(
            p(
                "Agora consulte o <a href=\"http://www.atlasbrasil.org.br/\" target=\"_blank\" rel=\"noopener noreferrer\">Atlas do Desenvolvimento Humano</a> e veja o resultado do IDHM e de suas subdimensões para o seu município de residência. O desenvolvimento humano de seu município está em qual faixa? Qual dimensão está mais desenvolvida? E qual está menos?"
            )
        )
        + row_mb4(heading_block("O Índice de Vulnerabilidade Social (IVS)", tag="h5"))
        + row(
            p(
                "Outro índice bastante conhecido é o IVS, elaborado pelo Instituto de Pesquisa Econômica Aplicada (Ipea) e instituições parceiras. O IVS é obtido pelo cálculo da média aritmética dos subíndices: IVS Infraestrutura Urbana, IVS Capital Humano e IVS Renda e Trabalho, cada um deles com o mesmo peso."
            ),
            p(
                "No quadro a seguir, são apresentados os indicadores que compõem os subíndices e seus respectivos pesos:"
            ),
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig4-ivs-indicadores-pesos.png",
                "Tabela com dimensões do IVS, indicadores componentes e pesos de cada indicador.",
                "Fonte: Ipea, 2018, p. 25.",
                strong_caption="Figura 4 – Indicadores que compõem os subíndices do IVS e pesos.",
            )
        )
        + row(
            p(
                "Assim como o IDH, os resultados do IVS são expressos em uma escala de 0 a 1 com três casas decimais, classificados também em cinco faixas correspondentes a graus de vulnerabilidade. Contudo, em um sentido de interpretação inverso: quanto mais próximo de 1, maior a vulnerabilidade social."
            )
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig5-como-ler-ivs.jpg",
                "Escala horizontal de 0 a 1 com cinco faixas coloridas de vulnerabilidade social: muito baixa, baixa, média, alta e muito alta.",
                "Fonte: Elaborado a partir de Ipea, Atlas da Vulnerabilidade Social.",
                strong_caption="Figura 5 – Como ler o IVS.",
            )
        )
        + row(
            p(
                "Na figura a seguir, podemos ver comparativamente os municípios brasileiros segundo desenvolvimento humano (IDHM) e vulnerabilidade social (IVS)."
            )
        )
        + row(
            figure(
                "media/modulo2/mod2-a3-fig8-comparativo-idhm-ivs.jpg",
                "Dois mapas do Brasil comparando faixas do IDHM e do IVS por município em 2010.",
                "Fonte: Ipea, 2018, p. 31.",
                strong_caption="Figura 8 – Municípios segundo faixas do IDHM e do IVS, 2010.",
            )
        )
        + row(
            p(
                "Acesse também a plataforma do "
                '<a href="http://ivs.ipea.gov.br/" target="_blank" rel="noopener noreferrer">Atlas da Vulnerabilidade Social</a> '
                "para consultar o Índice de Vulnerabilidade Social do seu município e comparar os resultados com o IDHM."
            )
        )
    )


def content_topico4() -> str:
    quote = (
        "Não são os indicadores sintéticos que responderão às perguntas dos gestores "
        "para aprimoramento das políticas e programas. São indicadores mais específicos, "
        "referidos a aspectos particulares dos componentes dos programas que fornecerão as pistas "
        "para aprimorá-los. Assim como o estado de saúde de uma pessoa adulta não pode ser inferido "
        "somente com base na regularidade de seu peso ou da ausculta de seu coração – mesmo que por estetoscópio – "
        "a avaliação do nível de desenvolvimento, do bem-estar ou pobreza em sua multidimensionalidade "
        "não pode ser encapsulada em uma só medida."
    )
    return (
        row(heading_block("Vantagens e desvantagens no uso de índices", small="Tópico 4"))
        + row_mb4(heading_block("na gestão e avaliação de políticas públicas", tag="h5"))
        + row(
            p(
                "A partir dos exemplos do IDHM e do IVS, pode-se perceber que, entre as possíveis vantagens do uso de índices, está a sintetização de múltiplas informações, a facilitação da comparabilidade dos resultados, e a maior facilidade de interpretação em relação ao uso de uma diversidade de indicadores simples, e o estímulo do interesse público."
            ),
            p(
                "Em contraposição às vantagens, há uma vasta literatura criticando o uso de índices na gestão de políticas públicas, por razões como falta de especificidade; potencial falta de sensibilidade a mudanças de seus componentes e pesos; dificuldade de validação e arbitrariedade da seleção de variáveis e pesos; excesso de reducionismo; entre outros aspectos metodológicos e de uso (Fribel; Steventon, 2018; Valente, 2002; OECD, 2008). Para além das desvantagens apontadas, a seleção de indicadores para compor um índice e a definição dos pesos dos componentes também pode ser alvo de disputas políticas e de mau uso."
            ),
            p(
                "Os índices são também passíveis de críticas quanto ao seu uso como critério de priorização de determinadas localidades na implementação de políticas públicas (Carvalho et al., 2023), como, por exemplo, na hipotética situação de destinação de mais recursos orçamentários para municípios com piores Índices de Desenvolvimento Humano Municipal (Guimarães; Jannuzzi, 2005)."
            ),
            p("Essa crítica foi reforçada por Jannuzzi (2024), que argumenta que:"),
        )
        + row(quotation(quote, "(JANNUZZI, 2024, P.167)"))
        + row(
            box_saiba_mais(
                "<p class=\"mb-0\">Leia o artigo "
                '<a href="https://doi.org/10.22296/2317-1529.2005v7n1p73" target="_blank" rel="noopener noreferrer">'
                "“IDH, indicadores sintéticos e suas aplicações em políticas públicas: uma análise crítica”</a>. "
                "Essa leitura ajudará você a aprofundar a compreensão sobre os desafios e potenciais usos dos indicadores sintéticos "
                "no planejamento e avaliação de políticas públicas.</p>"
            )
        )
    )


REFERENCES = [
    "ALBUQUERQUE C, MARTINS M. Indicadores de desempenho no Sistema Único de Saúde: uma avaliação dos avanços e lacunas. <strong>Saúde em Debate</strong>; 41(n. spe): 118-137, 2017.",
    "BRASIL. Ministério da Saúde. <strong>IDSUS: Índice de Desempenho do Sistema Único de Saúde. Ano 1.</strong> Brasília: Ministério da Saúde, 2014, 50 pp. Disponível em: <a href=\"http://idsus.saude.gov.br/documentos/IDSUS_Texto_Base_13-03-14.pdf\" target=\"_blank\" rel=\"noopener noreferrer\">http://idsus.saude.gov.br/documentos/IDSUS_Texto_Base_13-03-14.pdf</a>. Acesso em 22 fevereiro 2026.",
    "CARVALHO, C.C.; et al. Análise comparativa de classificações de vulnerabilidade para municípios g100. <strong>Revista Brasileira de Estudos de População - REBEP</strong>, v. 40, p. 1-20, 2023. Disponível em: <a href=\"https://www.scielo.br/j/rbepop/a/x3WRtg5F7LyLwtgszQtxhxx/?format=html&lang=pt#\" target=\"_blank\" rel=\"noopener noreferrer\">https://www.scielo.br/j/rbepop/a/x3WRtg5F7LyLwtgszQtxhxx/?format=html&lang=pt#</a>. Acesso em 22 fevereiro 2026.",
    "CEBES - Centro Brasileiro de Estudos de Saúde. Divulgação do Índice de Desempenho do SUS repercute na academia. 7 de mar. de 2012. Disponível em: <a href=\"https://cebes.org.br/divulgacao-do-indice-de-desempenho-do-sus-repercute-naacademia/10482/\" target=\"_blank\" rel=\"noopener noreferrer\">https://cebes.org.br/divulgacao-do-indice-de-desempenho-do-sus-repercute-naacademia/10482/</a>. Acesso em 22 fevereiro 2026.",
    "FRIEBEL, R.; STEVENTON, A. Composite measures of healthcare quality: sensible in theory, problematic in practice. <strong>BMJ Qual Saf.</strong> Editorial, 17 set. 2018. Disponível em: <a href=\"https://qualitysafety.bmj.com/content/early/2018/09/16/bmjqs-2018-008280.info\" target=\"_blank\" rel=\"noopener noreferrer\">https://qualitysafety.bmj.com/content/early/2018/09/16/bmjqs-2018-008280.info</a>. Acesso em 22 fevereiro 2026.",
    "GUIMARÃES, J. R. S.; JANNUZZI, P. IDH, indicadores sintéticos e suas aplicações em políticas públicas: uma análise crítica. <strong>Revista Brasileira De Estudos Urbanos E Regionais</strong>, 7(1), 73, 2005. <a href=\"https://doi.org/10.22296/2317-1529.2005v7n1p73\" target=\"_blank\" rel=\"noopener noreferrer\">https://doi.org/10.22296/2317-1529.2005v7n1p73</a>. Acesso em 22 fevereiro 2026.",
    "IPEA - Instituto de Pesquisa Econômica Aplicada. <strong>Atlas da Vulnerabilidade Social.</strong> Disponível em: <a href=\"http://ivs.ipea.gov.br/\" target=\"_blank\" rel=\"noopener noreferrer\">http://ivs.ipea.gov.br/</a>. Acesso em 22 fevereiro 2026.",
    "IPEA - Instituto de Pesquisa Econômica Aplicada. Vulnerabilidade social no Brasil: conceitos, métodos e primeiros resultados para municípios e regiões metropolitanas brasileiras. <strong>Texto para discussão 2364</strong> / Instituto de Pesquisa Econômica Aplicada. Brasília, Rio de Janeiro: Ipea, 2018. ISSN 1415-4765. Disponível em: <a href=\"https://ivs.ipea.gov.br/api/cockpit/storage/uploads/publicacoes/td_2364b.pdf\" target=\"_blank\" rel=\"noopener noreferrer\">https://ivs.ipea.gov.br/api/cockpit/storage/uploads/publicacoes/td_2364b.pdf</a>. Acesso em 22 fevereiro 2026.",
    "JANNUZZI, Paulo de Martino. <strong>Indicadores sociais no Brasil.</strong> Campinas, SP: Editora Alínea, 2017. 6a. Edição, 3a. Impressão, 2024.",
    "OECD. <strong>Handbook on Constructing Composite Indicators: methodology and user guide.</strong> OECD, 2008. Disponível em: <a href=\"https://www.oecd.org/els/soc/handbookonconstructingcompositeindicatorsmethodologyanduserguide.htm\" target=\"_blank\" rel=\"noopener noreferrer\">https://www.oecd.org/els/soc/handbookonconstructingcompositeindicatorsmethodologyanduserguide.htm</a>. Acesso em 22 fevereiro 2026.",
    "OLIVEIRA, L.; PASSADOR, C. Considérations sur l'indice de performance du Système unique de santé (SUS) au Brésil. <strong>Santé Publique</strong>, vol. 26, p. 829-836, 2014. Disponível em: <a href=\"https://www.cairn.info/revue-sante-publique-2014-6-page829.htm\" target=\"_blank\" rel=\"noopener noreferrer\">https://www.cairn.info/revue-sante-publique-2014-6-page829.htm</a>. Acesso em: 22 fevereiro 2026.",
    "PNUD – Programa das Nações Unidas para o Desenvolvimento. <strong>Atlas do Desenvolvimento Humano no Brasil.</strong> Disponível em: <a href=\"http://www.atlasbrasil.org.br/\" target=\"_blank\" rel=\"noopener noreferrer\">http://www.atlasbrasil.org.br/</a>. Acesso em 22 fevereiro 2026.",
    "PNUD – Programa das Nações Unidas para o Desenvolvimento. <strong>O Índice de Desenvolvimento Humano Municipal Brasileiro.</strong> Série Atlas do Desenvolvimento Humano no Brasil. Brasília: PNUD, Ipea, FJP, 2013. ISBN: 978-85-7811-171-7. Disponível em: <a href=\"http://www.atlasbrasil.org.br/acervo/biblioteca\" target=\"_blank\" rel=\"noopener noreferrer\">http://www.atlasbrasil.org.br/acervo/biblioteca</a>. Acesso em 22 fevereiro 2026.",
]


def content_topico5() -> str:
    refs = "".join(f'<li class="list-group-item" list-style="default">{ref}</li>' for ref in REFERENCES)
    return (
        row(
            '<div class="referencias-aula">'
            + heading_block("Referências", small="Tópico 5")
            + f'<div class="list"><ul class="list-group">{refs}</ul></div></div>'
        )
    )


CONTENT_BUILDERS = [
    content_topico1,
    content_topico2,
    content_topico3,
    content_topico4,
    content_topico5,
]


def topic_nav(current: int) -> str:
    items = []
    for i, title in enumerate(TOPICS, start=1):
        status = 'status="visited"' if i < current else ('status="visited"' if i == current else "")
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
            f'<a class="fio-button fio-button-primary" href="../aula2/topico5.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Aula anterior</a>'
        )
    else:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{current - 1}.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        )
    if current == len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="../aula4/topico1.html" rel="next">'
            f'Próxima aula <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
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
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="topico1.html"><strong>Aula 3: </strong>{AULA_TITLE}</a></li>
\t\t\t\t\t\t\t\t<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula4/topico1.html"><strong>Aula 4: </strong>{AULA4_TITLE}</a></li>
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
    for orphan in range(len(TOPICS) + 1, 20):
        path = OUT_DIR / f"topico{orphan}.html"
        if path.exists():
            path.unlink()
            print(f"Removed {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
