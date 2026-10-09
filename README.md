# Polymarket-data

Övobu Invest sin egen innsamling av ordrebøker og handler fra Polymarket.

Polymarket lagrer nesten ingen historikk for ordrebøkene sine. Data vi ikke samler inn i dag, får vi aldri tak i senere. Derfor bygger vi vårt eget datasett på serveren, som vi kan analysere med SQL og bruke i modellene våre.

## Hva ligger her

| Fil | Hva det er |
|---|---|
| `markets.yaml` | Lista over markedene vi samler inn fra. Det er denne du endrer for å legge til eller fjerne et marked. |
| `CONTRIBUTING.md` | Slik foreslår du nye markeder, steg for steg. |
| `tools/lookup.py` | Lite skript som finner ID-en til et marked fra en Polymarket-lenke. |

Koden til selve innsamleren kommer i `collector/` etter hvert.

## Slik fungerer det

1. Du foreslår et marked ved å endre `markets.yaml` i en pull request.
3. Serveren henter den nye lista og begynner å samle inn fra markedet.

## Regler i korte trekk

- Ingen sportsmarkeder.
- Ingen kortsiktige kryptomarkeder (5–15 min «Up/Down»). De tar enormt mye plass.
- Alltid en kort begrunnelse i `reason`.
- Løste markeder blir ikke slettet, de blir arkivert på ekstern disk.
