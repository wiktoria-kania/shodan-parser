import sqlite3

DB_NAME = "./output/shodan_results.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()
    
    sql = """
        CREATE TABLE IF NOT EXISTS hosts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_date TEXT,
            ip TEXT,
            ports TEXT,
            org TEXT,
            isp TEXT,
            country_code TEXT,
            servers TEXT,
            server_types TEXT,
            vulnerabilities TEXT,
            ssl_domains TEXT
        )
        """
    cursor.execute(sql)

    conn.commit()
    conn.close()

def insert_result(result):
    conn = sqlite3.connect(DB_NAME)

    sql = """
        INSERT INTO hosts (
            scan_date,
            ip,
            ports,
            org,
            isp,
            country_code,
            servers,
            server_types,
            vulnerabilities,
            ssl_domains
        ) VALUES (?,?,?,?,?,?,?,?,?,?)
        """
    cursor = conn.cursor()

    cursor.execute(sql,
    (
        result["scan_date"],
        result["ip"],
        ",".join(map(str, result["ports"])),
        result["org"],
        result["isp"],
        result["country_code"],
        ",".join(result["servers"]),
        ",".join(result["server_types"]),
        ",".join(result["vulnerabilities"]),
        ",".join(result["ssl_domains"])
    ))

    conn.commit()
    conn.close()

def fetch_all_hosts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            *
        FROM hosts
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

def load_data_to_tree(tree):
    for item in tree.get_children():
        tree.delete(item)

    rows = fetch_all_hosts()

    for row in rows:
        tree.insert("", "end", values=row)
