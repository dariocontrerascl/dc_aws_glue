from typing import Any, cast, Tuple
from ..settings import Settings
from aws_cdk import aws_ec2, aws_glue, aws_iam, aws_s3_assets, core
import os
import yaml


IDAP = "idap"
ENVIRONMENT = "glue"
IAM_ROLE_GLUE = "AWSGlueServiceRoleDefault"


class GlueStack(core.Stack):
    settings: Settings

    def __get_all_job(self):
        directory = os.path.dirname(__file__)
        jobs = []
        for filename in os.listdir(directory):
            curr_folder = os.path.join(directory, filename)
            if curr_folder.__contains__("job_"):
                for config in os.listdir(curr_folder):
                    if config.__contains__(".yml"):
                        get_job = "%s/%s" % (curr_folder, config)
                        with open(get_job) as file:
                            documents = yaml.full_load(file)
                        jobs.append(documents)
        return jobs

    def __init__(self, scope: core.Construct, *, settings: Settings, **kwargs: Any, ) -> None:
        super().__init__(scope, IDAP, **kwargs)

        jobs = self.__get_all_job()
        for current_glue_job in jobs:
            print(1, current_glue_job)
            job = aws_glue.CfnJob(
                scope=self,
                **current_glue_job
                # id=current_glue_job['command']["name"],
                # command=current_glue_job['command'],
                # role= current_glue_job['role'],
                # default_arguments=current_glue_job['default_arguments'],
                # allocated_capacity=current_glue_job['allocated_capacity'],
                # description=current_glue_job['description'],
                # glue_version=current_glue_job['glue_version'],
                # max_capacity=current_glue_job['max_capacity'],
                # max_retries=current_glue_job['max_retries'],
                # number_of_workers=current_glue_job['number_of_workers'],
                # timeout=current_glue_job['timeout'],
                # worker_type=current_glue_job['worker_type']
            )
