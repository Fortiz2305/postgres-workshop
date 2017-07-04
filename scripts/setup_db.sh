# createdb ${POSTGRES_DB} -h db -w -U postgres -O postgres
echo 'creating db'
export PGPASSWORD=${POSTGRES_PASSWORD}
psql -h db -w -U ${POSTGRES_USER} -f /code/scripts/setup.sql
