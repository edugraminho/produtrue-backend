from pathlib import Path, PurePath
import os
from datetime import datetime, timedelta
from enum import Enum


# ====================== DIRETÓRIOS LOCAIS e DATAS ======================
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIRECTORY = os.path.join(ROOT, "data")
NOW = datetime.now().strftime("%d/%m/%y %H:%M:%S")
CURRENT_DAY = datetime.now().strftime("%d/%m")
