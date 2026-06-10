# Parser danych o wykrytych podatnościach — Shodan.io

---

## Opis projektu

Projekt jest aplikacją w języku Python, która pobiera dane o hostach z API serwisu **Shodan**, analizuje je oraz zapisuje wyniki do pliku tekstowego oraz lokalnej bazy danych **SQLite**.

Dodatkowo aplikacja posiada prosty interfejs graficzny (GUI), który umożliwia uruchamianie skanowania oraz przeglądanie wyników.

Celem projektu jest automatyczna analiza danych o usługach sieciowych oraz wykrytych podatnościach (CVE).

---

## Wymagania

- Python 3.10+
- dostęp do internetu
- aktywny klucz API Shodan

---

## Funkcjonalności

- wczytanie listy adresów IP z pliku tekstowego
- wysyłanie zapytań do API Shodan
- pobieranie danych o hostach:
  - otwarte porty
  - ISP i organizacja
  - kraj
  - serwery i usługi
  - certyfikaty SSL
  - podatności (CVE, jeśli dostępne)

- zapis wyników do:
  - pliku .txt
  - bazy danych SQLite

- prosty interfejs graficzny (Tkinter)
- możliwość otwierania plików wejściowych i wynikowych z poziomu GUI
- przeglądanie danych w tabeli (Treeview)

---

## Technologie

- Python 3.x
- requests
- sqlite3 
- tkinter
- JSON

---

## Instalacja

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/wiktoria-kania/shodan-parser.git
cd shodan-parser
```

---

### 2. Zainstaluj wymagania

```bash
pip install -r requirements.txt
```

---

## Konfiguracja API

W pliku shodan_client.py należy dodać klucz Shodan:

```python
API_KEY = "TWOJ_KLUCZ_API"
```

---

## Uruchomienie

### Uruchomienie aplikacji GUI:

```bash
python gui.py
```

### Uruchomienie aplikacji w konsoli:

```bash
python main.py
```

---

## Plik wejściowy ips.txt

Plik input/ips.txt powinien zawierać adresy IP sformatowane w taki sposób:

```txt
8.8.8.8
1.1.1.1
...
```
