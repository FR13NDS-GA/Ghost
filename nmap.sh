#!/bin/bash

read -p "Enter IP address: " ip_
nmap -sC -sV -Pn -v $ip_
echo "Nmap scan results for $ip_:"
echo "$output"
