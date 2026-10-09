#!/usr/bin/env python3
"""Gera as páginas estáticas do site Trigo Advogados.
Edite CONFIG abaixo (dados do escritório) e rode:  python3 tools/build.py
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============ DADOS DO ESCRITÓRIO (EDITE AQUI) ============
CONFIG = dict(
    nome="Trigo Advogados",
    site="https://www.trigoadvogados.com.br",
    email="contato@trigoadvogados.com.br",
    telefone="(11) 97466-1004",
    tel_link="+5511974661004",
    whatsapp="5511974661004",          # DDI+DDD+número, só dígitos
    endereco="Rua Exemplo, 000 – Sala 00, Centro",
    cidade="São Paulo",
    local="Vila Olímpia, São Paulo – SP",
    cep="00000-000",
    horario="Segunda a sexta, das 9h às 18h",
    oab_sociedade="OAB/SP nº 00.000",  # registro da sociedade
    instagram="https://instagram.com/advogadostrig",
    linkedin="https://linkedin.com/",
)
C = CONFIG
E = html.escape

ICONS = {
 "scale": '<path d="M12 3v18M5 21h14M7 7h10M7 7l-4 8a4 4 0 0 0 8 0zM17 7l-4 8a4 4 0 0 0 8 0z"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/>',
 "home": '<path d="M3 11l9-8 9 8M5 9.5V21h14V9.5M10 21v-6h4v6"/>',
 "heart": '<path d="M12 21s-8-5.2-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.8-8 11-8 11z"/>',
 "file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9zM14 3v6h6M8 13h8M8 17h6"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "coins": '<circle cx="9" cy="9" r="6"/><path d="M15.5 9.5A6 6 0 1 1 9.5 15.5M9 6.5v5M7.5 8h3"/>',
 "pin": '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}
def ico(n): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'

AREAS = [
 ("civil","scale","Direito Civil","Contratos, responsabilidade civil, indenizações, direito do consumidor e demais questões do dia a dia, na consultoria e no contencioso.",
  ["Elaboração e revisão de contratos","Responsabilidade civil e indenizações","Cobranças e execuções","Direito do consumidor","Direito imobiliário e posse","Família e sucessões"]),
 ("tributario","coins","Direito Tributário","Planejamento tributário e defesa do contribuinte em âmbito administrativo e judicial, para empresas e pessoas físicas.",
  ["Planejamento tributário","Recuperação de tributos pagos indevidamente","Defesas em autuações fiscais","Execuções fiscais","Consultoria em tributos federais, estaduais e municipais","Contencioso administrativo (CARF e esferas locais)"]),
 ("empresarial","briefcase","Direito Empresarial","Assessoria jurídica preventiva e contenciosa para empresas e empreendedores, da abertura à reestruturação.",
  ["Constituição e alteração de sociedades","Contratos empresariais e societários","Recuperação judicial e falência","Propriedade intelectual e marcas","Compliance, governança e LGPD","Planejamento societário e sucessório"]),
]

NAV = [("index.html","Início"),("sobre.html","O Escritório"),("areas.html","Áreas de Atuação"),("equipe.html","Equipe"),("artigos.html","Artigos"),("contato.html","Contato")]

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3A13 13 0 0 0 4.9 22.6L3 29l6.6-1.8A13 13 0 1 0 16 3zm0 23.7a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.700zm5.900-8c-.3-.2-1.900-.9-2.200-1s-.5-.2-.7.2-.8 1-1 1.200-.4.2-.7.1a8.700 8.700 0 0 1-4.300-3.800c-.3-.6.300-.5.900-1.700.1-.2 0-.4 0-.5l-1-2.300c-.2-.6-.5-.5-.7-.5h-.6a1.200 1.200 0 0 0-.9.400 3.700 3.700 0 0 0-1.100 2.700 6.400 6.400 0 0 0 1.300 3.400 14.700 14.700 0 0 0 5.600 4.900c2.100.9 2.900 1 3.900.8a3.300 3.300 0 0 0 2.200-1.500 2.700 2.700 0 0 0 .2-1.500c-.1-.1-.3-.2-.6-.4z"/></svg>'

def layout(fname, title, desc, body, hero="", ld=""):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    url = f'{C["site"]}/{"" if fname=="index.html" else fname}'
    full_title = title if fname=="index.html" else f'{title} | {C["nome"]}'
    org = f'''{{"@context":"https://schema.org","@type":"LegalService","name":"{C["nome"]}","url":"{C["site"]}","telephone":"{C["tel_link"]}","email":"{C["email"]}","address":{{"@type":"PostalAddress","addressLocality":"{C["cidade"]}","addressCountry":"BR"}},"openingHours":"Mo-Fr 09:00-18:00","areaServed":"BR"}}'''
    footer_areas = "".join(f'<li><a href="areas.html#{a[0]}">{a[2]}</a></li>' for a in AREAS[:6])
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b1f3a">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{E(full_title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{C["site"]}/assets/logo.png">
<link rel="icon" href="assets/favicon.png" type="image/png"><link rel="apple-touch-icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{org}</script>{ld}
</head>
<body>
<a class="skip" href="#main">Pular para o conteúdo</a>
<div class="topbar"><div class="wrap"><span>{C["horario"]}</span><span><a href="tel:{C["tel_link"]}">{C["telefone"]}</a> · <a href="mailto:{C["email"]}">{C["email"]}</a></span></div></div>
<header class="site"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="{C["nome"]} – página inicial"><img src="assets/logo.png" alt="Trigo Advogados" width="540" height="470"></a>
<button class="burger" aria-label="Abrir menu" aria-expanded="false"><span></span><span></span><span></span></button>
<ul class="menu">{nav}<li><a class="btn" href="contato.html">Fale conosco</a></li></ul>
</div></header>
<main id="main">
{hero}
{body}
</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand footlogo" href="index.html" aria-label="{C["nome"]} – página inicial"><img src="assets/logo.png" alt="Trigo Advogados" width="540" height="470" loading="lazy"></a>
<p style="margin-top:1.2rem">Advocacia pautada pela ética, pela técnica e pelo compromisso com cada cliente.</p></div>
<div><h4>Navegação</h4><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul></div>
<div><h4>Áreas</h4><ul>{footer_areas}</ul></div>
<div><h4>Contato</h4><ul>
<li>{C["local"]}</li>
<li><a href="tel:{C["tel_link"]}">{C["telefone"]}</a></li>
<li><a href="mailto:{C["email"]}">{C["email"]}</a></li>
<li><a href="{C["instagram"]}" rel="noopener" target="_blank">@advogadostrig</a></li></ul></div>
</div>
<p class="oab-note">Este site tem caráter exclusivamente informativo, nos termos do Provimento nº 205/2021 do Conselho Federal da OAB, e não constitui oferta de serviços, promessa de resultado ou aconselhamento jurídico. Resultados dependem das particularidades de cada caso.</p>
<div class="legal"><span>© <span id="y">2026</span> {C["nome"]} · Sociedade de Advogados · {C["oab_sociedade"]}</span><span><a href="privacidade.html">Política de Privacidade</a></span></div>
</div></footer>
<a class="wa" href="https://wa.me/{C["whatsapp"]}?text=Gostaria%20de%20saber%20mais%20sobre%20os%20servi%C3%A7os" target="_blank" rel="noopener" aria-label="Conversar pelo WhatsApp">{WA_SVG}</a>
<div class="cookie" role="dialog" aria-label="Aviso de cookies"><p style="margin:0">Utilizamos apenas cookies essenciais para o funcionamento do site. Saiba mais na <a href="privacidade.html">Política de Privacidade</a>.</p><button class="btn" id="cookie-ok">Entendi</button></div>
<script>window.TRIGO={{whatsapp:"{C["whatsapp"]}",email:"{C["email"]}"}};document.getElementById("y").textContent=new Date().getFullYear()</script>
<script src="assets/main.js" defer></script>
</body></html>'''

def page_hero(crumb, h1, lead):
    return f'<div class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Início</a> / {crumb}</div><h1>{h1}</h1><p>{lead}</p></div></div>'

CTA = '''<section class="band"><div class="wrap reveal"><span class="eyebrow">Atendimento</span><h2>Precisa de orientação jurídica?</h2>
<p>Conte-nos sobre o seu caso. Analisaremos a situação com atenção e sigilo e indicaremos os caminhos possíveis.</p>
<a class="btn" href="contato.html">Agendar uma conversa</a></div></section>'''

pages = {}

# ---------------- INDEX ----------------
area_cards = "".join(
 f'<a class="card reveal" href="areas.html#{k}"><div class="ico">{ico(i)}</div><h3>{n}</h3><p>{d}</p><span class="more">Saiba mais →</span></a>'
 for k,i,n,d,_ in AREAS)
hero = f'''<div class="hero"><div class="wrap">
<div><span class="eyebrow" style="color:var(--gold-2)">Sociedade de Advogados</span>
<h1>Advocacia com <em>rigor técnico</em> e atenção a cada pessoa</h1>
<p class="lead">Na Trigo Advogados, unimos conhecimento jurídico, comunicação clara e estratégia para proteger seus direitos e os interesses do seu negócio.</p>
<div class="cta"><a class="btn" href="contato.html">Agendar atendimento</a><a class="btn ghost" href="areas.html">Conheça as áreas</a></div></div>
<aside class="hero-card"><h2>Nosso compromisso</h2><ul>
<li>Atendimento próximo, claro e sigiloso</li><li>Análise individual de cada caso</li><li>Transparência em cada etapa do processo</li><li>Atuação ética, conforme o Código da OAB</li></ul></aside>
</div></div>'''
body = f'''
<section><div class="wrap"><div class="head center reveal"><span class="eyebrow">Áreas de atuação</span><h2>Soluções jurídicas para cada necessidade</h2>
<p class="muted">Atuamos em três frentes, de forma consultiva e contenciosa, com visão estratégica para prevenir conflitos e resolvê-los com eficiência.</p></div>
<div class="grid g3">{area_cards}</div>
<p style="text-align:center;margin-top:2.5rem"><a class="btn dark" href="areas.html">Ver detalhes das áreas</a></p></div></section>

<section class="alt"><div class="wrap split">
<div class="reveal"><span class="eyebrow">O escritório</span><h2>Tradição na técnica, modernidade no atendimento</h2>
<p>A Trigo Advogados nasceu da convicção de que o Direito deve ser acessível, compreensível e conduzido com responsabilidade. Acompanhamos pessoas e empresas em todas as fases do caso, sempre com linguagem clara.</p>
<ul class="values"><li><b>Ética</b> – conduta íntegra e sigilo profissional absoluto.</li><li><b>Técnica</b> – estudo aprofundado e atualização constante.</li><li><b>Proximidade</b> – você acompanha cada passo e conta com um interlocutor direto.</li></ul>
<a class="btn dark" href="sobre.html" style="margin-top:1.5rem">Conheça o escritório</a></div>
<div class="panel reveal"><blockquote>“Justiça não é apenas o resultado: é o cuidado com o caminho até ele.”</blockquote><cite>Trigo Advogados</cite></div>
</div></section>

<section class="dark"><div class="wrap"><div class="head reveal"><span class="eyebrow">Como trabalhamos</span><h2>Um método simples e transparente</h2></div>
<div class="steps reveal">
<div class="step"><h3>Escuta</h3><p>Entendemos sua situação, seus objetivos e os documentos envolvidos.</p></div>
<div class="step"><h3>Análise</h3><p>Avaliamos a viabilidade jurídica e apresentamos as alternativas.</p></div>
<div class="step"><h3>Estratégia</h3><p>Definimos juntos o melhor caminho, com prazos e etapas claros.</p></div>
<div class="step"><h3>Acompanhamento</h3><p>Mantemos você informado, de forma objetiva, até a conclusão.</p></div></div></div></section>

<section><div class="wrap split">
<div class="reveal"><span class="eyebrow">Dúvidas frequentes</span><h2>Perguntas que recebemos com frequência</h2><p class="muted">Não encontrou a sua dúvida? Fale conosco e teremos prazer em ajudar.</p><a class="btn dark" href="contato.html">Falar com o escritório</a></div>
<div class="reveal">
<details><summary>Como funciona o primeiro atendimento?</summary><p>É uma conversa para entendermos o seu caso, analisarmos os documentos e explicarmos os caminhos possíveis. Pode ser presencial ou on-line.</p></details>
<details><summary>Atendem clientes de outras cidades?</summary><p>Sim. Realizamos reuniões por vídeo e atuamos em processos eletrônicos, o que permite atender clientes em todo o país.</p></details>
<details><summary>Quais documentos devo levar?</summary><p>Documento de identificação, comprovante de residência e todos os papéis relacionados ao assunto (contratos, notificações, comprovantes). Informaremos o que for necessário em cada caso.</p></details>
<details><summary>Meus dados e informações são sigilosos?</summary><p>Sim. O sigilo profissional é um dever do advogado, e tratamos seus dados conforme a LGPD.</p></details>
<details><summary>Como são definidos os honorários?</summary><p>Os honorários são ajustados em contrato escrito, conforme a complexidade do caso e as tabelas da OAB, de forma transparente desde o início.</p></details>
</div></div></section>

<section class="alt"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Onde estamos</span><h2>Localizados na Vila Olímpia, em São Paulo</h2>
<p class="muted">Atendemos presencialmente na região e também por vídeo, para clientes de todo o país.</p>
<ul class="values"><li>Vila Olímpia, São Paulo – SP</li><li>Segunda a sexta, das 9h às 18h</li></ul>
<p style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem"><a class="btn dark" href="contato.html">Agendar atendimento</a>
<a class="btn dark" style="background:transparent;color:var(--navy)" href="https://www.google.com/maps/search/?api=1&amp;query=Vila+Ol%C3%ADmpia%2C+S%C3%A3o+Paulo%2C+SP" target="_blank" rel="noopener">Abrir no Google Maps</a></p></div>
<div class="map reveal" style="padding:0;overflow:hidden"><iframe title="Mapa: Vila Olímpia, São Paulo" src="https://www.google.com/maps?q=Vila+Ol%C3%ADmpia,+S%C3%A3o+Paulo,+SP&amp;hl=pt-BR&amp;z=15&amp;output=embed" width="100%" height="380" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>
{CTA}'''
pages["index.html"] = layout("index.html","Trigo Advogados – Advocacia com rigor técnico e atenção a cada pessoa",
 "Trigo Advogados: sociedade de advogados com atuação em Direito Civil, Tributário e Empresarial.",body,hero)

# ---------------- SOBRE ----------------
body = f'''
<section><div class="wrap split">
<div class="reveal"><span class="eyebrow">Nossa história</span><h2>Advocacia feita com responsabilidade e proximidade</h2>
<p>A Trigo Advogados é uma sociedade de advogados dedicada a oferecer assessoria jurídica de qualidade a pessoas físicas e empresas. Nosso trabalho parte da escuta atenta e da análise criteriosa de cada situação.</p>
<p>Acreditamos que um bom serviço jurídico começa com clareza: explicamos os riscos, as alternativas e os prazos, para que as decisões sejam tomadas com segurança.</p>
<p>Atuamos tanto na prevenção, com consultoria e contratos bem elaborados, quanto no contencioso, defendendo seus interesses perante o Judiciário e a Administração.</p></div>
<div class="panel reveal"><blockquote>Missão: oferecer soluções jurídicas éticas, eficientes e compreensíveis.</blockquote><cite>Missão</cite></div></div></section>
<section class="alt"><div class="wrap"><div class="head center reveal"><span class="eyebrow">Princípios</span><h2>O que orienta o nosso trabalho</h2></div>
<div class="grid g3">
<div class="card reveal"><div class="ico">{ico("shield")}</div><h3>Sigilo e ética</h3><p>Cumprimos rigorosamente o Código de Ética e Disciplina da OAB e o dever de sigilo profissional.</p></div>
<div class="card reveal"><div class="ico">{ico("scale")}</div><h3>Excelência técnica</h3><p>Estudo permanente da legislação e da jurisprudência para fundamentar cada estratégia.</p></div>
<div class="card reveal"><div class="ico">{ico("users")}</div><h3>Atendimento humano</h3><p>Cada cliente tem um interlocutor direto e recebe informações em linguagem simples.</p></div></div></div></section>
<section><div class="wrap"><div class="head reveal"><span class="eyebrow">Diferenciais</span><h2>Como podemos ajudar você</h2></div>
<div class="grid g2 reveal">
<div class="card"><h3>Pessoas físicas</h3><p>Questões cíveis, como contratos, consumo, imóveis, família e sucessões, e demandas tributárias, com sensibilidade e discrição.</p></div>
<div class="card"><h3>Empresas e empreendedores</h3><p>Estruturação societária, contratos, planejamento e defesa tributária e contencioso cível e empresarial estratégico.</p></div></div></div></section>
{CTA}'''
pages["sobre.html"] = layout("sobre.html","O Escritório","Conheça a Trigo Advogados: história, missão e princípios de uma advocacia ética, técnica e próxima do cliente.",
 body, page_hero("O Escritório","O Escritório","Ética, técnica e proximidade em cada caso."))

# ---------------- ÁREAS ----------------
chips = "".join(f'<li><a href="#{k}">{n}</a></li>' for k,_,n,_,_ in AREAS)
det = "".join(
 f'''<article class="area reveal" id="{k}"><div><div class="card" style="padding:1.2rem 1.5rem;display:flex;gap:1rem;align-items:center"><div class="ico" style="margin:0;flex:none">{ico(i)}</div><h2 style="font-size:1.45rem;margin:0">{n}</h2></div></div>
<div><p>{d}</p><h4 style="font-family:var(--sans);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)">Principais atuações</h4><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul>
<a class="more" style="color:var(--gold);font-weight:600" href="contato.html">Falar sobre este tema →</a></div></article>'''
 for k,i,n,d,l in AREAS)
body = f'<section style="padding-top:3rem"><div class="wrap"><ul class="chips">{chips}</ul>{det}</div></section>{CTA}'
pages["areas.html"] = layout("areas.html","Áreas de Atuação","Direito Civil, Tributário e Empresarial: consultoria preventiva e atuação contenciosa.",
 body, page_hero("Áreas de Atuação","Áreas de Atuação","Três áreas, com atuação consultiva e contenciosa."))

# ---------------- EQUIPE ----------------
body = f'''<section><div class="wrap"><div class="head reveal"><span class="eyebrow">Equipe</span><h2>Quem está à frente do escritório</h2></div>
<article class="founder reveal"><img src="assets/cristina-trigo.jpg" alt="Cristina Trigo, advogada fundadora da Trigo Advogados" width="600" height="600" loading="lazy">
<div><span class="role">Fundadora</span><h3>Cristina Trigo</h3><p class="oab">Advogada</p>
<p>Advogada formada pela Universidade Paulista (UNIP), em 2003, com especialização em Direito Civil pelo Instituto Presbiteriano Mackenzie.</p>
<p>Atua nas áreas consultiva e contenciosa, com foco em matérias de Direito Civil e Tributário.</p>
<a class="btn dark" href="contato.html">Falar com a Dra. Cristina</a></div></article></div></section>{CTA}'''
pages["equipe.html"] = layout("equipe.html","Equipe","Conheça Cristina Trigo, advogada fundadora da Trigo Advogados, com atuação em Direito Civil e Tributário.",body,page_hero("Equipe","Nossa Equipe","Atuação consultiva e contenciosa com foco em Direito Civil e Tributário."))

# ---------------- ARTIGOS ----------------
arts = [
 ("contratos-cuidados","Contratos","Cinco cuidados antes de assinar um contrato","Revisar com atenção evita problemas futuros.",
  ["Assinar um contrato sem lê-lo por inteiro é uma das causas mais comuns de litígios. Antes de firmar qualquer acordo, vale observar alguns pontos.",
   "<b>1. Identificação das partes.</b> Confira nomes, CPF/CNPJ e poderes de quem assina. <b>2. Objeto e prazo.</b> O que exatamente será entregue, quando e por quanto tempo vale. <b>3. Valores e reajustes.</b> Forma de pagamento, índice de correção e multas. <b>4. Rescisão.</b> Condições para encerrar o contrato e eventuais penalidades. <b>5. Foro e resolução de conflitos.</b> Onde e como eventuais disputas serão resolvidas.",
   "Em caso de dúvida, a análise prévia por um advogado costuma ser mais simples e econômica do que a solução do conflito depois de instaurado."]),
 ("recuperacao-tributos","Tributário","Pagou tributo a mais? Veja quando é possível pedir de volta","Nem toda cobrança indevida é percebida.",
  ["Empresas e pessoas físicas podem ter recolhido tributos acima do devido, seja por interpretação equivocada da legislação, seja por mudança de entendimento dos tribunais.",
   "Em geral, o primeiro passo é revisar os recolhimentos dos últimos cinco anos, prazo comum de prescrição para a restituição ou compensação. A partir da análise, avalia-se a via mais adequada: administrativa ou judicial.",
   "Cada situação depende do regime tributário, da documentação e da jurisprudência aplicável, por isso a análise individual por um advogado é indispensável."]),
 ("lgpd-empresas","Empresarial","LGPD: por onde a sua empresa deve começar","Primeiros passos para a adequação.",
  ["A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) alcança qualquer empresa que trate dados pessoais, de clientes, colaboradores ou fornecedores.",
   "Os passos iniciais incluem: mapear quais dados são coletados e para quê; definir a base legal de cada tratamento; revisar contratos e políticas de privacidade; implementar medidas de segurança; e indicar um encarregado (DPO).",
   "A adequação é um processo contínuo, e a assessoria jurídica ajuda a reduzir riscos de sanções e incidentes."]),
]
ahtml = "".join(
 f'<article class="article reveal" id="{k}"><div class="meta">{cat}</div><h2>{t}</h2><p class="muted">{sub}</p>{"".join(f"<p>{p}</p>" for p in ps)}</article>'
 for k,cat,t,sub,ps in arts)
body = f'<section style="padding-top:3rem"><div class="wrap">{ahtml}<div class="notice" style="max-width:760px;margin-inline:auto">O conteúdo desta página tem finalidade meramente informativa e não substitui a consulta a um advogado. Cada caso possui particularidades que podem alterar a orientação aplicável.</div></div></section>{CTA}'
pages["artigos.html"] = layout("artigos.html","Artigos","Artigos e orientações jurídicas da Trigo Advogados sobre contratos, sucessões, LGPD e mais.",body,page_hero("Artigos","Artigos e Orientações","Informação jurídica de forma clara e acessível."))

# ---------------- CONTATO ----------------
opts = "".join(f"<option>{n}</option>" for _,_,n,_,_ in AREAS) + "<option>Outro assunto</option>"
body = f'''<section><div class="wrap split" style="align-items:start">
<div class="reveal"><span class="eyebrow">Fale conosco</span><h2>Vamos conversar sobre o seu caso</h2><p class="muted">Preencha o formulário e escolha como prefere ser atendido. Não envie documentos nem dados sensíveis por este formulário.</p>
<form id="contact-form" novalidate onsubmit="return false">
<div class="row2"><div><label for="nome">Nome completo</label><input id="nome" name="nome" required autocomplete="name"></div>
<div><label for="telefone">Telefone / WhatsApp</label><input id="telefone" name="telefone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="(00) 00000-0000"></div></div>
<div class="row2"><div><label for="email">E-mail</label><input id="email" name="email" type="email" required autocomplete="email"></div>
<div><label for="area">Assunto</label><select id="area" name="area">{opts}</select></div></div>
<div><label for="mensagem">Mensagem</label><textarea id="mensagem" name="mensagem" rows="5" required></textarea></div>
<div><label for="canal">Prefiro ser atendido por</label><select id="canal" name="canal"><option value="whatsapp">WhatsApp</option><option value="email">E-mail</option></select></div>
<label class="check" style="font-weight:400"><input type="checkbox" name="lgpd" required> <span>Li e concordo com a <a href="privacidade.html">Política de Privacidade</a> e autorizo o uso dos meus dados para retorno de contato.</span></label>
<button class="btn" type="submit">Enviar mensagem</button><div id="form-msg" class="form-msg" role="status" aria-live="polite"></div></form></div>
<div class="reveal"><div class="info">
<div>{ico("pin")}<span><b>Endereço</b>{C["local"]}</span></div>
<div>{ico("phone")}<span><b>Telefone</b><a href="tel:{C["tel_link"]}">{C["telefone"]}</a></span></div>
<div>{ico("mail")}<span><b>E-mail</b><a href="mailto:{C["email"]}">{C["email"]}</a></span></div>
<div>{ico("clock")}<span><b>Horário</b>{C["horario"]}</span></div></div>
<div class="map" style="margin-top:2rem;padding:0;overflow:hidden"><iframe title="Mapa: Vila Olímpia, São Paulo" src="https://www.google.com/maps?q=Vila+Ol%C3%ADmpia,+S%C3%A3o+Paulo,+SP&amp;hl=pt-BR&amp;z=15&amp;output=embed" width="100%" height="320" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
<p style="margin-top:.8rem"><a class="more" style="color:var(--gold);font-weight:600" href="https://www.google.com/maps/search/?api=1&amp;query=Vila+Ol%C3%ADmpia%2C+S%C3%A3o+Paulo%2C+SP" target="_blank" rel="noopener">Abrir no Google Maps →</a></p></div>
</div></section>'''
pages["contato.html"] = layout("contato.html","Contato","Entre em contato com a Trigo Advogados e agende um atendimento presencial ou on-line.",body,page_hero("Contato","Contato","Estamos à disposição para ouvir você."))

# ---------------- PRIVACIDADE ----------------
body = f'''<section><div class="wrap prose">
<p class="muted">Última atualização: outubro de 2026.</p>
<h2>1. Quem somos</h2><p>{C["nome"]} é o controlador dos dados pessoais tratados neste site. Contato do encarregado: <a href="mailto:{C["email"]}">{C["email"]}</a>.</p>
<h2>2. Dados que coletamos</h2><ul><li>Dados informados voluntariamente no formulário de contato (nome, e-mail, telefone e mensagem).</li><li>Dados técnicos de navegação, quando necessários à segurança e ao funcionamento do site.</li></ul>
<h2>3. Finalidades e bases legais</h2><p>Utilizamos os dados para responder a solicitações e agendar atendimentos (execução de procedimentos preliminares a contrato e legítimo interesse) e para cumprir obrigações legais, nos termos da Lei nº 13.709/2018 (LGPD).</p>
<h2>4. Compartilhamento</h2><p>Não vendemos dados pessoais. O compartilhamento ocorre apenas quando necessário para o atendimento (por exemplo, serviços de e-mail e mensagens) ou por obrigação legal. As informações estão protegidas pelo sigilo profissional da advocacia.</p>
<h2>5. Cookies</h2><p>Utilizamos apenas cookies e armazenamento local essenciais, como o registro da sua ciência deste aviso. Fontes tipográficas são carregadas do Google Fonts.</p>
<h2>6. Seus direitos</h2><p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, portabilidade, eliminação e revogação de consentimento, escrevendo para <a href="mailto:{C["email"]}">{C["email"]}</a>.</p>
<h2>7. Retenção e segurança</h2><p>Mantemos os dados pelo tempo necessário às finalidades descritas e adotamos medidas técnicas e organizacionais para protegê-los.</p>
<h2>8. Alterações</h2><p>Esta política pode ser atualizada a qualquer momento; a versão vigente estará sempre nesta página.</p>
</div></section>'''
pages["privacidade.html"] = layout("privacidade.html","Política de Privacidade","Como a Trigo Advogados trata dados pessoais, em conformidade com a LGPD.",body,page_hero("Política de Privacidade","Política de Privacidade","Transparência no tratamento dos seus dados."))

# ---------------- 404 ----------------
body = '<section><div class="wrap" style="text-align:center"><span class="eyebrow">Erro 404</span><h1>Página não encontrada</h1><p class="muted">O endereço acessado não existe ou foi movido.</p><a class="btn" href="index.html">Voltar ao início</a></div></section>'
pages["404.html"] = layout("404.html","Página não encontrada","Página não encontrada.",body)

for f,c in pages.items():
    with open(os.path.join(ROOT,f),"w",encoding="utf-8") as fh: fh.write(c)

with open(os.path.join(ROOT,"sitemap.xml"),"w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+
      "".join(f'<url><loc>{C["site"]}/{"" if f=="index.html" else f}</loc></url>\n' for f in pages if f!="404.html")+'</urlset>\n')
with open(os.path.join(ROOT,"robots.txt"),"w") as fh:
    fh.write(f'User-agent: *\nAllow: /\nSitemap: {C["site"]}/sitemap.xml\n')
print("ok:",", ".join(pages))
