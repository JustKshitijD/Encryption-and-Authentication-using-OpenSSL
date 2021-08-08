#!/bin/bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:1024 -out private-key.pem
openssl pkey -in private-key.pem -out public-key.pem -pubout