#! /bin/sh

cd /src/ || exit

# Run migrations
echo "MIGRATING" && python manage.py migrate

exec "$@"
