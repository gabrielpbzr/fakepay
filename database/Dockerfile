FROM postgres:11.3-alpine

USER ${user}
ENV POSTGRES_PASSWORD rIVipG9YqN5
# Copia o script de inicialização do banco de dados
COPY init-db.sh /docker-entrypoint-initdb.d/

EXPOSE 5432