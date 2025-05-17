echo " ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓    ▄████▄    ██████  ██▓ ███▄    █ ▄▄▄█████▓"
echo "▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▒██▀ ▀█  ▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒"
echo "▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ▒▓█    ▄ ░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░"
echo "▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▒▓▓▄ ▄██▒  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ "
echo "░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░    ▒ ▓███▀ ░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ "
echo "░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░      ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░"
echo "  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░         ░  ▒   ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░"
echo "░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░        ░  ░  ░   ▒ ░   ░   ░ ░   ░"
echo "    ░ ░        ░   ░           ░             ░ ░            ░   ░           ░"
echo "                                             ░"
echo "+---------------+--------------+-------------+-----------+"
echo "+ lookup nazapi / lookup phone / lookup snus / lookup db +" 
echo "+---------------+--------------+-------------+-----------+"
echo "+       1       /       2      /      3      /      4    +"
echo "+---------------+--------------+-------------+-----------+"
echo "$" && read choix
if [ $choix == 2 ]; then
    clear
    echo "met le numéro a énumerer format +33612345678"
    read numero
    ./osint/lookup_db.sh $numero
elif [ $choix == 1 ]; then
    clear 
    python3 /osint/lookupnaz.py
elif [ $choix == 3 ]; then
    clear 
    python3 /osint/snusbase.py
elif [ $choix == 4 ]; then
    clear
    ./osint/lookup_db.sh
else
    clear
    ./main_osint.sh
fi                 
