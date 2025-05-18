clear
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
echo "$     98 pentest" && read choix 
if [ $choix == 2 ]; then
    clear
    cd osint
    echo "met le numéro a énumerer format +33612345678"
    read numero
    bash lookup_db.sh $numero
elif [ $choix == 1 ]; then
    clear
    cd osint 
    python3 lookupnaz.py
elif [ $choix == 3 ]; then
    clear
    cd osint 
    python3 snusbase.py
elif [ $choix == 4 ]; then
    clear
    cd osint
    bash lookup_db.sh
elif [ $choix == 98 ]; then
    clear
    bash main_pentest.sh
else
    clear
    bash main_osint.sh
fi                 
