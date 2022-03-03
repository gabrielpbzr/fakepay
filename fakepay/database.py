import sqlite3

import psycopg2


class DatabaseHelper:
    def __init__(self, db_url: str) -> None:

        if db_url:
            self.connection = psycopg2.connect(db_url)
        else:
            self.connection = sqlite3.connect("file::memory:?cache=shared", uri=True)
        sql = """
        CREATE TABLE IF NOT EXISTS pagamentos(
            id VARCHAR(22) NOT NULL PRIMARY KEY, 
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            situacao TEXT DEFAULT 'CRIADO',
            valor NUMERIC(18,2) NOT NULL,
            servico_pagamento TEXT,
            id_transacao TEXT
        );
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
