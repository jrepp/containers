# Remove all containers that are currently exited
docker rm $(docker ps -qaf status=exited)
