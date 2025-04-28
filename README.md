# ai_playwright_demo# Playwright Test Generaattori (GPT + RAG)

Tämä projekti generoi Playwright-testikoodia luonnollisen kielen perusteella hyödyntäen GPT-mallia ja RAG-menetelmää (Retrieval-Augmented Generation).

## Käynnistys
```
pip install -r requirements.txt
streamlit run app.py
```

## Projektirakenne
- `app.py` — Streamlit-pohjainen käyttöliittymä
- `generate_test.py` — Logiikka kehotteen rakentamiseen, URL-tunnistukseen, malligenerointiin ja HTML-analyysiin
- `examples.jsonl` — Esimerkkipareja (kuvaus + koodi)
- `best_practices.txt` — Playwrightin parhaat käytännöt, jotka lisätään automaattisesti kehotteeseen
- `retriever.py` — Esimerkkien hakeminen opetusdatan joukosta
- `models.py` — Mallin alustaminen (Transformer-mallit, Gemini jne.)
- `requirements.txt` — Tarvittavat Python-kirjastot

## Esimerkkidata
`examples.jsonl` sisältää prompt-koodi -pareja muodossa:
```
{"prompt": "Testaa kirjautuminen onnistuu", "code": "test('login success', async ({ page }) => {...})"}
```

## Parhaiden käytäntöjen ohjeistus
`best_practices.txt` tiedosto sisältää Playwrightin parhaat käytännöt:
- Käytä käyttäjäkeskeisiä selektoreita kuten 'getByRole', 'getByLabel', 'getByText'
- Odota automaattisesti elementtejä, vältä kovakoodattuja viiveitä ('waitForTimeout')
- Kirjoita selkeitä ja kuvaavia testinimiä
- Noudata DRY-periaatetta (älä toista koodia)
- Testaa sovellusta oikean käyttäjän näkökulmasta
- Käytä Page Object Model -rakennetta isommissa projekteissa

## Lisäominaisuudet
- URL-tunnistus: Käyttäjän promptista etsitään URL ja haetaan sen sivun elementit automaattisesti.
- HTML-elementtien analyysi: Löydetyt napit, syötekentät ja linkit lisätään mallin kehotteeseen.
- Kehotteen rikastaminen: Esimerkit, löydetyt elementit ja Best Practices ohjeet syötetään mallille parhaan mahdollisen koodin generoimiseksi.
- Navigoinnin jälkeen uusi HTML-sivu voidaan analysoida ja päivittää elementtitieto automaattisesti.
"""
