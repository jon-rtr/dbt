set -x

createdb dbt
psql -c "CREATE ROLE root WITH PASSWORD 'password';" -U postgres
psql -c "ALTER ROLE root WITH LOGIN;" -U postgres
psql -c "GRANT CREATE, CONNECT ON DATABASE dbt TO root;" -U postgres

psql -c "CREATE ROLE noaccess WITH PASSWORD 'password' NOSUPERUSER;" -U postgres;
psql -c "ALTER ROLE noaccess WITH LOGIN;" -U postgres
psql -c "GRANT CONNECT ON DATABASE dbt TO noaccess;" -U postgres;

set +x
