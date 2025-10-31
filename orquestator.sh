#!/bin/bash


read -p "Introduce la IP víctima: " TARGET


IPval='([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
	if [[ $TARGET =~ ^$IPval\.$IPval\.$IPval\.$IPval$ ]]; then
		echo -e "\e[1;39m IP válida: "$TARGET
	else
		echo -e "\e[1;31m IP no válida: "$TARGET
	exit
	fi
done

sleep 2


nmap -sCV -p- --open -Pn -n $TARGET -oX result.xml

sleep 5


echo -e "\e[1;39m Escaneo a ${TARGET} Completado"

sleep 3

echo "Se ha guardado el resultado como result.xml"


searchsploit --nmap result.xml


sleep 3

echo -e "\e[1;39m Script finalizado correctamente :)"
