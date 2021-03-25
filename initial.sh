#!/usr/bin/env bash
#swap 'virtual_day' on our data
createdb virtual_day;
psql -c "create user virtual_day with password 'virtual_day'";
psql -c 'grant all privileges on database virtual_day to virtual_day';
#sudo rabbitmqctl add_user virtual_day virtual_day
#sudo rabbitmqctl add_vhost virtual_day
#sudo rabbitmqctl set_user_tags virtual_day virtual_day_tag
#sudo rabbitmqctl set_permissions -p virtual_day virtual_day ".*" ".*" ".*"