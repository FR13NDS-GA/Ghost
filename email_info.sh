#!/bin/bash

# Check if the user provided an email address as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <EMAIL_ADDRESS>"
  exit 1
fi

EMAIL_ADDRESS=$1

# Extract the domain from the email address
DOMAIN=$(echo $EMAIL_ADDRESS | awk -F '@' '{print $2}')

# Check domain information using whois
echo "Gathering WHOIS information for the domain: $DOMAIN..."
whois $DOMAIN

# Perform DNS lookup for MX records (Mail Exchange servers)
echo ""
echo "Fetching MX (Mail Exchange) records for $DOMAIN..."
dig MX $DOMAIN +short

# Verify if domain has SPF (Sender Policy Framework) records
echo ""
echo "Checking for SPF records for $DOMAIN..."
dig TXT $DOMAIN +short | grep 'v=spf1'

# Check email reputation using emailrep.io API (replace YOUR_API_KEY with an actual API key)
echo ""
echo "Fetching email reputation from emailrep.io..."
curl -s "https://emailrep.io/$EMAIL_ADDRESS" -H "Key: YOUR_API_KEY"

# Perform basic email format validation (this is just a simple regex check, not a guarantee of validity)
echo ""
echo "Validating email format for $EMAIL_ADDRESS..."
if [[ $EMAIL_ADDRESS =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Email format is valid."
else
    echo "Email format is invalid."
fi

# Check the domain blacklist status using a public API (optional)
echo ""
echo "Checking domain blacklist status (using DNSBL lookup)..."
for blacklist in zen.spamhaus.org b.barracudacentral.org bl.spamcop.net; do
    echo -n "Checking $DOMAIN against $blacklist: "
    dig +short $DOMAIN.$blacklist
done
