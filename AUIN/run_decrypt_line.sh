#!/bin/bash
input="decrypt_line"
while IFS= read -r line
do
  #echo "Heyyyyy"		
  echo "$line"
  $line
done < "$input"

