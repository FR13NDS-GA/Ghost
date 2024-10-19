read -p "Enter target HTTP: " target
read -p "Enter wordlist directory: " wordlist_dir

gobuster dir -u $target -w $wordlist_dir -t 10 -x txt,html,php,js
while IFS= read -r line; do
    echo "$line"
done < <(gobuster dir -u $target -w $wordlist_dir -t 10 -x txt,html,php,js)
