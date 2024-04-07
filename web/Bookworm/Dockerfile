# Utilisation d'Ubuntu comme image de base
FROM ubuntu:latest

# Éviter les invites interactives de packages tels que tzdata
ENV DEBIAN_FRONTEND=noninteractive

# Installation des packages nécessaires
RUN apt-get update && apt-get install -y \
    nano apache2 php libapache2-mod-php php-mysql mysql-server cron tar && \
    rm -rf /var/lib/apt/lists/*

# Activation des modules Apache nécessaires et configuration du dossier uploads et logs
RUN a2enmod rewrite && \
    mkdir -p /var/www/html/uploads && \
    chown -R www-data:www-data /var/www/html/uploads && \
    chmod 755 /var/www/html/uploads && \
    touch /var/www/html/request_logs_8idfJwio2.txt && \
    chown -R www-data:www-data /var/www/html/request_logs_8idfJwio2.txt && \
    chmod 755 /var/www/html/request_logs_8idfJwio2.txt

# Configuration pour autoriser .htaccess overrides dans le dossier uploads
RUN echo '<FilesMatch "\.(php|php5|php4|php3|php2|phtml)$">\nSetHandler application/x-httpd-php\n</FilesMatch>\nOptions -Indexes' > /var/www/html/uploads/.htaccess && \
    echo '<Directory /var/www/html/uploads>\nAllowOverride All\n</Directory>' > /etc/apache2/conf-available/uploads.conf && \
    a2enconf uploads

RUN chmod 644 /var/www/html/uploads/.htaccess

# Copie des fichiers et scripts dans l'image
COPY src_site/ /var/www/html/
COPY scripts/init_db.sql /docker-entrypoint-initdb.d/
COPY scripts/entrypoint.sh /usr/local/bin/
COPY src_misc/ /var/www/

RUN chmod +x /usr/local/bin/entrypoint.sh && \
    chmod 444 /var/www/flag.txt && \
    chmod 444 /var/www/Log_Maintenance.txt && \
    chmod 444 /var/www/Maintenances.png

# Sécurisation du répertoire initdb
RUN chown root:root /docker-entrypoint-initdb.d && \
    chmod 700 /docker-entrypoint-initdb.d

# Exposition du port 80
EXPOSE 80

# Configuration du point d'entrée
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["apache2ctl", "-D", "FOREGROUND"]
