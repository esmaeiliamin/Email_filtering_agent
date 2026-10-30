import json
import logging
from typing import Optional

from openai import AsyncOpenAI

from src.config import Settings
from backend.contracts.email import (
    ClassificationResult,
    EmailCategory,
    IncomingEmail,
    UserPreferences,
)