# Docker and webstack debugging

Here are some tips for docker images

+ Start the container, map 80 port of the container to 8080 of the host
```bash
sudo docker run -p 8080:80 -d -it holbertonschool/265-0
```

+ log into the shell of the docker container knowing its id
```bash
sudo docker exec -it 4fa7df550230 /bin/bash
```

+ Listing all running docker containers
```bash
sudo docker ps
```

+ Get the id f the latest container
```bash
container_id=$(sudo docker ps -l -q)
```
+ Retart apache2 service remotely in the docker container, also appending ServerName localhost, to avoid a warning about a strange IP address
```bash
sudo docker exec "$container_id" bash -c 'echo "ServerName localhost" >> /etc/apache2/apache2.conf && service apache2 start'
```

+ You can also suppress the warning instead?
```bash
sudo docker exec "$container_id" service apache2 restart 2>/dev/null
```

+ query the root, to display the default page
```bash
sudo curl 0:8080
```


