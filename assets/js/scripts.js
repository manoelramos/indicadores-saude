// Stick Header

window.addEventListener("scroll", function () {
	const header = document.querySelector(".header");
	const titleHeight = document.querySelector(".header").scrollHeight;

	if (window.scrollY > 150) {
		header.classList.add("header--sticky");
	} else {
		header.classList.remove("header--sticky");
	}
});

// Popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	return new bootstrap.Popover(popoverTriggerEl);
});

// //Swiper (inicialização)

// //Type 1: Swiper Navigation
// var swiper = new Swiper('.swiper--navigation', {
// 	direction: 'horizontal',
// 	loop: false,
// 	slidesPerView: 1,
// 	spaceBetween: 30,

// 	//Mousewheel control
// 	mousewheel: true,

// 	//Keyboard control
// 	keyboard: {
// 		enabled: true,
// 	},

// 	// Navigation arrows
// 	navigation: {
// 		nextEl: '.swiper-button-next',
// 		prevEl: '.swiper-button-prev',
// 	},

// 	//Pagination (if needed)
// 	pagination: {
// 		el: '.swiper-pagination',
// 		clickable: true,
// 		type: 'bullets',
// 	},

// 	// Scrollbar (if needed)
// 	scrollbar: {
// 		el: '.swiper-scrollbar',
// 	},
// });

//Type 2: Swiper Vertical
// var swiperVertical = new Swiper('.swiper--vertical', {
// 	direction: 'vertical',
// 	slidesPerView: 1,
// 	spaceBetween: 0,
// 	mousewheel: true,
// 	pagination: {
// 		el: '.swiper-pagination2',
// 		clickable: true,
// 	},
// });

// //Type 3: Effect Card
// var swiperVertical = new Swiper('.swiper--effect-card', {
// 	effect: 'cards',
// 	grabCursor: true,
// 	pagination: {
// 		el: '.swiper-pagination3',
// 		clickable: true,
// 	},
// });

// Botão de copiar podcast

const copyButton = document.querySelectorAll(".copy-to-clip");

copyButton.forEach((btn) => {
	btn.addEventListener("click", () => {
		copyToClipboard(btn);
		// tooltipShow(btn);

		tooltipFeedback(btn);
	});
});

function copyToClipboard(e) {
	const textToCopy = e.getAttribute("data-link");
	const textarea = document.createElement("textarea");
	textarea.setAttribute("readonly", "");
	textarea.style.position = "absolute";
	textarea.value = textToCopy;
	document.body.appendChild(textarea);
	textarea.select();
	document.execCommand("copy");
	document.body.removeChild(textarea);
}
function tooltipFeedback(b) {
	let feedback = $('[data-toggle="tooltip"]');

	// feedback.tooltip('show');

	b.addEventListener("mouseout", () => {
		feedback.tooltip("hide");
	});
}

// Lightbox (insert the class "lightbox" into <figure>)

const imageToLightbox = document.querySelectorAll(".lightbox");
// const lightboxImage = imageToLightbox.querySelector("img");

console.log(imageToLightbox);

imageToLightbox.forEach((image) => {
	image.addEventListener("click", () => {
		if (!image.classList.contains("lightbox--show")) {
			const getImage = image.querySelector("img");
			const getImageSrc = getImage.getAttribute("src");
			const imageLightbox = document.createElement("div");

			imageLightbox.classList.add("lightbox__image");

			document.body.appendChild(imageLightbox);
			imageLightbox.innerHTML = `<img src="${getImageSrc}"/>`;
			console.log(getImageSrc);

			image.classList.add("lightbox--show");

			document.body.style.overflow = "hidden";
			document.body.style.userSelect = "none";

			closeLightbox(imageLightbox);
		}

		function closeLightbox(e) {
			const lightboxOpen = document.querySelector(".lightbox__image");
			e.addEventListener("click", () => {
				document.body.removeChild(e);
				image.classList.remove("lightbox--show");
				document.body.style.overflow = "auto";
				document.body.style.userSelect = "auto";
			});
		}
	});
});

// Boxes - inserir o título de acordo com o atributo

const boxes = document.querySelectorAll(".box");

boxes.forEach((box) => {
	const boxAttribute = box.getAttribute("data-box");

	const boxLabel = box.querySelector(".label");

	boxLabel.innerHTML = boxAttribute;
});

