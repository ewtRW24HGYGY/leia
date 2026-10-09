# Trigo Advogados – Site institucional

Site estático (HTML/CSS/JS, sem dependências) com: Início, O Escritório, Áreas de Atuação, Equipe, Artigos, Contato, Política de Privacidade (LGPD) e 404. Inclui SEO (meta, Open Graph, JSON-LD, sitemap, robots), acessibilidade, layout responsivo, botão de WhatsApp e aviso de cookies.

## Editar dados do escritório
Os dados (telefone, e-mail, endereço, WhatsApp, OAB, redes) ficam em `CONFIG` no topo de `tools/build.py`. Depois rode:

    python3 tools/build.py

As páginas HTML são regeneradas na raiz. Para publicar, hospede a pasta em qualquer serviço estático (GitHub Pages, Netlify, Vercel…).

## Pendências (substituir placeholders)
- Telefone, e-mail, endereço, CEP, nº OAB, domínio (`site`)
- Nomes, fotos e OAB dos advogados em `equipe.html` (via `tools/build.py`)
- Embed do Google Maps em Contato

## Publicação gratuita
**GitHub Pages:** Settings → Pages → Source: *GitHub Actions*. O workflow `.github/workflows/pages.yml` publica a cada push na `main` em `https://<usuario>.github.io/leia/`.

**Cloudflare Pages:** Workers & Pages → Create → Pages → Connect to Git → repositório `leia`. Framework: *None*; build command: vazio; output directory: `/`. Endereço gratuito: `https://<projeto>.pages.dev`.

Depois de definir o endereço final, atualize `site` em `tools/build.py` e rode `python3 tools/build.py` (canonical, sitemap e robots).
