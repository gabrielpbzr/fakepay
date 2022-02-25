import sqlite3


class DatabaseHelper:
    def __init__(self, db_url: str) -> None:
        self.connection = sqlite3.connect(db_url)
        sql = """
        CREATE TABLE IF NOT EXISTS pagamentos(
            id VARCHAR(22) NOT NULL PRIMARY KEY, 
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            situacao TEXT DEFAULT 'CRIADO',
            valor NUMERIC(18,2) NOT NULL,
            servico_pagamento TEXT,
            id_transacao TEXT
        );
        """
        self.connection.execute(sql)
        self.connection.commit()
