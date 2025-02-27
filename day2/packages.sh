#!/bin/bash
mypackages=("curl" "vim" "httpd")
for pkg in ${mypackages[@]}; do
	if rpm -q "$pkg">/dev/null;
	then 
		echo "$pkg is already installed"
	else
		yum install -y $pkg
	fi
done
