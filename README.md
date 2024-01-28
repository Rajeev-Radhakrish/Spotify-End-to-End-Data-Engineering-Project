# Spotify End-to-End-Data-Engineering-Project
Building an ETL (Extract, Transform, Load) data pipeline using Spotify API on AWS. The pipeline will extract data from the API, transform into desired format and load into AWS Storage.

## Introduction
Imagine you have a client who is a music composer and wants to understand more about the current music industry.
- Client wants to analyse what kind of songs & albums are trending
- Find some patterns over the data
- Compose music based on the analysis trends
- To carry out all these, client needs a large dataset of Spotify Top songs-Global spanning over a period of time.

![Top Songs-Global](https://github.com/Rajeev-Radhakrish/spotify-end-to-end-data-engineering-project/blob/main/Top%20Songs%20-%20Global.png)

## Objective
- Spotify API integration to extract data
- Deploying code on AWS Lambda for Data Extraction
- Connecting trigger to run the extraction automatically
- Writing transformation function & Building automated trigger on transformation function
- Store files securely on Amazon S3
- Building Analytics Tables on data files using Glue and Athena

## Architecture Diagram
![Architecture Diagram](https://github.com/Rajeev-Radhakrish/spotify-end-to-end-data-engineering-project/blob/main/Data%20Architecture.png)

## About Dataset/API
This API contains information about music artists, albums and songs - [Spotify API](https://developer.spotify.com/documentation)

## Services used
1. **S3 (Simple Storage Service):** Amazon S3 is a highly scalable object storage service that can store and retrieve any amount of data from web.
2. **AWS Lambda:** Lambda is a computing service that allows programmers to run code without creating or managing servers.
3. **Cloud Watch:** It is a monitoring service for resources and application. Used to collect and track metrics, monitor log files and set alarms.
4. **Glue Crawler:** A fully managed service that automatically crawls data sources, identifies data formats, schemas to create AWS Glue Data Catalog.
5. **Data Catalog:** AWS Glue Data catalog is a fully managed metadata repository for easy discovering and managing of data.
6. **AWS Athena:** An interactive query service to analyse data in Amazon S3 using standard SQL.

## Package installation
```
pip install pandas
pip install numpy
pip install spotipy
```
## Flow of Execution
Extract data from API -> Lambda Trigger -> Run Extract Code -> Store Raw data -> Trigger transform function -> Transform Data and Loading it -> Query using Athena
