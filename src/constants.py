from pathlib import Path
from typing import Any, Dict, Literal, TypeVar, Tuple

# Default ACM (AWS Certificate Manger) region
ACM_REGION = "us-east-1"

# Default CDK account & region to use
DEFAULT_CDK_ACCOUNT = "124614996455"
DEFAULT_CDK_REGION = "us-east-2"

# Paths to stacks, assets, source & root
IDAP_PATH = Path(__file__).parent
STACKS_PATH = IDAP_PATH / "stacks"
ASSETS_PATH = STACKS_PATH / "assets"
SRC_PATH = IDAP_PATH.parent
ROOT_PATH = SRC_PATH.parent

# Default stages

StageName = Literal["dev", "prod"]
STAGES: Tuple[StageName, ...] = ("dev", "prod")


print(STAGES)