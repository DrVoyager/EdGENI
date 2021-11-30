#!/bin/bash

sudo apt-get update -y
sudo debconf-set-selections <<< "postfix postfix/mailname string example.com"
sudo debconf-set-selections <<< "postfix postfix/main_mailer_type string 'Internet Site'"
sudo apt-get install -y postfix
sudo apt-get install -y mailutils
sudo apt-get update -y
