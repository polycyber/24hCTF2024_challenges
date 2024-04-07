#!/bin/bash

# Start MySQL service
service mysql start

# Wait for MySQL to be ready
while ! mysqladmin ping -h localhost --silent; do
    sleep 1
done

# Execute the SQL initialization scripts
for script in /docker-entrypoint-initdb.d/*.sql; do
    mysql < "$script"
done

# Proceed to start Apache in the foreground
exec apache2ctl -D FOREGROUND