# ANF website — notes for Claude

## What this is
One-page site for Adjor & Friends (ANF) / Adjor Talks Football, a Ghanaian football media channel. Live on GitHub Pages at https://josephbortey2003-droid.github.io/anf-website/ — every push to main redeploys it within a couple of minutes.

## Structure
- Everything is in `index.html`: CSS in `<style>`, JS in `<script>` at the bottom, logo and crew photo inlined as base64 data URIs.
- Keep it a single file unless I ask otherwise. No frameworks or build step.

## Brand
- Font: Outfit (Google Fonts), weights 400/500/700/800.
- Light theme: yellow background #FFF417, blue ink #002AFF, card #FFFBB5.
- Dark theme swaps them: blue background #002AFF, yellow ink #FFF417, card #0020CC.
- Bold, uppercase hero headings, thick 3px borders, rounded cards.
- Colours are CSS variables on :root; dark mode is set in three places (prefers-color-scheme, and data-theme="dark"/"light" from the Theme button). Keep all three in sync.

## Settings (top of the <script> block)
- `SPONSOR_EMAIL`: empty means the "Email us" button stays hidden.
- `LEADERS`: prediction league rows, e.g. {name:"@handle", exact:2, results:3}. Points = exact × 3 + results. Table sorts itself.
- `HASHTAG`: league hashtag, default #ANFgames.

## Links used on the site
- YouTube: https://www.youtube.com/@thekingadjor
- Community: https://www.playback.tv/adjtalksfootball
- X: @adjorNfriends and @thekingadjor
- Partner: Betano

## Gotchas
- `.la` / `.lb` are the light/dark logo classes. Don't reuse those class names for anything else (the league table once used `lb` and got hidden).
- Most visitors are on phones in Ghana, often on mobile data: test at phone width, keep images compressed, avoid heavy scripts.
- Don't invent names, emails, fixtures or stats. Ask me for real ones.

## Still to add
Sponsor email, crew names/roles/handles, upcoming fixtures, 3–4 featured videos (YouTube embeds are fine now that it's on GitHub Pages).

## Workflow
When a change is done: preview it, commit with a clear message, and push to main.
