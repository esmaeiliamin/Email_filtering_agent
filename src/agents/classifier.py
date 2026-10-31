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

def _build_prompt(email: IncomingEmail, prefs: Optional[UserPreferences]) -> str:
    prefs_block = ""
    if prefs:
        if prefs.urgent_keywords:
            prefs_block += f"\nUser flags these words as urgent: {', '.join(prefs.urgent_keywords)}"
        if prefs.important_senders:
            prefs_block += f"\nAlways treat mail from these senders as important: {', '.join(prefs.important_senders)}"
        if prefs.ignore_keywords:
            prefs_block += f"\nIgnore emails containing: {', '.join(prefs.ignore_keywords)}"
        if prefs.custom_rules:
            prefs_block += f"\nAdditional rules: {prefs.custom_rules}"

    return f"""Classify the following email:{prefs_block}

From: {email.sender_name or email.sender} <{email.sender}>
Subject: {email.subject}
---
{email.body[:3000]}

Respond with JSON:
{{
  "category": "urgent|important|requires_follow_up|ignore",
  "reasoning": "one-sentence explanation",
  "confidence": 0.0-1.0
}}"""

