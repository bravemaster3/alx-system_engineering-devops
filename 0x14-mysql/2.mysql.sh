#!/usr/bin/env bash

# MySQL Connection Details
MYSQL_ROOT_USER="root"
MYSQL_ROOT_PASSWORD="$1"

# MySQL Commands
MYSQL_COMMAND="mysql -u$MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e"

# Create database
$MYSQL_COMMAND "CREATE DATABASE IF NOT EXISTS tyrell_corp;"

# Create table
$MYSQL_COMMAND "USE tyrell_corp; CREATE TABLE IF NOT EXISTS nexus6(
    name VARCHAR(255),
    birthdate DATE
);"

# Adding one entry to the table
$MYSQL_COMMAND "USE tyrell_corp; INSERT INTO nexus6 (name, birthdate) VALUES ('John Doe', '1993-03-27');"
