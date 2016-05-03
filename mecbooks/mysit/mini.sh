#!/bin/bash

#COMMENTS
#use ./mini.sh "query"   :can use query with spaces like "to kill a mockingbird" 

query=$1

# sleep 10
# echo $query
var=$(echo $query | sed 's/ /%20/g')
echo query
echo $var
lynx -dump -listonly "http://www.google.com/search?complete=0&num=5&hl=en&complete=0&site=webhp&source=hp&q=$var%20pdf&start=0" > hello.text

grep -o 'q=.*pdf' hello.text | grep "http" | grep "[.]pdf$" |sed '/related/d'|sed 's/q=/ /' > res.text

# subl res.text