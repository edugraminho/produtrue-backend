## Rodar localhost



## Refazer as migracoes:

docker container rm produtrue-backend-db-1
docker volume rm produtrue-backend_pgdata
docker-compose up db



## Para servidores novos

Capturar o IP externo do servidor.
`curl -4 ifconfig.me` 
ou 
`curl https://api.ipify.org` 

Adicionar o IP externo no TIPO A no DNS da página (godaddy)



## Conectar ao servidor 

`sudo ssh -i produtrue-rsa.pem ubuntu@18.228.11.42`