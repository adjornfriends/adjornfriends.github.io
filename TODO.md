# ANF website: to-do list

Instructions for Claude: work through this one item at a time, starting at the top. Where an item says NEEDS FROM JOE, stop and ask me for the value. Never make up names, emails, fixtures, stats or links. After each item, preview it at phone width (360px), commit with a clear message, push to main, and tick the item off in this file.

---

## 1. Fixes (do first)

- [x] **Mobile layout fix.** Skip this if the commit "Fix mobile layout: no sideways scroll, one-row swipe menu, bigger tap targets" is already in `git log`. If it isn't, ask me for the CSS.
- [x] **Theme button on phones.** It now sits at the end of the swipeable menu, where it's hidden until you swipe. Move it next to the logo on screens under 820px.

## 2. Real content (NEEDS FROM JOE)

- [x] **Sponsor email.** Set `SPONSOR_EMAIL` in the script block so the "Email us" button appears.
  - Email: adjorandfriends@gmail.com
- [ ] **Crew.** Replace the single group photo caption with a card for each crew member: name, role or segment, X handle, and a headshot if available. Compress headshots to under 40KB each (WebP), because most visitors are on mobile data.
  - Names / roles / handles: ______________________
  - Headshots: yes / no (keep group photo)
- [x] **Latest videos (auto-updating).** Show the channel's newest uploads without anyone editing the site.
  - **Placement:** at the top of the existing "Watch and follow" section (`#watch`), above the YouTube / Playback / X cards, so the Watch menu link jumps to it.
  - **How it updates:** add a GitHub Actions workflow (`.github/workflows/videos.yml`) that runs every 3 hours (plus a manual "Run workflow" button). It downloads the channel's public feed `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`, takes the newest 6 videos (id, title, published date), and writes `videos.json` to the repo root. It commits only if something changed. No API key needed. The browser can't read YouTube's feed directly (blocked cross-site), which is why the workflow does it.
  - **What the site does:** `index.html` fetches `videos.json` and renders the newest 4 as cards: thumbnail (`https://i.ytimg.com/vi/ID/hqdefault.jpg`, `loading="lazy"`), title, and "x days ago". Tapping a card swaps in a `youtube-nocookie.com` player with autoplay, so the player only loads when someone taps (light on mobile data). The newest video is shown largest.
  - **Layout:** on phones, one card at a time, full width, in a sideways swipe row (scroll-snap). On laptop, the newest large on the left with 3 smaller beside it. End with a "More on YouTube" link to the channel.
  - **Fallback:** if `videos.json` is missing or empty, show a single "Watch the latest on YouTube" button instead of an empty box.
  - **Check with Joe:** the feed includes Shorts and finished live streams. Decided: hide Shorts (a Short can be detected by requesting `https://www.youtube.com/shorts/ID` in the workflow: it returns 200 for Shorts and redirects otherwise).
  - **NEEDS FROM JOE:** Channel ID (YouTube Studio → Settings → Channel → Advanced settings, starts with `UC`): UCCurjgjcfiRm9l0dYlC_RNw
- [ ] **Upcoming fixtures and watch-alongs.** Add a "Coming up" section listing date, time (GMT, Ghana time), teams, and whether there's a live watch-along. Also let people tap a fixture to prefill the teams on the "Call the score" board.
  - Fixtures: ______________________
- [ ] **Audience numbers for sponsors.** Add 3–4 headline stats to the sponsor section (for example subscribers, typical live viewers, best watch-along views). Use current figures only.
  - Figures + date they were taken: ______________________
- [x] **Partner logo.** The partner is Jerzarie Clothing (replaced Betano), shown in "Join the squad" as a pill with their round badge and name, linking to https://www.jerzarie.com. The badge was taken from their website header; swap it if they send an official file.

## 3. Sharing and discoverability

- [x] **Link previews.** Add Open Graph and Twitter card meta tags (title, description, a 1200×630 share image in ANF yellow/blue) so links posted on WhatsApp and X show a proper preview card.
- [x] **Favicon.** Add a browser-tab icon based on the ANF logo.
- [ ] **Visitor analytics.** Add a free, lightweight, cookie-free counter (e.g. GoatCounter or Cloudflare Web Analytics) so we know how many people visit.
  - Which one / account: ______________________

## 4. Bigger decisions (discuss before building)

- [ ] **Live prediction league.** Right now fans post calls on X with #ANFgames and the table is edited by hand in `LEADERS`. Options: (a) keep it manual; (b) a Google Form + Sheet the site reads; (c) a small Supabase database with fan submissions and an admin results page. Ask me which, and explain the trade-offs first.
- [ ] **Custom domain.** e.g. adjorandfriends.com instead of the github.io address. The domain has to be bought first; then set it in Settings → Pages.
  - Domain: ______________________
