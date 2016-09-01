#!/usr/bin/bash



SQL_PASSWORD=$(cat ~/.my.cnf | grep -m 1 password | tr -d "'" | tr -d "password=")
echo ""

while true; 
    do
    echo -n "Volume ID (Ctrl+C for exit) -> "; read VOLUME_ID
    echo ""
    mysql -u root --password=$SQL_PASSWORD -D cinder -e "update volumes set deleted=1,status='deleted',deleted_at=now(),updated_at=now() where deleted=0 and id='$VOLUME_ID';";
    done
