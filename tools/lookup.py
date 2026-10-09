"""Finn condition_id for markedene i en Polymarket-lenke.

Bruk:  python tools/lookup.py https://polymarket.com/event/<event-slug>
Skriver ut en ferdig blokk du kan lime inn i markets.yaml.
"""
import json
import sys
import urllib.request
from datetime import date

GAMMA = "https://gamma-api.polymarket.com"


def hent(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ovobu-lookup"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def slug_fra_lenke(lenke):
    deler = [d for d in lenke.split("?")[0].strip("/").split("/") if d]
    return deler[-1]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    lenke = sys.argv[1]
    slug = slug_fra_lenke(lenke)

    markeder = []
    if "/event/" in lenke:
        try:
            markeder = hent(f"{GAMMA}/events/slug/{slug}").get("markets", [])
        except Exception:
            markeder = []
    if not markeder:
        try:
            markeder = [hent(f"{GAMMA}/markets/slug/{slug}")]
        except Exception as e:
            print(f"Fant ikke noe marked for '{slug}': {e}")
            sys.exit(1)

    for m in markeder:
        lukket = "  LUKKET" if m.get("closed") else ""
        print(f"# {m.get('question', '')}{lukket}")
        print(f'- condition_id: "{m.get("conditionId", "")}"')
        print(f"  slug: {m.get('slug', '')}")
        print(f'  question: "{m.get("question", "").replace(chr(34), chr(39))}"')
        print("  requested_by: DITT-GITHUB-NAVN")
        print('  reason: "SKRIV HVORFOR"')
        print("  status: active")
        print(f"  added: {date.today().isoformat()}")
        print()


if __name__ == "__main__":
    main()
