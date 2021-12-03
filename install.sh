#!/bin/bash
WHITE=('\033[38;5;15m');
GREEN=('\033[38;5;10m');
PURPLE=('\033[38;5;93m');
DARK=('\033[38;5;245m');
BLUE=('\033[38;5;50m');
RED=('\033[38;5;9m');
BOLD=('\033[01m');
if [[ ${UID} != 0 ]]; then
    echo -e "${RED}Run this script with sudo to complete the installation"
    exit
fi
if [[ -f ./py2marshal.py ]]; then
    if [[ -d /bin ]]; then
        echo -e "${GREEN}Linux${WHITE}: ${BLUE}Installing ${PURPLE}pymarshal.py ${BLUE}to ${GREEN}/bin/${PURPLE}pymarshal"
        echo -e "${BLUE}To run it${WHITE}, ${BLUE}just type ${WHITE}'${GREEN}pymarshal${WHITE}'"
        sudo cp py2marshal.py /bin/py2marshal
    elif [[ -d /data/data/com.termux ]]; then
        echo -e "${GREEN}Termux${WHITE}: ${BLUE}Installing ${PURPLE}pymarshal.py ${BLUE}to ${GREEN}/bin/${PURPLE}pymarshal"
        echo -e "${BLUE}To run it${WHITE}, ${BLUE}just type ${WHITE}'${GREEN}pymarshal${WHITE}'"
        cp py2marshal.py /data/data/com.termux/files/usr/bin
    else
        echo -e ${RED}"No /bin. Not using Linux ? Come back later for a better installer that'll work with your operating system."
    fi
fi
if [[ -d /usr/share/bash-completion ]]; then 
    sudo cp py2marshal.completion /usr/share/bash-completion/completions
elif [[ -d /data/data/com.termux/files/usr/share/bash-completion ]]; then 
    cp py2marshal.py /data/data/com.termux/files/usr/share/bash-completion/completions
else
    echo -e ${RED}"No bash completion installed. Cannot install the tab completion script right now."
fi