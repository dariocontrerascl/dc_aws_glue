from typing import Any, cast, Tuple
from ..settings import Settings
from aws_cdk import aws_ec2, aws_glue, aws_iam, aws_s3_assets, core, aws_s3_deployment, aws_s3
import os
import yaml

ID_STACK = "idap-glue-reporting"
IAM_ROLE_GLUE = "AWSGlueServiceRoleDefault"


class GlueStack(core.Stack):
    settings: Settings

    @staticmethod
    def get_all_job(directory):
        jobs = []
        for filename in os.listdir(directory):
            curr_folder = os.path.join(directory, filename)
            if os.path.isdir(curr_folder):
                for config in os.listdir(curr_folder):
                    if config.__contains__(".yml"):
                        get_job = "%s/%s" % (curr_folder, config)
                        with open(get_job) as file:
                            documents = yaml.full_load(file)
                        s3_script = documents['command']['script_location'].split('/')[-1]
                        job_script_asset = "%s/%s" % (curr_folder, s3_script)
                        # s3_script_dest = documents['s3_script_destination']
                        # del documents['s3_script_destination']
                        print(documents['command'])
                        documents['command'] = aws_glue.CfnJob.JobCommandProperty(**documents['command'])
                        jobs.append((documents, job_script_asset, None))

        return jobs

    def __init__(self, scope: core.Construct, *, settings: Settings, **kwargs: Any, ) -> None:
        super().__init__(scope, ID_STACK, **kwargs)
        base_job_directory = os.path.dirname(__file__) + '/job/'
        jobs = self.get_all_job(base_job_directory)

        glue_jobs_bucket = aws_s3.Bucket(self, 'my-code-dacl', bucket_name="my-code-dacl")

        if len(jobs) > 0:
            project_asset = aws_s3_assets.Asset(self, "ProjectZippedAsset", path=base_job_directory)

            aws_s3_deployment.BucketDeployment(
                self,
                'DeployGlueJobsBucket',
                sources=[aws_s3_deployment.Source.asset(base_job_directory)] + [aws_s3_deployment.Source.asset(project_asset.asset_path)],
                destination_bucket=glue_jobs_bucket,
                destination_key_prefix="glue_jobs",
                prune=False,
            )




        for current in jobs:
            current_glue_job = current[0]
            aws_glue.CfnJob(
                scope=self,
                **current_glue_job
            )
