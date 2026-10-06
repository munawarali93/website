# Website

A small, responsive HTML and CSS starter website, hosted with GitHub Pages.

## Files

- `index.html` — page content, navigation, and metadata.
- `styles.css` — layout, colors, and responsive styles.
- `favicon.svg` — browser icon.
- `.nojekyll` — serves the static files without Jekyll processing.

## Preview locally

Open `index.html` in a browser, or serve this folder:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then visit <http://localhost:8000>. Stop the server with Ctrl+C.

## Publish changes

GitHub Pages is configured to publish the root of the `main` branch. There is no build step or package installation.

```sh
git add index.html styles.css favicon.svg
git commit -m "Update website"
git push origin main
```

GitHub Pages redeploys after each push. Deployment can take a few minutes.

Repository: <https://github.com/munawarali93/website>

Website: <https://munawarali93.github.io/website/>

## Customize

Edit the page title, introduction, About, and Projects text in `index.html`. Adjust the color variables at the top of `styles.css` to change the palette. Use relative links for local assets so they work under the `/website/` address.

The personal CV PDF in this folder is excluded from Git and is not published. Only add files that you intend to make public.
