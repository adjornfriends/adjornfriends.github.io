# Adjor & Friends website

One-page site for Adjor & Friends / Adjor Talks Football: score predictor, prediction league table, links to YouTube, Playback and X, and a sponsor contact section.

Everything lives in `index.html` (CSS, JS and images are inline). Open it in a browser to preview it.

## Quick edits (in the `<script>` block near the bottom of `index.html`)

- `SPONSOR_EMAIL` — set it to the business email to show the "Email us" button.
- `LEADERS` — league table rows, e.g. `{name:"@handle", exact:2, results:3}`. Points = exact × 3 + results.
- `HASHTAG` — the league hashtag (default `#ANFgames`).
