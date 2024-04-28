from pathlib import Path, PurePath
import os
from datetime import datetime, timedelta
from enum import Enum
import pytz

# ====================== DIRETÓRIOS LOCAIS e DATAS ======================
FULL_DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIRECTORY = os.path.join(ROOT, "data")
DATE_NOW = datetime.now().strftime(FULL_DATE_FORMAT)
