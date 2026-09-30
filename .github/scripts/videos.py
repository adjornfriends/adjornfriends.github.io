"""Write the channel's newest full videos (no Shorts) to videos.json.

Run by .github/workflows/videos.yml. Uses YouTube's public feed, so no API key.
If YouTube is unreachable or returns nothing usable, videos.json is left as it is.
"""
import json
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

CHANNEL_ID = "UCCurjgjcfiRm9l0dYlC_RNw"  # Adjor Talks Football (@thekingadjor)
KEEP = 6
FEED = "https://www.youtube.com/feeds/videos.xml?channel_id=" + CHANNEL_ID
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
HEADERS = {"User-Agent": "Mozilla/5.0 (anf-website video updater)", "Accept-Language": "en"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


no_redirect = urllib.request.build_opener(NoRedirect)


def warn(msg):
    print("::warning::" + msg)


def fetch_feed():
    for attempt in range(3):
        try:
            req = urllib.request.Request(FEED, headers=HEADERS)
            return urllib.request.urlopen(req, timeout=30).read()
        except Exception as e:
            warn(f"Feed attempt {attempt + 1} failed: {e}")
            time.sleep(10)
    return None


def is_short(video_id):
    """/shorts/ID answers 200 for a Short and redirects to /watch for anything else."""
    req = urllib.request.Request("https://www.youtube.com/shorts/" + video_id, headers=HEADERS)
    try:
        return no_redirect.open(req, timeout=30).status == 200
    except urllib.error.HTTPError as e:
        if 300 <= e.code < 400:
            return False
        raise


def main():
    xml = fetch_feed()
    if xml is None:
        warn("Could not reach the YouTube feed; keeping the current videos.json.")
        return
    videos = []
    for entry in ET.fromstring(xml).findall("a:entry", NS):
        video_id = entry.find("yt:videoId", NS).text
        try:
            if is_short(video_id):
                continue
        except Exception as e:
            warn(f"Skipping {video_id}, Shorts check failed: {e}")
            continue
        videos.append({
            "id": video_id,
            "title": entry.find("a:title", NS).text,
            "published": entry.find("a:published", NS).text,
        })
        if len(videos) == KEEP:
            break
    if not videos:
        warn("No full videos found in the feed; keeping the current videos.json.")
        return
    with open("videos.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {len(videos)} videos:")
    for v in videos:
        print(f"  {v['published'][:10]}  {v['id']}  {v['title']}")


if __name__ == "__main__":
    sys.exit(main())
