# Run Python app in a docker container

This example is using Python installed on Alpine Linux, a minimalist Linux distro, which helps keep the images for Docker small **(~ 100 MB image)**. Refer the docker file which is kept in the folder 2.web-api

RUN directive that is calling PyPi (pip) and pointing to the requirements.txt file. This file is listing all the dependencies that the application needs to run.

EXPOSE exposes the port 8080, that is used by Flask framework mentioned in app.py

> Note: The flask framework in python needs to be configured with host as '0.0.0.0' (see in app.py) for it to bind with the host interace. If missing, it will only bind with the container interface and can't be accessed from the host machine.

To build the image, run Docker build from a command line or terminal that is in the root directory of the application. First of all, “tag” the image abs-python-app-image and build it. After it is built, you can run the image as a container.
```cmd
docker build --tag <image_name> .
Eg:
docker build --tag abs-python-app-image .
```
Next, bind port 8080 of the container to port 80 on 127.0.0.1 of the host machine.
```cmd
docker run --name <container_name> -p <host_port>:<container_port> <image_name>
Eg:
docker run --name python-app-container -p 80:8080 abs-python-app-image
```

To log into the running container
```cmd
docker exec -it python-app sh
```

To invoke the API, browse the endpoint - http://localhost/subscriptions