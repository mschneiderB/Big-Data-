# Big Data Project on german Internet domains

## Introduction
In the following project we have been analyzing a data set of 4.860.885 data points of Internet domains in Germany, which have been scraped in december 2020.

## Description

## Installation Setup

Folgende Programme müssen installiert werden
-Docker
-

Beispielhaft erfolgt die Installation auf Fedora wie folgt

sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io
Siehe auch https://developer.fedoraproject.org/tools/docker/docker-installation.html


Starten des Containers
sudo systemctl start docker

docker-compose.yaml und nginx.conf in gewünschten Pfad ablegen, um daraufhin docker-compose aufzurufen

sudo docker-compose up
Hiermit werden alle Container gestartet

Aufrufen von
http://localhost:9000
http://127.0.0.1:8080
http://127.0.0.1:8888 

Führen Sie den folgenden Befehl aus
sudo docker exec -it bde2020-minio-mc /bin/sh 

mc config host add minio http://minio1:9000 minio minio123 --api S3v4 
mc mb minio/bucket 
mc policy set public minio/bucket 

in Browser in "http://localhost:9000" in bucket die Datei "real-domains.csv" hochladen. Rechtsklick über bucket und Edit policy in Read an write und addieren

Die Datei ..ipynb in Jupyter aufrufen und runnen.




Installation on windows



## Technologies

Docker 20.10.7

Pandas
Python 3.9.5
PySpark

## Launch

## License
The project is licensed with the GNU General public license. See license.txt for more information. 


## Team members
Daniel, Laura, Miriam





