#!/bin/bash
echo "Enter Username"
read username
group="devops"

if id "$username"&>/dev/null;
then
	echo "$username already exists"
	exit 0
fi

useradd -m -s /bin/bash "$username"

if ! getent group "$group" > /dev/null;
then
	echo "creating group '$group'"
	groupadd "$group"
fi

usermod -aG "$group" "$username"

echo "$username created and added to $group"
