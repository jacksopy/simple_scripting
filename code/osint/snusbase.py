import os
import requests
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class FakeColor:
        def __getattr__(self, name): return ""
    Fore = Style = FakeColor()

API_TOKEN = "VOTRE_TOKEN_SNUSBASE"
API_URL = "https://api.snusbase.com/v3/"

ASCII_ART = f"""{Fore.GREEN}
 _____             _           _               
|   __|___ ___ ___| |_ ___ ___| |_ ___ ___ ___ 
|__   | . |  _| . | '_| -_|  _| '_|_ -| -_|_ -|
|_____|___|_| |  _|_,_|___|___|_,_|___|___|___|
              |_|                             

{Style.RESET_ALL}Recherche de données avec Snusbase
"""

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def search_snusbase(query):
    try:
        response = requests.post(
            f"{API_URL}search",
            headers=HEADERS,
            json={"query": query}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def format_results(data):
    if not data or "result" not in data:
        return f"{Fore.RED}Aucune donnée trouvée ou format inattendu."

    lines = [f"{Fore.YELLOW}Résultats trouvés :\n"]

    for entry in data["result"]:
        for key, value in entry.items():
            lines.append(f"{Fore.CYAN}{key}: {Fore.WHITE}{value}")
        lines.append("")

    return "\n".join(lines)

def save_results(output):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"snusbase_results_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"{Fore.GREEN}Résultats sauvegardés dans : {filename}")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(ASCII_ART)
        query = input(f"{Fore.WHITE}🔎 Entrez une recherche (email, ip, hash...) : ").strip()

        if not query:
            print(f"{Fore.RED}❌ Recherche vide.")
            input("Appuyez sur Entrée pour recommencer.")
            continue

        print(f"{Fore.YELLOW}⏳ Requête envoyée à Snusbase...\n")
        results = search_snusbase(query)

        if "error" in results:
            print(f"{Fore.RED}❌ Erreur : {results['error']}")
        else:
            output = format_results(results)
            print(output)
            if input("💾 Sauvegarder les résultats ? (y/n) : ").lower() == "y":
                save_results(output)

        if input("\n🔁 Nouvelle recherche ? (y/n) : ").lower() != "y":
            break

if __name__ == "__main__":
    main()
