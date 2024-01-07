printf "\ec\e[43;37m\a\n\n"
llc $1 -o /tmp/temp
cat /tmp/temp
