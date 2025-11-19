# DevOps Crypto Pipeline

Detta projekt är en enkel crypto-applikation som hämtar prisdata från CoinGecko API och visar den i en webapp.

## Syfte

- Öva på Git och GitHub
- Bygga upp en mappstruktur för ett Python-projekt
- Förbereda en DevOps-pipeline (tester, build, deploy)
- Hämta data från ett externt API (CoinGecko)

## Teknisk översikt

- Språk: Python
- API: CoinGecko
- Struktur:
  - `src/webapp/app.py` – startpunkt för applikationen (webbgränssnitt)
  - `src/webapp/crypto_api.py` – funktioner för att hämta data från CoinGecko
  - `src/webapp/constants.py` – konstanter, t.ex. valda kryptovalutor
  - `src/webapp/utils.py` – hjälpfunktioner för att bearbeta data
  - `src/tests/test_crypto_api.py` – tester för API-funktionerna

## Pipeline-idé (kort)

1. När kod pushas till GitHub:
   - Kör testerna i `src/tests/`
2. Om testerna går igenom:
   - Bygg applikationen (t.ex. docker-image i ett senare steg)
3. (Senare) Deploy till moln (t.ex. Azure).
