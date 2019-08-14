# Data-Pipelines-using-Airflow

**Introduction**:
This Project is mainly to create automated data pipelines using Apache Airflow.
		
The music streaming startup Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

We would create custom operators to perform tasks like staging the data and loading into datawarehouse, Also running checks on the data as the final step. 

**Datasets**:
We are provided JSON files that are in AWS S3 Bucket below are the 2 parts.

**Song Dataset:** s3://udacity-dend/song_data

    `{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}`

**Log Dataset:** s3://udacity-dend/log_data Log Data


