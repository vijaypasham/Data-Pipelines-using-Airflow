from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # redshift_conn_id=your-connection-name
                 redshift_conn_id="",
                 aws_credentials_id="",
                 region="",
                 table="",
                 s3_bucket="",
                 s3_key="",
                 json="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.json = json
        self.aws_credentials_id = aws_credentials_id
        self.region = region

    def execute(self, context):
        self.log.info('StageToRedshiftOperator not implemented yet')
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Copying data from S3 to Redshift")

        copy_to_redshift = ("""
                                copy {0}
                                from 's3://{1}/{2}'
                                access_key_id '{3}' secret_access_key '{4}'
                                compupdate off region '{5}'
                                FORMAT AS JSON '{6}';
                                """.format(
                                self.table, self.s3_bucket, self.s3_key, 
                                credentials.access_key, credentials.secret_key,
                                self.region,
                                self.json)
                            )

        redshift.run(copy_to_redshift)

        self.log.info("Copy command completed")





