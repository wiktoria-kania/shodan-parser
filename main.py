from src.file_handler import load_ips
from src.shodan_client import get_host
from src.parser import parse_host
from src.result_writer import save_results
from src.database import insert_result
from src.database import connect_db
import os

def check_files():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    if not os.path.isfile("input/ips.txt"):
        with open("input/ips.txt", "w", encoding="utf-8"):
            pass

        print("Utworzono plik input/ips.txt")

    if not os.path.isfile("output/results.txt"):
            with open("output/results.txt", "w", encoding="utf-8"):
                pass

            print("Utworzono plik output/results.txt")

    connect_db();

def scan_ips():

    ips = load_ips("input/ips.txt")

    results = []

    connect_db();

    for ip in ips:
        raw_data = get_host(ip)

        if raw_data is None:
            continue
        
        result = parse_host(raw_data)

        insert_result(result)

        results.append(result)

    save_results(results, "output/results.txt")

    return results
