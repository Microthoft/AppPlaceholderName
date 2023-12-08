@echo off

CALL .venv\Scripts\activate
CALL python manage.py runserver

PAUSE