#!/bin/sh

set -e

if [ -z "$PGHOST" ] || [ -z "$PGUSER" ] || [ -z "$PGPASSWORD" ] || [ -z "$PGDATABASE" ]; then
  echo "Error: One or more required environment variables are missing."
  echo "Required: PGHOST, PGUSER, PGPASSWORD, PGDATABASE"
  exit 1
fi

export PGPASSWORD=$PGPASSWORD

BACKUP_FILE="/backup/db-$(date +%F).sql"

echo "Starting backup of $PGDATABASE from $PGHOST to $BACKUP_FILE"

pg_dump -h "$PGHOST" -U "$PGUSER" "$PGDATABASE" > "$BACKUP_FILE"

echo "Backup completed."