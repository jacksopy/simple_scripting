echo " ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███     ▓█████▄  ▄▄▄▄"
echo "▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒   ▒██▀ ██▌▓█████▄"
echo "▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒   ░██   █▌▒██▒ ▄██"
echo "▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒   ░▓█▄   ▌▒██░█▀"
echo "░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░   ░▒████▓ ░▓█  ▀█▓"
echo "░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░    ▒▒▓  ▒ ░▒▓███▀▒"
echo "░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░         ░ ▒  ▒ ▒░▒   ░"
echo "  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░           ░ ░  ░  ░    ░"
echo "    ░  ░    ░ ░      ░ ░  ░  ░      ░                    ░     ░"
echo "met la valeur a rechercher"
read recherche
cd db
cat * | grep $recherche
