#/bin/bash 

playerctl --follow metadata --format '{{ artist }} - {{ title }}'
