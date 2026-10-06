"""Render the academic website with Python's standard library. No build service required."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.loads((ROOT / 'content.json').read_text())
BASE = 'https://munawarali93.github.io/website/'
NAV = [('index.html', 'About'), ('publications.html', 'Publications'),
       ('teaching.html', 'Teaching'), ('talks.html', 'Talks'),
       ('awards.html', 'Awards'), ('grants.html', 'Grants'),
       ('schools.html', 'Schools'), ('cv.html', 'CV')]


def e(text):
    return escape(str(text), quote=True)


def link(url, label, cls=''):
    return f'<a href="{e(url)}" class="{e(cls)}">{e(label)}</a>'


def profiles():
    return ''.join(link(url, label) for label, url in D['profiles'])


def paper(p, summary=False):
    title = link(p['url'], p['title']) if p['url'] else e(p['title'])
    authors = e(p['authors']).replace('Munawar Ali', '<strong>Munawar Ali</strong>')
    summary_html = f'<p class="paper-summary">{e(p["summary"])}</p>' if summary and p.get('summary') else ''
    action = link(p['url'], 'Read preprint ↗' if p['type'] == 'Preprint' else 'View article ↗', 'text-link') if p['url'] else ''
    return f'''<article class="paper">
      <div class="record-date">{e(p['year'])}<span>{e(p['type'])}</span></div>
      <div><h3>{title}</h3><p class="authors">{authors}</p>
      <p class="venue">{e(p['venue'])}</p>{summary_html}{action}</div>
    </article>'''


def records(items, title_links=False):
    rows = []
    for r in items:
        title = link(r['url'], r['title']) if title_links and r.get('url') else e(r['title'])
        place = link(r['url'], r['place']) if r.get('kind') and r.get('url') else e(r['place'])
        kind = f'<p class="record-kind">{e(r["kind"])}</p>' if r.get('kind') else ''
        detail = f'<p class="record-detail">{e(r["detail"])}</p>' if r.get('detail') else ''
        rows.append(f'<article class="record"><p class="record-date">{e(r["date"])}</p><div>{kind}<h3>{title}</h3><p class="record-place">{place}</p>{detail}</div></article>')
    return '<div class="record-list">' + ''.join(rows) + '</div>'


def section(title, body, id_='', cls=''):
    return f'<section class="content-section {e(cls)}" id="{e(id_)}"><h2>{e(title)}</h2>{body}</section>'


def intro(title, description, label='Academic profile', extra=''):
    return f'<header class="page-intro"><p class="eyebrow">{e(label)}</p><h1>{e(title)}</h1><p class="lead">{e(description)}</p>{extra}</header>'


def shell(filename, title, description, content, cls=''):
    nav_items = []
    for path, name in NAV:
        current = ' aria-current="page"' if path == filename else ''
        nav_items.append(f'<a href="{path}"{current}>{name}</a>')
    nav = ''.join(nav_items)
    document_title = 'Munawar Ali | Mathematics · Florida State University' if filename == 'index.html' else f'{title} | Munawar Ali'
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(description)}">
  <meta name="author" content="Munawar Ali">
  <meta name="theme-color" content="#692a38">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(document_title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{BASE}{filename if filename != 'index.html' else ''}">
  <title>{e(document_title)}</title>
  <link rel="canonical" href="{BASE}{filename if filename != 'index.html' else ''}">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="stylesheet" href="styles.css">
  <script src="site.js" defer></script>
</head>
<body class="{cls}">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="./" aria-label="Munawar Ali — home">Munawar Ali<span>MATHEMATICS · FLORIDA STATE UNIVERSITY</span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-navigation" hidden>Menu <span aria-hidden="true">☰</span></button>
      <nav class="main-navigation" id="main-navigation" aria-label="Main navigation">{nav}</nav>
    </div>
  </header>
  <main class="container" id="main">{content}</main>
  <footer class="site-footer"><div class="container footer-grid">
    <div><a class="footer-name" href="./">Munawar Ali</a><p>Department of Mathematics<br>Florida State University · Tallahassee, Florida</p></div>
    <div><p class="footer-label">CONTACT</p><a href="mailto:{e(D['email'])}">{e(D['email'])}</a><p>Office: {e(D['office'])}</p></div>
    <div><p class="footer-label">ELSEWHERE</p><div class="footer-profiles">{profiles()}</div></div>
  </div><div class="container footer-bottom"><span>© 2026 Munawar Ali</span><span>Updated {e(D['updated'])}</span></div></footer>
</body>
</html>
'''
    (ROOT / filename).write_text(html)


def home():
    interests = ''.join(f'<div><h3>{e(i["title"])}</h3><p>{e(i["text"])}</p></div>' for i in D['interests'])
    selected = ''.join(paper(p) for p in D['papers'][1:4])
    body = f'''
    <section class="profile-hero" aria-labelledby="profile-name">
      <div class="profile-copy"><p class="eyebrow">Probability · Analysis · Learning</p>
        <h1 id="profile-name">Munawar Ali<span class="name-period">.</span></h1>
        <p class="profile-role">{e(D['role'])}</p>
        <p class="profile-university">Florida State University</p>
        <p class="profile-summary">I study stochastic systems through rough paths and signatures, connecting mathematical theory with data-driven methods.</p>
        <div class="profile-actions"><a class="button" href="publications.html">Explore my research <span aria-hidden="true">↗</span></a><a class="button button-outline" href="cv.html">Curriculum vitae</a></div>
        <div class="profile-links" aria-label="Academic and professional profiles">{profiles()}</div>
      </div>
      <figure class="profile-photo"><img src="assets/munawar-ali.jpg" width="1280" height="580" alt="Munawar Ali by the waterfront with the New York skyline behind him" fetchpriority="high"><figcaption>Munawar Ali</figcaption></figure>
    </section>
    <section class="split-section" id="about" aria-labelledby="about-heading">
      <div><p class="eyebrow">A brief introduction</p><h2 id="about-heading">About me</h2></div>
      <div class="prose"><p>I am a PhD candidate in Financial Mathematics at Florida State University, working with Dr. Qi Feng. My research sits at the intersection of stochastic analysis, rough path theory, and machine learning, with an emphasis on signature methods for irregular data and stochastic dynamics.</p>
      <p>I am also a Lecturer in Mathematics at {e(D['lectureship'])}, currently on study leave. Before joining FSU, I completed my MS in Mathematics at Sukkur IBA University and my BSc and MSc at Shah Abdul Latif University, Khairpur.</p>
      <p>At FSU, I teach calculus and have supported courses in linear algebra and differential equations. I enjoy the connections between abstract mathematics, computation, and applications.</p></div>
    </section>
    <section class="research-themes" aria-labelledby="interests-heading"><div class="section-heading"><h2 id="interests-heading">Research interests</h2><span class="section-note">Theory & applications</span></div><div class="interest-grid">{interests}</div></section>
    <section class="selected-research" aria-labelledby="selected-heading"><div class="section-heading"><h2 id="selected-heading">Selected research</h2><a class="text-link" href="publications.html">All publications <span aria-hidden="true">→</span></a></div>{selected}</section>
    <div class="home-bottom"><section><p class="eyebrow">Teaching at FSU</p><h2>In the classroom</h2><p>Calculus, linear algebra, and differential equations.</p><a class="text-link" href="teaching.html">Teaching history <span aria-hidden="true">→</span></a></section>
    <section><p class="eyebrow">Academic recognition</p><h2>Honors & support</h2><p>Fulbright–HEC Scholar and recipient of FSU graduate fellowships and awards.</p><a class="text-link" href="awards.html">Honors and awards <span aria-hidden="true">→</span></a></section></div>
    '''
    shell('index.html', 'About', 'Munawar Ali is a PhD candidate in Financial Mathematics at Florida State University, researching stochastic analysis, rough paths, signatures, and machine learning.', body, 'home-page')


def publications():
    body = intro('Publications', 'Working papers, preprints, and journal articles on stochastic analysis, signatures, and mathematical finance.', 'Research', '<nav class="page-index" aria-label="Publication sections"><a href="#working">Working papers</a><a href="#preprints">Preprints</a><a href="#journals">Journal articles</a><a href="#theses">Theses</a></nav>')
    for title, key, kind in [('Working papers', 'working', 'Working paper'), ('Preprints', 'preprints', 'Preprint'), ('Journal articles', 'journals', 'Journal article')]:
        body += section(title, ''.join(paper(p, summary=True) for p in D['papers'] if p['type'] == kind), key)
    body += section('Theses', records([
        {'date':'2022–present', 'title':'PhD thesis', 'place':'Florida State University', 'detail':'In progress · Advisor: Dr. Qi Feng'},
        {'date':'2018–2020', 'title':'Modeling Credit Risk Driven by Mixed Fractional Brownian Motion', 'place':'Master’s thesis · Sukkur IBA University', 'detail':''}
    ]), 'theses')
    shell('publications.html', 'Publications', 'Publications and preprints by Munawar Ali on branched signatures, stochastic dynamics, and mathematical finance.', body)


def teaching():
    rows = ''.join(f'<tr><th scope="row">{e(c["term"])}</th><td><span class="course-code">{e(c["code"])}</span>{e(c["title"])}</td><td>{e(c["role"])}</td></tr>' for c in D['courses'])
    body = intro('Teaching', 'Undergraduate mathematics teaching in the United States and Pakistan.', 'In the classroom')
    body += section('Florida State University', '<p class="section-description">Graduate Teaching Assistant, Grader, and Instructor of Record · August 2023–present</p><div class="table-wrap" role="region" aria-label="FSU teaching history" tabindex="0"><table><caption>Courses and teaching roles</caption><thead><tr><th scope="col">Term</th><th scope="col">Course</th><th scope="col">Role</th></tr></thead><tbody>'+rows+'</tbody></table></div>', 'fsu')
    body += section('Lectureships', records(D['appointments'][1:]), 'lectureships')
    body += '<aside class="contact-note"><h2>For students</h2><p>For course-related questions, contact me at <a href="mailto:ma22bm@fsu.edu">ma22bm@fsu.edu</a>. My office is LOV-303.</p></aside>'
    shell('teaching.html', 'Teaching', 'Munawar Ali’s teaching experience in calculus, linear algebra, differential equations, and applied mathematics.', body)


def listing(filename, title, description, label, items, extra='', title_links=False):
    shell(filename, title, description, intro(title, description, label) + records(items, title_links) + extra)


def cv():
    body = intro('Curriculum vitae', 'Munawar Ali · Department of Mathematics, Florida State University', 'Academic record', '<div class="cv-tools"><button class="button print-button" type="button" hidden>Print / save as PDF <span aria-hidden="true">↗</span></button><span>Updated October 2026</span></div>')
    body += '<div class="cv-contact"><a href="mailto:ma22bm@fsu.edu">ma22bm@fsu.edu</a> · Office LOV-303 · Tallahassee, Florida</div>'
    body += section('Education', records(D['education']), 'education')
    body += section('Research interests', '<p class="prose">'+e('; '.join(i['text'].rstrip('.') for i in D['interests']))+'.</p>', 'research')
    body += section('Academic appointments', records(D['appointments']), 'appointments')
    body += section('Publications & working papers', ''.join(paper(p) for p in D['papers']), 'papers')
    body += section('Theses', records([
        {'date':'2022–present', 'title':'PhD thesis (in progress)', 'place':'Florida State University', 'detail':'Advisor: Dr. Qi Feng'},
        {'date':'2018–2020', 'title':'Modeling Credit Risk Driven by Mixed Fractional Brownian Motion', 'place':'Master’s thesis · Sukkur IBA University', 'detail':''}
    ]), 'theses')
    body += section('Honors & awards', records(D['awards']), 'awards')
    body += section('Research & travel support', records(D['grants']), 'grants')
    body += section('Talks & presentations', records(D['talks']), 'talks')
    body += section('Summer & winter schools', records(D['schools'], True), 'schools')
    body += section('Workshops', records(D['workshops']), 'workshops')
    body += section('Technical skills', '<p>Python · MATLAB · LaTeX · Microsoft Office</p>', 'skills')
    shell('cv.html', 'Curriculum vitae', 'Academic CV of Munawar Ali: education, research, publications, teaching, honors, and presentations.', body, 'cv-page')


if __name__ == '__main__':
    home()
    publications()
    teaching()
    listing('talks.html', 'Talks & presentations', 'Conference talks, workshop presentations, and posters.', 'Sharing research', D['talks'])
    listing('awards.html', 'Honors & awards', 'Fellowships, scholarships, and recognition for research, academic achievement, and presentation.', 'Academic recognition', D['awards'])
    listing('grants.html', 'Grants & support', 'Funding for doctoral studies and participation in the mathematical community.', 'Research support', D['grants'])
    listing('schools.html', 'Schools & workshops', 'Summer and winter schools in stochastic analysis, scientific machine learning, and mathematical finance.', 'Continuing study', D['schools'], section('Workshops', records(D['workshops']), 'workshops'), True)
    cv()
    print('Generated 8 static academic pages.')
