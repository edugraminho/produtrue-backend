Refazer as migracoes:

docker container rm verit4s-backend-db-1
docker volume rm verit4s-backend_pgdata
docker-compose up db
