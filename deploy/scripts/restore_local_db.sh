#!/usr/bin/env bash
set -x
set -e
createdb $2
gunzip $1
NAME=$1
CLEAN_NAME="${NAME/.gz/}"
db_user=${DB_USER:-promonster}
echo "Creating db"
cat $CLEAN_NAME | psql $2 -U $db_user
