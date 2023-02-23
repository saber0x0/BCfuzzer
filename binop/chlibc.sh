#!/bin/zsh

if [[ $1 = "--help" ]] || [[ $1 = "-h" ]] || [[ $1 = "" ]]
then
    echo "--------------------"
    echo "arg1: libc版本"
    echo "arg2: 32 or 64"
    echo "arg3: binary path"
    echo "such as: sl 2.23 64 ./pwn"
    echo "--------------------"
    exit 0
fi

message="请查看帮助 -h (--help)"

case $1 in
"2.23")
    if [ $2="64" ]
    then
        ld="/glibc/2.23-0ubuntu11.3_amd64/ld-2.23.so"
        libc="/glibc/2.23-0ubuntu11.3_amd64/libc-2.23.so"
    elif [ $2="32" ]
    then
        ld="/glibc/2.23-0ubuntu11.3_i386/ld-2.23.so"
        libc="/glibc/2.23-0ubuntu11.3_i386/libc-2.23.so"
    else
        echo $message
    fi
;;
"2.27")
    if [ $2="64" ]
    then
        ld="/glibc/2.27-3ubuntu1_amd64/ld-2.27.so"
        libc="/glibc/2.27-3ubuntu1_amd64/libc-2.27.so"
    elif [ $2="32" ]
    then
        ld="/glibc/2.27-3ubuntu1.2_i386/ld-2.27.so"
        libc="/glibc/2.27-3ubuntu1.2_i386/libc-2.27.so"
    else
        echo $message
    fi
;;
"2.29")
    if [ $2="64" ]
    then
        ld="/glibc/2.29/64/lib/ld-2.29.so"
        libc="/glibc/2.29/64/lib/libc-2.29.so"
    elif [ $2="32" ]
    then
        ld="/glibc/2.29/32/lib/ld-2.29.so"
        libc="/glibc/2.29/32/lib/libc-2.29.so"
    else
        echo $message
    fi
;;
"2.31")
    if [ $2="64" ]
    then
        ld="/glibc/2.31/64/lib/ld-2.31.so"
        libc="/glibc/2.31/64/lib/libc-2.31.so"
    elif [ $2="32" ]
    then
        ld="/glibc/2.31/32/lib/ld-2.31.so"
        libc="/glibc/2.31/32/lib/libc-2.31.so"
    else
        echo $message
    fi
;;
*)
echo $message
;;
esac

figlet -f small "Switch the  libc"
echo -e "\033[1;32mld-path:$ld\033[0m"
echo -e "\033[1;32mlibc-path:$libc\033[0m"
figlet -f small "Switch the  libc"

patchelf --set-interpreter $ld $3
LD_PRELOAD=$libc $3
exit 0