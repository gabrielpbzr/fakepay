#!*-* coding: UTF-8 *-*
"""
 Módulo para carregar as configurações do ambiente
"""
import os


def database_url():
    return read_value("DATABASE_URL")


def read_value(key: str):
    """
    Busca um valor na configuração de ambiente

    params: 
        key: str
    """
    return os.environ.get(key)
