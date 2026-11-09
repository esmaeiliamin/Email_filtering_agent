import uuid
from typing import Dict, List, Optional

from openai import AsyncOpenAI

from src.contracts.conversation import (
    ConversationMessage,
    ConversationSession,
    FollowUpState,
    MessageRole,
)
