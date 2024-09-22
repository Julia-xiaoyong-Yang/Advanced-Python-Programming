# Advanced-Python-Programming

# Fördjupning i Pythonprogrammering

## Målet
Detta projekt är utformat för att automatisera datainsamling och lagring genom att hämta data från antingen en lokal CSV-fil eller en Web API, och sedan lagra informationen i en SQL Server-databas. Genom att använda Windows Task Scheduler kan Python-programmet schemaläggas för att köras vid en bestämd tidpunkt varje dag, vilket säkerställer att datat uppdateras automatiskt och att den senaste informationen alltid finns tillgänglig i databasen.

## Instruktioner
Pythonprogrammet kan bearbeta data, till exempel genom att:
- Ändra datatyper
- Formatera värden enligt ett visst format
- Uppdatera en SQL-tabell

Datan kan komma från:
- En fil på din dator (till exempel i CSV-format)
- Ett API
- En SQL-databas

Skriptet hanterar eventuella undantag (exceptions) och loggar dem i en loggfil för felsökning och spårning. Dessutom finns ett separat skript för att automatisera testerna.

## Funktioner
- **Databehandling**: Bearbetning av data genom att ändra datatyper och formatera värden.
- **Datakälla**: Data kan hämtas från en lokal fil, API, eller SQL-databas.
- **Automatisk Schemaläggning**: Programmet är konfigurerat för att köras automatiskt via Windows Task Scheduler.
- **Loggning och Felsökning**: Skriptet hanterar exceptions och loggar dem i en loggfil för att underlätta felsökning.
- **Tester**: Ett separat skript för att testa huvudkoden finns tillgängligt.

## Struktur
Projektet består av följande Python-skript:

- `main.py`: Huvudprogrammet som ansvarar för att koppla samman hela arbetsflödet (pipeline) genom att köra följande steg:
  - `api_data.py`: Hämtar data från ett API (om tillämpligt).
  - `clean_data.py`: Bearbetar och rensar data (till exempel genom att ändra datatyper och dela upp data).
  - `update_SQL.py`: Uppdaterar SQL-tabellen med de bearbetade data.

- `test.py`: Ett separat skript för att automatiskt testa funktionerna i huvudprogrammet.

## Kodstandard
Koden är väl dokumenterad och följer konventioner för kodstandarder, inklusive PEP 8. Dessutom är alla skript försedda med detaljerade kommentarer för att underlätta förståelsen av koden.

## Krav
- Python 3.x
- Bibliotek som används:
  - `pandas`
  - `logging`
  - `sqlite3` (eller annan SQL-modul beroende på din databas)
  - Eventuellt ytterligare bibliotek för att hantera API-anrop, till exempel `requests`.

## Installation och användning
1. Klona detta repository:
   ```bash
   git clone https://github.com/your-username/F-rdjupning-i-Pythonprogrammering.git
