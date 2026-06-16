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

## GUI

Aplikacja posiada prosty interfejs graficzny stworzony w oparciu o bibliotekę Tkinter, który umożliwia obsługę parsera danych Shodan bez użycia terminala.

### Funkcje GUI

W interfejsie dostępne są następujące opcje:

#### Skanowanie adresów IP

Uruchamia proces skanowania adresów zapisanych w pliku input/ips.txt.

#### Otwieranie plików wejściowych i wyjściowych

- input/ips.txt – lista IP do skanowania
- output/results.txt – zapisane wyniki skanowania
  
Pliki otwierane są bezpośrednio w Notatniku.

#### Odświeżanie danych z bazy

  Pobiera aktualne rekordy z bazy danych i wyświetla je w tabeli.

#### Tabela wyników (TreeView)

Interfejs zawiera tabelę prezentującą dane o zeskanowanych hostach, w tym:

- ID rekordu
- datę skanu
- adres IP
- porty
- organizację i ISP
- kod kraju
- serwery i typy serwerów
- wykryte podatności
- domeny SSL

### Szczegóły rekordu

Po dwukrotnym kliknięciu w wiersz tabeli wyświetlane jest okno dialogowe ze szczegółami hosta które mogą być słąbo widoczne w graficznym wyglądzie bazy danych, zawierające m.in.:

- IP
- porty
- serwery
- typy serwera
- podatności
- domeny SSL

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

### 2. Utwórz środowisko

```bash
python -m venv .venv
```

### 3. Zainstaluj wymagania

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

Aplikacja jest uruchamiana za pomocą pliku gui.py.

```bash
python gui.py
```

---

## Struktura projektu

```bash
shodan-parser/
│
├── gui.py             
├── main.py              
│
├── src/
│   ├── database.py         
│   ├── file_handler.py        
│   ├── parser.py    
│   ├── result_writer.py     
│   └── shodan_client.py       
│
├── input/
│   └── ips.txt          
│
├── output/
│   ├── results.txt      
│   └── shodan_results.db      
│
└── requirements.txt
```

---

## Plik wejściowy ips.txt

Plik input/ips.txt powinien zawierać adresy IP sformatowane w taki sposób:

```txt
8.8.8.8
1.1.1.1
...
```

---

## Ograniczenia

Funkcja otwierania plików wejściowych i wynikowych z poziomu interfejsu graficznego wykorzystuje program Notatnik (notepad.exe) i jest dostępna wyłącznie w systemie Windows.

Pozostałe funkcjonalności aplikacji, takie jak komunikacja z API Shodan, analiza danych, zapis wyników do pliku oraz obsługa bazy danych SQLite, są niezależne od systemu operacyjnego i mogą działać również na innych platformach obsługujących Python.
