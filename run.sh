#!/bin/bash
export DATABASE_URL=postgres://fakepay:nAqpcZ3g4ax@localhost:15432/fakepay
gunicorn -w 2 wsgi:app
