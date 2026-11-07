import json
import logging
from typing import Optional, Tuple

from openai import AsyncOpenAI

from src.config import Settings
from src.memory.short_term_memory import ShortTermMemory
from src.contracts.conversation import FollowUpState, MessageRole
from src.contracts.email import EmailCategory, IncomingEmail