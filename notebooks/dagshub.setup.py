import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/write2shivamgithub/credit_risk_pipeline.mlflow")
dagshub.init(repo_owner='write2shivamgithub', repo_name='credit_risk_pipeline', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)