// Modal - Criação dos modais principais

const modalInfos = {
	creditos: {
		ariaLabel: "creditos",
		modalSize: "modal-lg",
		modalTitle: "Créditos",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-10 col-lg-10">
					<span class="h5 mb-3 d-block">Ministério da Saúde</span>

					<div class="mb-5">
						<p class="mb-1">Alexandre Padilha</p>
						<p class="small text-muted"><em>Ministro</em></p>
					</div>

					<span class="h5 mb-3 d-block">Fundação Oswaldo Cruz – Fiocruz</span>
					
					<div class="mb-5">
						<p class="mb-1">Mario Moreira</p>
						<p class="small text-muted"><em>Presidente</em></p>
						<p class="mb-1">Marly Cruz</p>
						<p class="small text-muted"><em>Vice-Presidência de Educação, Informação e Comunicação (VPEIC)</em></p>
					</div>

					<span class="h5 mb-3 d-block">Campus Virtual Fiocruz</span>

					<div class="mb-5">

						<p class="mb-1">Ana Cristina da Matta Furniel</p>
						<p class="small text-muted"><em>Coordenadora geral</em></p>

						<p class="mb-1">Rosane Mendes</p>
						<p class="small text-muted"><em>Coordenadora adjunta</em></p>
						
						<p class="mb-1">Renata Bernardes David</p>
						<p class="small text-muted"><em>Coordenadora de produção</em></p>

						<p class="mb-1">Juliana Dutra</p>
						<p class="small text-muted"><em>Gerente de produção</em></p>

						<p class="mb-1">Isabela Schincariol</p>
						<p class="small text-muted"><em>Assessora de comunicação</em></p>
					
						<p class="mb-1">Roberta Saboya</p>
						<p class="small text-muted"><em>Designer Educacional</em></p>

						<p class="mb-1">Pilar Tavares Veras Florentino</p>
						<p class="small text-muted"><em>Consultora técnico-pedagógico</em></p>
					
						<span class="h6 mb-3 d-block">Design de Interface</span>
						
						<p class="mb-1">Aline Polycarpo</p>
						<p class="small text-muted"><em>UX/UI Designer</em></p>
						<p class="mb-1">Danilo Blum</p>
						<p class="small text-muted"><em>UX/UI Designer e Front-end</em></p>
						<p class="mb-1">Luciana Nunes</p>
						<p class="small text-muted"><em>UX/UI Designer</em></p>
						
						<span class="h6 mb-3 d-block">Recursos Audiovisuais</span>

						<p class="mb-1">Bruno Athaydes</p>
						<p class="small text-muted"><em>Editor audiovisual</em></p>
			
						<p class="mb-1">Teo Venerando</p>
						<p class="small text-muted"><em>Editor audiovisual</em></p>
			
						<span class="h6 mb-3 d-block">Recursos Educacionais</span>
						
						<p class="mb-1">Carmélia Brito</p>
						<p class="small text-muted"><em>Bibliotecária</em></p>

						<p class="mb-1">Natália Rasina</p>
						<p class="small text-muted"><em>Audiodescrição</em></p>

						<p class="mb-1">Janaina Vieira</p>
						<p class="small text-muted"><em>Revisão de português</em></p>


						<span class="h6 mb-3 d-block">Suporte Técnico de Tecnologia da Informação</span>
					
						<p class="mb-1">Bruno Alexandre de Oliveira</p>
						<p class="small text-muted"><em>Desenvolvedor</em></p>

						<p class="mb-1">Eduardo Xavier da Silva</p>
						<p class="small text-muted"><em>Desenvolvedor</em></p>

						<p class="mb-1">Adriano Lourenço</p>
						<p class="small text-muted"><em>Analista de Tecnologias Educacionais</em></p>

						<p class="mb-1">Orlando Terra</p>
						<p class="small text-muted"><em>Analista de Tecnologias Educacionais</em></p>

						<p class="mb-1">Fábio Carneiro</p>
						<p class="small text-muted"><em>Designer gráfico e web designer</em></p>
					</div>

					<span class="h5 mb-3 d-block">Coordenação Acadêmica</span>
					
					<div class="mb-5">
						<p class="mb-1">Alexandra Ribeiro Mendes de Almeida</p>
						<p class="small text-muted mb-0"><em>Programa de Computação Científica (PROCC) – Fiocruz</em></p>
						<p class="small text-muted"><em>Coordenadora</em></p>

						<p class="mb-1">Carlos Antonio de Souza Teles Santos</p>
						<p class="small text-muted mb-0"><em>Centro de Integração de Dados e Conhecimentos para Saúde (CIDACS) – Fiocruz Bahia</em></p>
						<p class="small text-muted"><em>Coordenador</em></p>


						<span class="h6 mb-3 d-block">Conteudistas</span>
						
						<p class="mb-1"><strong>Módulo 1: Lógica e Linguagem de Programação</strong></p>
						
						<p class="mb-1">Juracy Bertoldo</p>
						<p class="small text-muted mb-0"><em>Centro de Integração de Dados e Conhecimentos para Saúde (CIDACS) – Fiocruz</em></p>
						<p class="small text-muted mb-0"><em>Instituto de Saúde Coletiva da Universidade Federal da Bahia (ISC/UFBA)</em></p>
						<p class="small text-muted"><em>[Aula 1 e 2]</em></p>

						<p class="mb-1">Pilar Tavares Veras Florentino</p>
						<p class="small text-muted mb-0"><em>Centro de Integração de Dados e Conhecimentos para Saúde (CIDACS) – Fiocruz</em></p>
						<p class="small text-muted"><em>[Aula 1 e 2]</em></p>

						<p class="mb-1 mt-5"><strong>Módulo 2: Estatística Descritiva e Comunicação de Resultados</strong></p>

						<p class="mb-1">Alexandra Ribeiro Mendes de Almeida</p>
						<p class="small text-muted mb-0"><em>Programa de Computação Científica (PROCC) – Fiocruz</em></p>
						<p class="small text-muted"><em>[Aula 1]</em></p>

						<p class="mb-1">Thiago Cerqueira-Silva</p>
						<p class="small text-muted mb-0"><em>London School of Hygiene and Tropical Medicine (LSHTM)</em></p>
						<p class="small text-muted"><em>[Aula 2]</em></p>

						
						<p class="mb-1 mt-5"><strong>Módulo 3: Modelos estatísticos</strong></p>

						<p class="mb-1">Alexandra Ribeiro Mendes de Almeida</p>
						<p class="small text-muted mb-0"><em>Programa de Computação Científica (PROCC) – Fiocruz</em></p>
						<p class="small text-muted"><em>[Aula 3]</em></p>

						<p class="mb-1">Aline Araújo Nobre</p>
						<p class="small text-muted mb-0"><em>Programa de Computação Científica, Presidência, Fundação Oswaldo Cruz</em></p>
						<p class="small text-muted"><em>[Aula 1 e 2]</em></p>

						<p class="mb-1">Thiago Cerqueira-Silva</p>
						<p class="small text-muted mb-0"><em>London School of Hygiene and Tropical Medicine (LSHTM)</em></p>
						<p class="small text-muted"><em>[Aula 4]</em></p>
					</div>
					
				</div>
			</div>
		`,
	},
	bibliografiaMod1: {
		ariaLabel: "bibliografiaMod1",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 1",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FIGUEIREDO, José Augusto N. G.; FIGUEIREDO, Jacyra N. G. <strong>Algoritmos</strong>: Lógica para Desenvolvimento de Programação de Computadores. 28. ed. Rio de Janeiro: Érica, 2016.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MENEZES, Nilo Ney Coutinho. <strong>Introdução à Programação com Python</strong>: Algoritmos e Lógica de Programação para Iniciantes. 2. ed. São Paulo: Novatec Editora, 2018. Disponível em: <a href='' target='_blank' rel="noopener noreferrer">https://www.kufunda.net/publicdocs/Introdu%C3%A7%C3%A3o%20%C3%A0%20programa%C3%A7%C3%A3o%20com%20Python%20algoritmos%20e%20l%C3%B3gica%20de%20programa%C3%A7%C3%A3o%20para%20iniciantes%20(Nilo%20Ney%20Coutinho%20Menezes).pdf</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MENEZES, Nilo Ney Coutinho.<strong> Introdução à programação com Python:</strong> algoritmos e lógica de programação. 2. ed. São Paulo: Novatec Editora, 2014. p. 53.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GROLEMUND, Garrett; WICKHAM, Hadley. <strong>R for Data Science</strong>: import, tidy, transform, visualize, and model data. Disponível em: <a href='https://r4ds.had.co.nz' target='_blank' rel="noopener noreferrer">https://r4ds.had.co.nz</a>. Acesso em: 8 jun. 2025. Versão em português em tradução: Disponível em: <a href='https://r4ds-translation.netlify.app' target='_blank' rel="noopener noreferrer">https://r4ds-translation.netlify.app</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MATLOFF, Norman. <strong>The Art of R Programming</strong>: a tour of statistical software design. San Francisco: No Starch Press, 2011.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">THEUS, Garrett. <strong>Hands-On Programming with R</strong>: write your own functions and simulations. [S.l.]: Shroff Publishers & Distributors Pvt Ltd, 1 jul. 2014.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>
					
				</div>
			</div>
		`,
	},
	bibliografiaMod2: {
		ariaLabel: "bibliografiaMod2",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 2",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group mb-5">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GROLEMUND, Garrett; WICKHAM, Hadley. <strong>R for Data Science</strong>: import, tidy, transform, visualize, and model data. Disponível em: <a href='https://r4ds.had.co.nz' target='_blank' rel="noopener noreferrer">https://r4ds.had.co.nz</a>. Acesso em: 8 jun. 2025. Versão em português em tradução: Disponível em: <a href='https://r4ds-translation.netlify.app' target='_blank' rel="noopener noreferrer">https://r4ds-translation.netlify.app</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GIOVANIS, E.; OZDAMAR, O.; SAMUK, S. Health status and willingness-to-pay estimates for the benefits of improved recycling rates: evidence from Great Britain. <strong>SN Business & Economics</strong>, v. 1, n. 1, 2021. Dispoível em: <a href='https://doi.org/10.1007/s43546-020-00006-9' target='_blank' rel="noopener noreferrer">https://doi.org/10.1007/s43546-020-00006-9</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">IMAI, C. <em>et al</em>. Tropical influenza and weather variability among children in an urban low-income population in Bangladesh. <strong>Global Health Action</strong>, v. 7, n. 1, 2014. Disponível em: <a href='https://doi.org/10.3402/gha.v7.24413' target='_blank' rel="noopener noreferrer">https://doi.org/10.3402/gha.v7.24413</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Kostaki, E. G. l. <em>et al</em>. Estimation of the determinants for HIV late presentation using the traditional definition and molecular clock‐inferred dates: Evidence that older age, heterosexual risk group and more recent diagnosis are prognostic factors. <strong>HIV Medicine</strong>, v. 23, n. 11, p. 1143-1152, 2022. Disponível em: <a href='https://doi.org/10.1111/hiv.13415' target='_blank' rel="noopener noreferrer">https://doi.org/10.1111/hiv.13415</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Morettin, P. A. <strong>Estatística Básica</strong>. 10. ed. Campinas, SP: Saraiva Uni, 2024</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Rosner, B. <strong>Fundamentals of biostatistics</strong>. 6th ed. Belmont, CA: Thomson-Brooks/Cole, 2006</li>
											</ul>

											<p><strong>Websites</strong></p>

											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GDESCRIPTIVE Statistics. Disponível em: <a href='https://aprendeconalf.es/en/teaching/statistics/manual/descriptive-statistics/' target='_blank' rel="noopener noreferrer">https://aprendeconalf.es/en/teaching/statistics/manual/descriptive-statistics/</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">HISTOGRAMA. 2022. 1 vídeo (8 min.). Disponível em: <a href='https://www.youtube.com/watch?v=cTFUfb0QL7o' target='_blank' rel="noopener noreferrer">https://www.youtube.com/watch?v=cTFUfb0QL7o</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MEDIUM . Boxplot: Como interpretar e plotar em Python? Disponível em: </li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. PNAD – Pesquisa Nacional por Amostra de Domicílios. Disponível em: <a href='https://www.ibge.gov.br/estatisticas/sociais/populacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e' target='_blank' rel="noopener noreferrer">https://www.ibge.gov.br/estatisticas/sociais/populacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group mb-5">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">EME, P. E. <em>et al</em>. Obesity measures in the Kiribati population: a need to reclassify body mass index cut-points. <strong>BMC Public Health</strong>, v. 20, n. 1, 2020. <a href='https://doi.org/10.1186/s12889-020-09217-z' target='_blank' rel="noopener noreferrer">https://doi.org/10.1186/s12889-020-09217-z</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">IMAI, C. <em>et al</em>. Tropical influenza and weather variability among children in an urban low-income population in Bangladesh. <strong>Global Health Action</strong>, v. 7, n. 1, 2014. <a href='https://doi.org/10.3402/gha.v7.24413' target='_blank' rel="noopener noreferrer">https://doi.org/10.3402/gha.v7.24413</a></li>
												
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">CERQUEIRA-SILVA, Thiago; CARDIM, Luciana L.; PAIXÃO, Enny; ROSSI, Marta; SANTOS, Andreia Costa;<em>et al</em>. Hospitalisation, mortality and years of life lost among chikungunya and dengue cases in Brazil: a nationwide cohort study, 2015–2024. <strong>The Lancet Regional Health – Americas</strong>, [S. l.], v. 49, p. 101177, set. 2025.  <a href='https://www.sciencedirect.com/science/article/pii/S2667193X25001875' target='_blank' rel="noopener noreferrer">https://www.sciencedirect.com/science/article/pii/S2667193X25001875</a> </li>


											</ul>

											<p><strong>Websites</strong></p>

											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DATA VIZ PROJECT. Disponível em: <a href='https://datavizproject.com/' target='_blank' rel="noopener noreferrer">https://datavizproject.com/</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">THE DATA visualisation catalogue. <strong>Data Viz Project</strong>. Disponível em: <a href='https://datavizcatalogue.com/' target='_blank' rel="noopener noreferrer">https://datavizcatalogue.com/</a>.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FLOURISH. How to choose the right chart type for your data. Disponível em: <a href='https://flourish.studio/blog/choosing-the-right-visualisation/' target='_blank' rel="noopener noreferrer">https://flourish.studio/blog/choosing-the-right-visualisation/</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>
				</div>
			</div>
		`,
	},
	bibliografiaMod3: {
		ariaLabel: "bibliografiaMod3",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 3",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DIEZ, D.; CETINKAYA-RUNDEL, M.; CHRISTOPHER, D. B. <strong>OpenIntro Statistics</strong>. v. 4. Boston, MA, USA: OpenIntro, 2019. </li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MAGALHÃES, M. N; LIMA, A. C. P. <strong>Noções de probabilidade e estatística</strong>. 4. ed. São Paulo, SP, Brazil: Edusp, 2002.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PAGANO, M.; GAUVREAU, K. <strong>Princípios de bioestatística</strong>. 2. ed. São Paulo: Cengage Learning, 2011. </li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">ANUNCIAÇÃO, L. Tipos de amostragem. <em>In:</em> ANUNCIAÇÃO, L. <strong>Conceitos e análises estatísticas com R e JASP</strong>. São Paulo: Nila Press, 2021.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PROFESSOR GURU. 2023. 1 vídeo (2 min.). Disponível em: <a href='https://www.youtube.com/channel/UCkBKRTla-WORg2aKwLo-iZg' target='_blank' rel="noopener noreferrer">https://www.youtube.com/channel/UCkBKRTla-WORg2aKwLo-iZg</a>. Acesso em: 31 ago. 2024.</li>

											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PAGANO, M.; GAUVREAU, K. <strong>Princípios de bioestatística</strong>. 2. ed. São Paulo: Cengage Learning, 2011. </li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">SILVA, F. R. <em>et al</em>. <strong>Análises ecológicas no R</strong>. Recife: Nupeea; Bauru, SP: Canal 6, 2022. Disponível em: <a href='https://canal6.com.br/livreacesso/livro/analises-ecologicas-no-r/' target='_blank' rel='noopener noreferrer'>https://canal6.com.br/livreacesso/livro/analises-ecologicas-no-r/</a></li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">STATPLACE. Disponível em: <a href='www.youtube.com/@Statplace' target='_blank' rel='noopener noreferrer'>www.youtube.com/@Statplace</a>. Acesso em: 16 set. 2024.</li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">COLOSIMO, E. <strong>Correlação e Regressão linear Simples</strong>. Apresentação do Beamer. Disponível em: <a href='https://www.est.ufmg.br/~enricoc/pdf/EstatisticaII/aula9-10_corr-reg.pdf' target='_blank' rel='noopener noreferrer'>https://www.est.ufmg.br/~enricoc/pdf/EstatisticaII/aula9-10_corr-reg.pdf</a>. Acesso em 12 set. 2024.</li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">LUCAMBIO PÉREZ, F. <strong>Modelos Lineares Generalizados</strong>. Disponível em: <a href='http://leg.ufpr.br/~lucambio/GLM/GLM.html' target='_blank' rel='noopener noreferrer'>http://leg.ufpr.br/~lucambio/GLM/GLM.html</a>. Acesso em: 16 set. 2024.</li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DOBSON, A. J.; BARNETT, A. G. <strong>An introduction to generalized linear models</strong>. 4. ed. Boca Raton, FL: CRC Press, 2018.</li>

											<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">WOOD, S. N. <strong>Generalized additive models:</strong> an introduction with R. Boca Raton, FL: CRC Press, 2017.</li>

										</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item3">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item3" aria-expanded="false" aria-controls="collapse1-item3">Aula 3</button>
								</h5>
								<div id="collapse1-item3" class="accordion-collapse collapse" aria-labelledby="heading1-item3" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DIEZ-ROUX, A. V. Multilevel analysis in public health research. <strong>Annu Rev Public Health</strong>, v. 21, p. 171-92, 2000. doi: 10.1146/annurev.publhealth.21.1.171. PMID: 10884951.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BOCK, C. <em>et al</em>. Machine Learning for Biomedical Time Series Classification: From Shapelets to Deep Learning. <strong>Methods Mol Biol</strong>., v. 2190, p. 33-71, 2021. <a href='https://doi.org/10.1007/978-1-0716-0826-5_2' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1007/978-1-0716-0826-5_2</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">CAPLEHORN, J. R. M.; BELL, J. Methadone dosage and retention of patients maintenance treatment. <strong>Medical Journal of Australia</strong>, v. 154, n. 3, p. 195-199, 1991. <a href='https://doi.org/10.5694/j.1326-5377.1991.tb121030.x' target='_blank' rel='noopener noreferrer'>https://doi.org/10.5694/j.1326-5377.1991.tb121030.x</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">CARVALHO, M. S. <em>et al</em>. <strong>Análise de sobrevivência:</strong> teoria e aplicações em saúde. Rio de Janeiro: Editora Fiocruz, 2011.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MARQUES-TOLEDO, C. D. A. <em>et al</em>. Dengue prediction by the web: Tweets are a useful tool for estimating and forecasting Dengue at country and city level. <strong>PLOS Neglected Tropical Diseases</strong>, v. 11, n. 7, 2017. <a href='https://doi.org/10.1371/journal.pntd.0005729' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1371/journal.pntd.0005729</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">UTHMAN, O. A.; EKSTRÖM, A. M.; MORADI, T. T. Influence of socioeconomic position and gender on current cigarette smoking among people living with HIV in sub-Saharan Africa: Disentangling context from composition. <strong>BMC Public Health</strong>, v. 16, n. 998, 2016. <a href='https://doi.org/10.1186/s12889-016-3637-1' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1186/s12889-016-3637-1</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">WANG, Y. <em>et al</em>. Time series analysis of temporal trends in hemorrhagic fever with renal syndrome morbidity rate in China from 2005 to 2019. <strong>Scientific Reports</strong>, v. 10, n. 9609, 2020. <a href='https://doi.org/10.1038/s41598-020-66758-4' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1038/s41598-020-66758-4</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">WEI, W. W. S. <strong>Time series analysis:</strong> univariate and multivariate methods. 2nd ed. Boston: Pearson Addison Wesley, 2006.</li>
											</ul>

											<p><strong>Website:</strong></p>

											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200"><a href='https://ogre51.medium.com/in-time-series-forecasting-what-do-you-think-is-the-difference-between-seasonality-and-cyclicity-f4e8d9523d24' target='_blank' rel='noopener noreferrer'>https://ogre51.medium.com/in-time-series-forecasting-what-do-you-think-is-the-difference-between-seasonality-and-cyclicity-f4e8d9523d24</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">WHITE NOISE. In: WIKIPEDIA: the free encyclopedia. [San Francisco, CA: Wikimedia Foundation, 2010]. Disponível em: <a href='https://en.wikipedia.org/wiki/White_noise' target='_blank' rel='noopener noreferrer'>https://en.wikipedia.org/wiki/White_noise</a></li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200"><a href='https://bookdown.org/mpfoley1973/survival/semiparametric.html' target='_blank' rel='noopener noreferrer'>https://bookdown.org/mpfoley1973/survival/semiparametric.html</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item4">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item4" aria-expanded="false" aria-controls="collapse1-item4">Aula 4</button>
								</h5>
								<div id="collapse1-item4" class="accordion-collapse collapse" aria-labelledby="heading1-item4" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">LU, S.  <em>et al</em>. Osimertinib after Chemoradiotherapy in Stage III EGFR-Mutated NSCLC. <strong>New England Journal of Medicine</strong>, v. 391, n. 7, p. 585-587, 2024.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">RANZANI, O. T. et al. Characterisation of the first 250 000 hospital admissions for COVID-19 in Brazil: a retrospective analysis of nationwide data. <strong>The Lancet Respiratory Medicine</strong>, v. 9, n. 4, p. 407-418, 2021.</li>
												
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">WEI, W. W. S. <strong>Time series analysis:</strong> univariate and multivariate methods. 2nd ed. Boston: Pearson Addison Wesley, 2006.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>
				</div>
			</div>
		`,
	},
	autorMod1Aula1: {
		ariaLabel: "autorMod1Aula1",
		modalSize: "modal-xl",
		modalTitle: "Sobre os autores",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-10 col-lg-10">
					<div class="mb-5">
						<h5 class="mb-3">Uende Aparecida Figueiredo Gomes</h5>
						<p class="mb-0">Professora-pesquisadora do Departamento de Engenharia Sanitária e Ambiental da Escola de Engenharia da Universidade Federal de Minas Gerais (DESA/UFMG).</p>
					</div>
					
					<div class="mb-5">
						<h5 class="mb-3">Alexandre Pessoa Dias </h5>
						<p class="mb-0">Coordenador acadêmico do curso, professor-pesquisador da Escola Politécnica de Saúde Joaquim Venâncio da Fiocruz (ESPJV/Fiocruz).</p>
					</div>

				</div>
			</div>
		`,
	},
	glossario: {
		ariaLabel: "glossario",
		modalSize: "modal-lg",
		modalTitle: "Glossário",
		modalBody: `
			<div class="accordion accordion-flush" id="accordionExample2">
	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-c">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-c" aria-expanded="false" aria-controls="collapse1-c">C</button>
		</h2>
		<div id="collapse1-c" class="accordion-collapse collapse" aria-labelledby="heading1-c" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>CIT</strong></p>
					<p><strong>Comissão Intergestores Tripartite:</strong> Um fórum de discussão e deliberação que reúne
						representantes do Ministério da Saúde, dos estados e dos municípios para tratar de temas
						relacionados ao SUS.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-e">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-e" aria-expanded="false" aria-controls="collapse1-e">E</button>
		</h2>
		<div id="collapse1-e" class="accordion-collapse collapse" aria-labelledby="heading1-e" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>ESD</strong></p>
					<p><strong>Estratégia de Saúde Digital:</strong> Iniciativa do Ministério da Saúde para promover a
						digitalização dos serviços de saúde no Brasil, com foco na integração de dados e no uso de
						tecnologias emergentes.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-i">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-i" aria-expanded="false" aria-controls="collapse1-i">I</button>
		</h2>
		<div id="collapse1-i" class="accordion-collapse collapse" aria-labelledby="heading1-i" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>IA</strong></p>
					<p>Inteligência Artificial: Tecnologia que simula processos de inteligência humana, utilizada na
						saúde para diagnósticos, previsão de surtos e personalização de tratamentos.</p>
				</div>

				<div class="mb-5">
					<p class="mb-3"><strong>IoT</strong></p>
					<p><strong>Internet das Coisas:</strong> Tecnologia que conecta objetos do dia a dia à internet,
						permitindo que eles coletem e compartilhem dados, sendo aplicada na saúde para monitoramento e
						gestão de dados clínicos.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-o">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-o" aria-expanded="false" aria-controls="collapse1-o">O</button>
		</h2>
		<div id="collapse1-o" class="accordion-collapse collapse" aria-labelledby="heading1-o" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>OMS</strong></p>
					<p><strong>Organização Mundial da Saúde:</strong> Agência especializada das Nações Unidas que
						coordena a saúde pública internacional e define normas e diretrizes globais para a saúde.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-p">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-p" aria-expanded="false" aria-controls="collapse1-p">P</button>
		</h2>
		<div id="collapse1-p" class="accordion-collapse collapse" aria-labelledby="heading1-p" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>PNIIS</strong></p>
					<p><strong>Política Nacional de Informação e Informática em Saúde:</strong> Política elaborada para
						consolidar as ações do SUS relacionadas à informação e tecnologia da informação em saúde, com
						diretrizes para os três níveis da federação.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-r">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-r" aria-expanded="false" aria-controls="collapse1-r">R</button>
		</h2>
		<div id="collapse1-r" class="accordion-collapse collapse" aria-labelledby="heading1-r" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>RNDS</strong></p>
					<p><strong>Rede Nacional de Dados e Saúde:</strong> Plataforma de interoperabilidade do SUS que
						integra dados de saúde em todo o país, promovendo a conectividade entre as diferentes regiões.
					</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-s">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-s" aria-expanded="false" aria-controls="collapse1-s">S</button>
		</h2>
		<div id="collapse1-s" class="accordion-collapse collapse" aria-labelledby="heading1-s" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>SNIS</strong></p>
					<p><strong>Sistema Nacional de Informações em Saúde:</strong> Um sistema proposto para organizar as
						informações em saúde no Brasil, gerido pelo Ministério da Saúde em parceria com estados e
						municípios.</p>
				</div>

				<div class="mb-5">
					<p class="mb-3"><strong>SUS</strong></p>
					<p><strong>Sistema Único de Saúde:</strong> O sistema de saúde pública do Brasil que visa garantir
						acesso universal, integral e gratuito aos serviços de saúde para toda a população.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-t">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-t" aria-expanded="false" aria-controls="collapse1-t">T</button>
		</h2>
		<div id="collapse1-t" class="accordion-collapse collapse" aria-labelledby="heading1-t" data-bs-parent="">
			<div class="accordion-body">
				<p class="mb-3"><strong>TIC</strong></p>
				<p><strong>Tecnologias de Informação e Comunicação:</strong> Conjunto de tecnologias usadas para o
					processamento e comunicação de dados, fundamentais para a organização e gestão da informação em
					saúde.</p>
			</div>
		</div>
	</div>
</div>
		`,
	},
};

// Get all buttons and links that have "modal" in the data-bs-toggle
const modalButtons = document.querySelectorAll('[data-bs-toggle="modal"]');

document.addEventListener("DOMContentLoaded", function (event) {
	//do work

	modalButtons.forEach((btn) => {
		// Check if the modal exist
		const modalId = btn.getAttribute("data-bs-target").slice(1);
		const createdModalId = document.getElementById(modalId);
		const modalOrigin = btn.getAttribute("data-bs-target").slice(7);
		const hasPropriety = Object.hasOwn(modalInfos, modalOrigin);

		if (!createdModalId && hasPropriety) {
			// console.log('modalOrigin: ' + modalOrigin + ' hasPropriety: ' + hasPropriety);

			// If don't exist create one
			createModal(modalId);
		}
	});
});

function createModal(id) {
	const newModal = document.createElement("div");
	const modalLabel = id.slice(6);

	newModal.classList.add("modal", "fade");
	newModal.setAttribute("id", id);
	newModal.setAttribute("tabindex", "-1");
	newModal.setAttribute("aria-labelledby", modalLabel);
	newModal.setAttribute("aria-hidden", "true");

	newModal.innerHTML = `
		<div class="modal-dialog ${modalInfos[modalLabel].modalSize}">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="${modalInfos[modalLabel].ariaLabel}">${modalInfos[modalLabel].modalTitle}</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					${modalInfos[modalLabel].modalBody}
				</div>
				<div class="modal-footer">
					<button type="button" class="fio-button fio-button-primary" data-bs-dismiss="modal">Fechar</button>
				</div>
			</div>
		</div>
	`;

	document.body.appendChild(newModal);
}

//Before and after
const container = document.querySelector(".antes-e-depois--container");
document.querySelector(".antes-e-depois--slider").addEventListener("input", (e) => {
	container.style.setProperty("--position", `${e.target.value}%`);
});
