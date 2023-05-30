#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -e

if [ "x$INIT_DB_DATA" = 'xon' ]; then
  echo "==> Running init db data"
  python app/initial_data.py
fi

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

exec "$@"