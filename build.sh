#!/usr/bin/env bash
# Salir si hay un error
set -o errexit

# Instalar dependencias (incluyendo la versión parcheada de djongo)
pip install git+https://github.com/doableware/djongo.git
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones
python manage.py migrate