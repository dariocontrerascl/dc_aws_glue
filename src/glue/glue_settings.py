from ..constants import idap_bucket_project_code


class GlueSettings:
    def __init__(self, stage):
        self.base_glue_bucket = idap_bucket_project_code % stage
        self.BASE_GLUE_JOB_PREFIX = "glue_jobs"
        base_glue_job_bucket = "s3://%s/%s" % (self.base_glue_bucket, self.BASE_GLUE_JOB_PREFIX)
        self.glue_zip_file = "IDAP_GLUE.zip"
        base_glue_zip_project = "s3://%s/glue_jobs/%s" % (self.base_glue_bucket, self.glue_zip_file)

        self.global_parameters = {
            "${env}": stage,
            "${glue_jobs_bucket}": base_glue_job_bucket,
            "${glue_jobs_prefix}": self.BASE_GLUE_JOB_PREFIX,
            "${glue_project_zip}": base_glue_zip_project
        }
