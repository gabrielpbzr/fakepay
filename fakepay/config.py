#!*-* coding: UTF-8 *-*
"""
 Módulo para carregar as configurações do ambiente
"""

import os
import re

"""Credenciais do banco de dados"""
database = {
    'host': '',
    'port': '',
    'user': '',
    'password': '',
    'dbname': ''
}


def load_values():
    db_url = read_value("DATABASE_URL")
    if not db_url:
        return
    # Divide em partes a url: //user, password@hostname, port/database
    db_url = db_url.split(':')[1:]

    user = db_url[0].replace("//", "")
    database['user'] = user

    password_host = db_url[1].split('@')
    database['password'] = password_host[0]
    database['host'] = password_host[1]

    port_database = db_url[2].split('/')
    database['port'] = port_database[0]
    database['dbname'] = port_database[1]

    print(database)


def read_value(key: str) -> str:
    """
    Busca um valor na configuração de ambiente

    params:
        key: str
    """
    value = os.environ.get(key)
    if not value:
        return ""
    return value
