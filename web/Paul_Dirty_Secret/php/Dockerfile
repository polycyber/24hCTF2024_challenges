FROM php:8.2-apache

RUN apt update -y; \
    apt upgrade -y;


RUN docker-php-ext-install mysqli pdo_mysql

RUN a2enmod rewrite
RUN a2enmod vhost_alias
#RUN a2ensite fun-in-jail.ctf secret-site.ctf

COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf


ADD public_html /var/www/html

EXPOSE 80
#RUN sed -i 's/session.auto_start = 0/session.auto_start = 1/' "$PHP_INI_DIR/php.ini"

