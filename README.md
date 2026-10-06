# Munawar Ali · Academic website

An accessible, responsive academic website built with static HTML, CSS, and a small amount of JavaScript. GitHub Pages publishes the repository root from `main`.

- Website: <https://munawarali93.github.io/website/>
- Repository: <https://github.com/munawarali93/website>

## Pages

About, Publications, Teaching, Talks, Awards, Grants, Schools, and a printable Curriculum Vitae. All page content and navigation are available without JavaScript. JavaScript enhances the mobile menu and adds the CV print button.

## Edit content

Repeated academic records are maintained in `content.json`. Page introductions and the shared layout are in `scripts/build_site.py`. After editing either source, regenerate the HTML:

```sh
python3 scripts/build_site.py
```

The generated HTML is committed, so hosting needs no Python runtime, package installation, or build step. Edit `styles.css` for visual changes and `site.js` for interactions. Local assets use relative paths so the site works under `/website/`.

## Preview locally

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit <http://localhost:8000>. Stop the server with Ctrl+C.

## Publish

```sh
python3 scripts/build_site.py
git add content.json scripts/build_site.py *.html styles.css site.js favicon.svg assets README.md
git commit -m "Update academic website"
git push origin main
```

GitHub Pages automatically publishes the update after the deployment succeeds.

## Sources and editorial choices

- Biography, course history, talks, awards, grants, schools, profile links, and the original photograph: [previous Google Site](https://sites.google.com/view/munawarali/homepage), reviewed October 6, 2026.
- Education, appointments, research interests, technical skills, and workshops: the local CV PDF.
- KCAMS is the institution name explicitly confirmed by the owner. The original CV uses an older/different name.
- Publication metadata was checked against arXiv and publisher records where available. The two 2024 articles list Javed Hussain before Munawar Ali, consistent with the Google Site and publication records.
- The 2026 SLMath school dates follow the [official event page](https://www.slmath.org/summer-schools/1136): June 22–July 2.
- The university email uses `ma22bm@fsu.edu`; this corrects the mismatched mail link on the previous site.
- The public CV is an HTML page with print styles. The original PDF remains ignored and is not deployed; home address, personal phone number, and referees' contact details are not included in the public pages.
- Dates and roles are a snapshot as of October 2026. Update `content.json` when appointments or teaching assignments change.
