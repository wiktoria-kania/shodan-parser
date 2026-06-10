def save_results(results,filepath):
    with open(filepath,"a") as file:

        for result in results:
            file.write(f"Scan date: {result['scan_date']}\n")
            file.write(f"IP: {result['ip']}\n")
            file.write(f"Ports:\n\t" + "\n\t".join(map(str, result['ports'])) + "\n")
            file.write(f"Organization: {result['org']}\n")
            file.write(f"ISP: {result['isp']}\n")
            file.write(f"Country: {result['country_code']}\n")
            file.write(f"Servers: \n\t" + "\n\t".join(result['servers']) + "\n")
            file.write(f"Server Types:\n\t" + "\n\t".join(result['server_types']) + "\n")
            file.write(f"Vulnerabilities:\n\t" + "\n\t".join(result['vulnerabilities']) + "\n" or 'None' + "\n")
            file.write(f"SSL Domains:\n\t" + "\n\t".join(result['ssl_domains']) or 'None' + "\n")

            file.write("\n")
            file.write("-" * 50)
            file.write("\n\n")