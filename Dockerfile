FROM nginx
MAINTAINER Wilf Huang "wilf.huang@gtedx.com"

RUN apt-get update -y && apt-get install -y php5.6-fpm php5.6-intl php-apc php5.6-gd php5.6-intl php5.6-mysqlnd php5.6-pgsql php-pear php5.6-cli curl php5.6-curl \
  libcurl3 libcurl3-dev && rm -rf /var/lib/apt/lists/*

# Once we start using PHP, it will dictate the use of www-data, so use that instead of nginx
RUN sed -i 's/user  nginx/user  www-data/g' /etc/nginx/nginx.conf

# Force PHP to log to nginx
RUN echo "catch_workers_output = yes" >> /etc/php5.6/fpm/php-fpm.conf

# Enable php by default
ADD default.conf /etc/nginx/conf.d/default.conf
ADD h5api.conf /etc/nginx/conf.d/h5api.conf

CMD service php5.6-fpm start && nginx -g "daemon off;"