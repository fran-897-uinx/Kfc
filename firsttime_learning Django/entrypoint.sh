#!/bin/bash
KYC_PORT=${PORT:-8000} 

cd /app/

/opt/env/Scripts/gunicorn --worker-tmp-dir /dev/shm kyc.wsgi:application --bind "0.0.0.0:${KYC_PORT}"