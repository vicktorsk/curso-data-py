docker build -t cluster-apache-spark:3.0.2 .


docker-compose up -d
docker ps
docker images

8. Abrir el navegador

http://localhost:9090

docker-compose logs

/*
docker images -q
docker-compose ps
docker volume ls
docker network ls
docker-compose down
docker rmi 36ff18d21807
docker volume prune
docker network prune
docker system prune
*/