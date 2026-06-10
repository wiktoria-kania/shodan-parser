from src.file_handler import load_ips
from src.shodan_client import get_host
from src.parser import parse_host
from src.result_writer import save_results
from src.database import insert_result
from src.database import connect_db


def scan_ips():
    ips = load_ips("input/ips.txt")

    results = []

    connect_db()

    for ip in ips:
        raw_data = get_host(ip)

        if raw_data is None:
            continue
        
        result = parse_host(raw_data)

        insert_result(result)

        results.append(result)

    save_results(results, "output/results.txt")

    return results

