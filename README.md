# mwaa-dynamodb-stock

This is a sample project for using Amazon DynamoDB with Amazon MWAA.

This project is based on the following repository.

- airflow: v2.4.3
- python: v3.10

### make .env file

```
AIRFLOW_ENV=local
S3_AWS_ACCESS_KEY_ID= [your access key id]
S3_AWS_SECRET_ACCESS_KEY= [your secret access key]
```

### dynamodb config (json) -> s3
```
{
    "dynamodb_table_name": "stock",
    "dynamodb_partition_key": "symbol",
    "dynamodb_region": " [your region]]",
    "dynamodb_access_key_id": " [your access key id]",
    "dynamodb_secret_access_key": " [your secret access key]"
}
```

### sync s3 

```
aws s3 sync airflow/ s3://mwaa-environment-public-network-environmentbucket-xxx/ --profile xxx
```

### How to use

1. Create a new MWAA environment
2. Upload the project to the MWAA environment
3. Create a new DAG
4. Create a new connection
5. Create a new variable
6. Run the DAG
7. Check the result


- Link: [https://medium.com/@rhcproc/amazon-managed-workflow-for-apache-airflow-mwaa-storing-current-stock-prices-using-dynamodb-30f2036621ef](https://medium.com/@rhcproc/amazon-managed-workflow-for-apache-airflow-mwaa-storing-current-stock-prices-using-dynamodb-30f2036621ef)