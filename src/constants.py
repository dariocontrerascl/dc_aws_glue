from pathlib import Path
from typing import Tuple

# Default ACM (AWS Certificate Manger) region
ACM_REGION = "us-east-1"

# Default CDK account & region to use
DEFAULT_CDK_ACCOUNT = "013472794367"
DEFAULT_CDK_REGION = "us-east-2"

# Paths to stacks, assets, source & root
IDAP_PATH = Path(__file__).parent
STACKS_PATH = IDAP_PATH / "stacks"
ASSETS_PATH = STACKS_PATH / "assets"
SRC_PATH = IDAP_PATH.parent
ROOT_PATH = SRC_PATH.parent

# Default maintenance window for ElastiCache / RDS update
# Saturday 01am - 03am PST (America/Los_Angeles)
MAINTENANCE_WINDOW = "sat:09:00-sat:11:00"

#: Default domain name to use
IFXND_DOMAIN_NAME = "ifxnd.rocks"

#: Default certificate ID for *.ifxnd.rocks domains. Certificate manually
#: issued in `ACM_REGION`
IFXND_CERTIFICATE_ID = "17863e48-a392-438a-81ef-e5dab295649e"
