#!/bin/bash

sudo apt-get update -y  
sudo apt-get install apache2 -y  
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password vpark'  
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password vpark'  
sudo apt-get -y install mysql-server  
sudo apt-get install -y software-properties-common  
sudo add-apt-repository ppa:ondrej/php -y  
sudo apt-get update -y
sudo apt-get install php5.6 php5.6-mysql php-xdebug libapache2-mod-php5.6 php5.6-mbstring -y  
sudo wget https://raw.githubusercontent.com/DrVoyager/EdGENI/master/Scripts/Nmap/phpinfo.php 
sudo mv phpinfo.php /var/www/html/phpinfo.php 
