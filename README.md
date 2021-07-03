# Big Data Project on german Internet domains

## Introduction
In the following project we have been analyzing a data set of 4.860.885 data points of Internet domains in Germany, which have been scraped in december 2020.

## Description

## Installation Setup

Folgende Programme müssen installiert werden
-Docker
-Docker-compose


Beispielhaft erfolgt die Installation auf Fedora wie folgt
```
sudo dnf install dnf-plugins-core  
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo  
sudo dnf install docker-ce docker-ce-cli containerd.io  
sudo dnf install docker-compose
```
Siehe auch https://developer.fedoraproject.org/tools/docker/docker-installation.html  

 
Starten des Containers
```
sudo systemctl start docker
```
docker-compose.yaml und nginx.conf in gewünschtem Pfad ablegen, um daraufhin docker-compose aufzurufen
```
sudo docker-compose up  
```
Hiermit werden alle Container gestartet  

Danach können Sie Jupyter Notebook mit dem entsprechenden Link öffnen. Dieser steht in dem Terminal nach folgender Ausgabe: To access the notebook, open this file in a browser: xxx Or copy and paste one of these URLs: xxx

Aufrufen von   
http://localhost:9000  
http://127.0.0.1:8888   

Führen Sie den folgenden Befehl aus  
```
sudo docker exec -it bde2020-minio-mc /bin/sh   

mc config host add minio http://minio1:9000 minio minio123 --api S3v4   
mc mb minio/bucket  
mc policy set public minio/bucket  
```

Zum Einlesen der Datei real_domains wird als Seperator ein Semikolon gewählt:
```
sudo apt install csvkit
csvformat -D ";" <Pfad der Datei>/real_domains.csv > real_new.csv 
```
damit wird der delimeter der Datei zu Semikolon geändert um sie problemlos in spark einlesen zu können.

Im Browser in "http://localhost:9000" in bucket die Datei "real-new.csv" hochladen. Rechtsklick über bucket und Edit policy in Read and write und addieren.
Daraufhin müssen im bucket alle weiteren benötigten csv-files hochgeladen werden:
GeoLite2-Country-Locations-en.csv
GeoLite2-Country-Blocks-IPv4.csv
GeoLite2-ASN-Blocks-IPv4.csv

Die Datei BDA_2.ipynb in Jupyter aufrufen und runnen.


## Technologies

Docker   
Pandas    
Python   
PySpark    
Seaborn   


## License
The project is licensed with the GNU General public license. See license.txt for more information. 


## Team members
Daniel Eben, Laura Rücker, Miriam Schneider





