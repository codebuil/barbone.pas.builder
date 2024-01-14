printf "\ec\e[43;37m\n"
rm kernel.bin 2>/tmp/null
rm /tmp/kernel.o 2>/tmp/null
rm ppas.sh /tmp 2>/tmp/null
mv link.res /tmp 2>/tmp/null
nasm -felf32 -o /tmp/boot.o ./file/boot.s
fpc -Cn -CcCDECL -O2 -Xs -Xs -Xt -Pi386 -Tlinux  kernel.pas 
mv ppas.sh /tmp 2>/tmp/null
mv link.res /tmp 2>/tmp/null
mv ./kernel.o /tmp
gcc ./file/link.ld /tmp/boot.o /tmp/kernel.o -o /tmp/kernel.bin -nostdlib
mv /tmp/kernel.bin ./
