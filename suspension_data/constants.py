from typing import Final

from utils import runtime_path_resolver

RUNTIME_DIR: Final[str] = runtime_path_resolver.RUNTIME_DIR

DATA_SOURCE_LOCATION: Final[str] = f"{RUNTIME_DIR}/data_source"
ASSETS_LOCATION: Final[str] = f"{RUNTIME_DIR}/assets"

NUM_CLASSES: Final[int] = 1
INPUT_DIM: Final[int] = 5
TRAIN_EPOCHS: Final[int] = 50
