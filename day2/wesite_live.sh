#!/bin/bash
echo "Enter Website To Check Availability";
read site;
if curl --silent --fail "$site">/dev/null;
then
	echo "$site is accessible"
else
	echo "$site is not live"
fi
