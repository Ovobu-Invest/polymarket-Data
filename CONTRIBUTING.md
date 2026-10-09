# Slik legger du til eller fjerner et marked

## 1. Finn markedet

Gå til polymarket.com og åpne markedet. Kopier lenken, for eksempel
`https://polymarket.com/event/fed-decision-in-october`.

Merk: én *event* kan ha flere *markeder* inni seg (for eksempel ett per kandidat eller ett per utfall). Vi samler inn per marked.

## 2. Finn ID-en

Kjør:

```bash
python tools/lookup.py https://polymarket.com/event/fed-decision-in-october
```

Skriptet lister alle markedene i eventen og skriver ut en ferdig blokk du kan lime rett inn i `markets.yaml`. Velg markedet du vil ha. Står det `LUKKET` bak, er markedet allerede avgjort.

Har du ikke Python? Si fra til Carl, så hjelper vi deg.

## 3. Legg det til

Enklest rett på GitHub:

1. Åpne `markets.yaml` og trykk på blyanten (Edit).
2. Lim inn blokken nederst i fila. Fyll inn `requested_by` og `reason`.
3. Trykk **Commit changes**, velg **Create a new branch** og så **Propose changes**.
4. Trykk **Create pull request**.

Carl går gjennom og godkjenner.

## 4. Fjerne et marked

Endre `status: active` til `status: remove` på markedet, skriv hvorfor i `reason`, og lag en pull request på samme måte. Data vi allerede har samlet blir ikke slettet, det blir arkivert.

## Regler

- Ingen sportsmarkeder.
- Ingen kortsiktige kryptomarkeder (5–15 min). Avtal med Carl først hvis du har en god grunn.
- Én pull request per forslag, alltid med en begrunnelse.
