import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

class EmailCategory(str, Enum):
    URGENT = "urgent"
    IMPORTANT = "important"
    REQUIRES_FOLLOW_UP = "requires_follow_up"
    IGNORE = "ignore"