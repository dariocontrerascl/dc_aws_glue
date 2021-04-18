from typing import Any, cast, Tuple

from .glue_settings import GlueSettings
from ..constants import StageName
from ..settings import Settings
from aws_cdk import aws_ec2, aws_glue, aws_iam, aws_s3_assets, core, aws_s3_deployment, aws_s3
import os
import yaml

IAM_ROLE_GLUE = "AWSGlueServiceRoleDefault"


class GlueStack(core.Stack):
    settings: Settings

    def get_all_job(self, directory):
        jobs = []
        for filename in os.listdir(directory):
            curr_folder = os.path.join(directory, filename)
            if os.path.isdir(curr_folder):
                for config in os.listdir(curr_folder):
                    if config.__contains__(".yml"):
                        get_job = "%s/%s" % (curr_folder, config)
                        with open(get_job) as file:
                            curr_yaml = file.read()

                            for key, val in self.glue_settings.global_parameters.items():
                                curr_yaml = curr_yaml.replace(key, val)

                            documents = yaml.full_load(curr_yaml)

                        documents['name'] = str(documents['name']).upper()
                        documents['id'] = documents['name']
                        documents['command'] = aws_glue.CfnJob.JobCommandProperty(**documents['command'])
                        jobs.append((documents, None, None))

        return jobs

    def __init__(self, scope: core.Construct, *, settings: Settings, stage: str, **kwargs: Any, ) -> None:
        ID_STACK = "idap-%s-glue-reporting" % stage
        super().__init__(scope, ID_STACK, **kwargs)
        self.settings = settings
        self.stage = stage
        self.glue_settings = GlueSettings(self.stage)
        base_job_directory = os.path.dirname(__file__) + '/job/'

        print(self.glue_settings.global_parameters)
        jobs = self.get_all_job(base_job_directory)

        glue_jobs_bucket = aws_s3.Bucket(self,
                                         self.glue_settings.base_glue_gubket,
                                         bucket_name=self.glue_settings.base_glue_gubket)

        if len(jobs) > 0:
            aws_s3_deployment.BucketDeployment(
                self,
                'DeployGlueJobsBucket%s' % stage,
                sources=[aws_s3_deployment.Source.asset(base_job_directory)],
                destination_bucket=glue_jobs_bucket,
                destination_key_prefix=self.glue_settings.BASE_GLUE_JOB_PREFIX,
                prune=False,
            )

        for current in jobs:
            current_glue_job = current[0]
            aws_glue.CfnJob(
                scope=self,
                **current_glue_job
            )
