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

![](https://raw.githubusercontent.com/vijaypasham/Data-Pipelines-using-Airflow/master/Files/DEND-logdata-20190814.png)

### Process

The Airflow data pipeline process is intended to process the raw data and model it into a data warehouse to facilitate the analytics team to gain insight into their users' behavior.

![](https://raw.githubusercontent.com/vijaypasham/Data-Pipelines-using-Airflow/master/Files/dag.png)

Airflow DAG executes the following steps:

-   Copy source data from S3 to staging tables
-   Transform data from staging tables to fact table and dimension tables
-   Run data quality checks to ensure that all data in fact table and dimension tables is correct and clean.

Output: JSON data is processed and analysed data is loaded into Fact and Dimensions tables in AWS Redshift.

#### Setup
 -  Set up Amazon Redshift data warehouse
 -  Run SQL queries from  `create_tables.sql`  file if the data warehouse has not been created yet
 - Configure Airflow connections with Amazon credentials
    -   `Conn Id`  =  `aws_credentials`
    -   `Conn Type`  =  `Amazon Web Services`
    -   `Login`  =  `Access key ID`  for the IAM User
    -   `Password`  =  `Secret access key`  for the IAM User
  - Configure the Airflow connections with the Redshift credentials
	  -    `Conn Id`:  `redshift`
	  -    `Conn Type`:  `PostgreSQL`
	  -    `Host`: Redshift cluster endpoint
	  -    `Schema`: Database name
	  -    `Login`: Username with privileges on the database
	  -    `Password`: Database password
	  -    `Port`: Redshift port (`5439`)