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

API_TOKEN = "#mettre l'api ici"
API_URL = "https://leakosintapi.com/"

ASCII_ART = f"""{Fore.GREEN}

 _   _    _     _____   _    ____  _____    _    ____   ____ _   _
| \ | |  / \   |__  /  / \  / ___|| ____|  / \  |  _ \ / ___| | | |
|  \| | / _ \    / /  / _ \ \___ \|  _|   / _ \ | |_) | |   | |_| |
| |\  |/ ___ \  / /_ / ___ \ ___) | |___ / ___ \|  _ <| |___|  _  |
|_| \_/_/   \_\/____/_/   \_\____/|_____/_/   \_\_| \_\\____ |_| |_|


{Style.RESET_ALL}Recherche d'informations via NAZAPI - By Oris
"""

ICON_MAP = {
    "email": "📩",
    "e-mail": "📩",
    "données": "💾",
    "mot de passe": "🔑",
    "password": "🔑",
    "dossier de fuite": "📁",
    "file": "📁"
}

def search_api(query):
    payload = {"token": API_TOKEN, "request": query, "lang": "fr"}
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def format_results(query, results):
    lines = [
        f"{Fore.YELLOW}📄 Résultats pour : {query}",
        f"{Fore.CYAN}📊 Bases analysées : {results.get('NumOfDatabase', 'Inconnu')}",
        f"{Fore.CYAN}📈 Résultats : {results.get('NumOfResults', 0)}\n"
    ]
    for category, details in results.get("List", {}).items():
        lines.append(f"{Fore.MAGENTA}🔍 --- {category} ---")
        lines.append(f"{Fore.BLUE}📝 Description : {details.get('InfoLeak', 'Aucune info')}")
        lines.append(f"{Fore.BLUE}🔢 Résultats : {details.get('NumOfResults', 0)}\n")
        for data in details.get("Data", []):
            for field, value in data.items():
                icon = ICON_MAP.get(field.lower(), "🔸")
                lines.append(f"{icon} {field}: {value}")
            lines.append("")
    lines.append(f"{Fore.GREEN}✅ Fin des résultats.\n")
    return "\n".join(lines)

def save_results(text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{Fore.GREEN}💾 Résultats enregistrés dans : {filename}")

def show_info():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{Fore.CYAN}
📘 INFORMATIONS D'UTILISATION :

Ce programme utilise une API pour rechercher des informations dans des bases de données.

⚠️ Règles à respecter :
- Ne jamais utiliser cet outil pour harceler, nuire ou violer la vie privée d'autrui.
- Toute utilisation malveillante est strictement interdite.
- Respectez les lois en vigueur dans votre pays.

✅ Bonnes pratiques :
- Utilisez uniquement pour l'analyse légale, la cybersécurité ou la récupération d'informations vous appartenant.
- Ne conservez pas de données sensibles inutilement.

⚙️ search :
- email
- phone
- name
- nickname
- username
- ID
- domaine
- à peu près tout

{Fore.YELLOW}[ BACK ] : Appuyez sur Entrée pour revenir au menu principal.{Style.RESET_ALL}
""")
    input()
    main()

def launch_search():
    os.system("clear" if os.name == "posix" else "cls")
    print(ASCII_ART)
    query = input(f"{Fore.WHITE}==> search : ").strip()

    if not query:
        print(f"{Fore.RED}❌ Aucune recherche saisie.")
        input("Appuyez sur Entrée pour revenir au menu...")
        return main()

    print(f"\n{Fore.YELLOW}⏳ Recherche en cours...\n")
    results = search_api(query)

    if results.get("success", True):
        output = format_results(query, results)
        print(output)

        save = input(f"{Fore.WHITE}💾 Voulez-vous sauvegarder les résultats ? (y/n) : ").strip().lower()
        if save == "y":
            save_results(output)
    else:
        print(f"{Fore.RED}❌ Erreur : {results.get('error')}")

    input(f"\n{Fore.YELLOW}🔁 Appuyez sur Entrée pour revenir au menu principal...")
    main()

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print(ASCII_ART)
    print(f"{Fore.CYAN}1 - Search")
    print(f"2 - Info")
    print(f"3 - Quitter\n")

    choice = input(f"{Fore.WHITE}==> Choisissez une option (1/2/3) : ").strip()

    if choice == "1":
        launch_search()
    elif choice == "2":
        show_info()
    elif choice == "3":
        print(f"{Fore.GREEN}👋 À bientôt !")
        exit(0)
    else:
        print(f"{Fore.RED}❌ Choix invalide.")
        input("Appuyez sur Entrée pour revenir au menu...")
        main()

if __name__ == "__main__":
    main()
