ANF website: to-do list
Instructions for Claude: work through this one item at a time, starting at the top. Where an item says NEEDS FROM JOE, stop and ask me for the value. Never make up names, emails, fixtures, stats or links. After each item, preview it at phone width (360px), commit with a clear message, push to main, and tick the item off in this file.


________________


1. Fixes (do first)
* [x] Mobile layout fix. Skip this if the commit "Fix mobile layout: no sideways scroll, one-row swipe menu, bigger tap targets" is already in git log. If it isn't, ask me for the CSS.
* [x] Theme button on phones. It now sits at the end of the swipeable menu, where it's hidden until you swipe. Move it next to the logo on screens under 820px.
2. Real content (NEEDS FROM JOE)
* Sponsor email. Set SPONSOR_EMAIL in the script block so the "Email us" button appears.
   * Email: ______________________
* Crew. Replace the single group photo caption with a card for each crew member: name, role or segment, X handle, and a headshot if available. Compress headshots to under 40KB each (WebP), because most visitors are on mobile data.
   * Names / roles / handles: ______________________
   * Headshots: yes / no (keep group photo)
* Featured videos. Add a "Latest videos" section with 3–4 YouTube embeds. Use youtube-nocookie.com embeds with loading="lazy", or a thumbnail that loads the player on tap (lighter on data).
   * Video links: ______________________
* Upcoming fixtures and watch-alongs. Add a "Coming up" section listing date, time (GMT, Ghana time), teams, and whether there's a live watch-along. Also let people tap a fixture to prefill the teams on the "Call the score" board.
   * Fixtures: ______________________
* Audience numbers for sponsors. Add 3–4 headline stats to the sponsor section (for example subscribers, typical live viewers, best watch-along views). Use current figures only.
   * Figures + date they were taken: ______________________
* Betano partner. Show the partner properly: logo if Betano's brand rules allow it, a link if they provided one, and an "18+ | Gamble responsibly" line next to it (standard for betting sponsors; check the partnership agreement for required wording).
   * Logo file / link / required wording: ______________________
3. Sharing and discoverability
* Link previews. Add Open Graph and Twitter card meta tags (title, description, a 1200×630 share image in ANF yellow/blue) so links posted on WhatsApp and X show a proper preview card.
* Favicon. Add a browser-tab icon based on the ANF logo.
* Visitor analytics. Add a free, lightweight, cookie-free counter (e.g. GoatCounter or Cloudflare Web Analytics) so we know how many people visit.
   * Which one / account: ______________________
4. Bigger decisions (discuss before building)
* Live prediction league. Right now fans post calls on X with #ANFgames and the table is edited by hand in LEADERS. Options: (a) keep it manual; (b) a Google Form + Sheet the site reads; (c) a small Supabase database with fan submissions and an admin results page. Ask me which, and explain the trade-offs first.
* Auto-updating videos. Instead of hand-picked videos, show the channel's latest upload automatically using the uploads playlist (the channel ID with UC swapped to UU).
   * Channel ID (YouTube Studio → Settings → Channel → Advanced): ______________________
* Custom domain. e.g. adjorandfriends.com instead of the github.io address. The domain has to be bought first; then set it in Settings → Pages.
   * Domain: ______________________