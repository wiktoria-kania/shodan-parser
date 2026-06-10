import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
def load_ips(filepath):
    with open(filepath,"r") as file:
        ips = []

        for line in file:
            ip = line.strip()
            
            if validate_ip(ip):
                ips.append(ip)
            else:
                print(f"Nieprawidłowy adres IP: {ip}")
        return ips
    