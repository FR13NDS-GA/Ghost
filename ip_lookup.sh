#!/bin/bash

# Check if the user provided an IP address as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <IP_ADDRESS>"
  exit 1
fi

IP_ADDRESS=$1

# Gather basic information using whois
echo "Gathering WHOIS information for $IP_ADDRESS..."
whois $IP_ADDRESS

# Get IP location info using an external API (ipinfo.io)
echo ""
echo "Fetching location and other details using ipinfo.io..."
curl -s https://ipinfo.io/$IP_ADDRESS

# Perform DNS lookup using dig
echo ""
echo "Performing DNS lookup for $IP_ADDRESS..."
dig -x $IP_ADDRESS +short

# Ping the IP to check if it's reachable
echo ""
echo "Pinging $IP_ADDRESS..."
ping -c 4 $IP_ADDRESS

# Trace the route to the IP
echo ""
echo "Tracing the route to $IP_ADDRESS..."
traceroute $IP_ADDRESS

# Get open ports (optional: requires nmap)
if command -v nmap &> /dev/null
then
  echo ""
  echo "Scanning for open ports using nmap..."
  nmap -Pn $IP_ADDRESS
else
  echo ""
  echo "nmap is not installed. Skipping port scan."
fi
