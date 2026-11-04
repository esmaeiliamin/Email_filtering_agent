import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"