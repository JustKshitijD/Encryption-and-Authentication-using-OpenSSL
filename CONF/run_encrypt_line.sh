#!/bin/bash
input="encrypt_line"
while IFS= read -r line
do
  #echo "Heyyyyy"		
  echo "$line"
  $line
done < "$input"

