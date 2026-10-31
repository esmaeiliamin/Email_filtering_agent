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
logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = """You are an intelligent email classification agent.
Analyze each incoming email and assign exactly one category:

- urgent: Requires immediate user attention — deadlines, critical issues, emergencies, or explicit "action required" requests.
- important: Contains valuable information worth logging — status updates, decisions, project progress, or meaningful correspondence.
- requires_follow_up: Contains open questions, missing context, or ambiguous content that must be clarified before it can be acted on.
- ignore: Newsletters, promotions, automated digests, spam, or any low-value content the user need not see.

Be conservative with "urgent" — only use it when truly time-sensitive.
Use "requires_follow_up" only when a clarifying reply is genuinely necessary.

Respond with valid JSON only — no markdown fences."""

