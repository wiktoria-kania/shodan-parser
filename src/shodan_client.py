import requests

API_KEY = "";

def get_host(ip):

    url = f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}"

    response = requests.get(url)

    print(response.status_code)

    if response.status_code != 200:
        print(f"Błąd dla {ip}: {response.status_code}")
        return None

    return response.json()


 