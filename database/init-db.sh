#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER fakepay WITH password 'nAqpcZ3g4ax' LOGIN;
    CREATE DATABASE fakepay;
    GRANT ALL PRIVILEGES ON DATABASE fakepay TO fakepay;
EOSQL