from datetime import date
def parse_host(data):
    ports = data.get("ports", [])
    org = data.get("org")
    isp = data.get("isp")
    country_code = data.get("country_code")

    servers = []
    server_types = []
    ssl_domains = []

    host_vulns = data.get("vulns", {})

    if (host_vulns):
        vulnerabilities = host_vulns
    else:
        vulnerabilities = []

    for service in data.get("data", []):
        server = (
        service.get("product")
        or service.get("http", {}).get("server")
        )
        if server:
            servers.append(server)

        server_type = service.get("_shodan", {}).get("module")
        if server_type:
            server_types.append(server_type)

        ssl_domain = service.get("ssl", {}).get("cert", {}).get("subject",{}).get("CN")
        if ssl_domain:
            ssl_domains.append(ssl_domain)

    return {
        "scan_date": str(date.today()),
        "ip": data.get("ip_str"),
        "ports": ports,
        "org": org,
        "isp": isp,
        "country_code": country_code,
        "servers": list(set(servers)),
        "server_types": list(set(server_types)),
        "vulnerabilities": list(set(vulnerabilities)),
        "ssl_domains": list(set(ssl_domains))
    }
 