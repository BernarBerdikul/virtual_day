#!/usr/bin/env bash
#swap 'db' on our data
createdb db;
psql -c "create user db with password 'db'";
psql -c 'grant all privileges on database menushka to menushka';
sudo rabbitmqctl add_user db db
sudo rabbitmqctl add_vhost db
sudo rabbitmqctl set_user_tags db db_tag
sudo rabbitmqctl set_permissions -p db db ".*" ".*" ".*"
mkdir logs;