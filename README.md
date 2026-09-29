# VECTRA International Logistics — website

Static website for VECTRA International Logistics Ltd ("Precision in Motion."). Plain HTML, CSS and JS; no build step needed to host it.

- Pages: `index.html`, `about.html`, `services.html`, five service pages, `industries.html`, `why-vectra.html`, `contact.html`
- Styles: `css/styles.css` · Scripts: `js/main.js` · Images: `images/`

## Editing

The header and footer are shared across pages, so pages are generated from `_source/build.py`:

```
python3 _source/build.py
```

Edit the content in `build.py`, run it, then commit the regenerated HTML.

## Before launch

- Add real social profile URLs (footer)
- Connect the quote form: set `data-endpoint` on the form in `contact.html` (Formspree, Netlify Forms, etc.). Without it, the form opens the visitor's email app.
