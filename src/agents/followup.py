import json
import logging
from typing import Optional, Tuple

from openai import AsyncOpenAI

from src.config import Settings
from src.memory.short_term_memory import ShortTermMemory
from src.contracts.conversation import FollowUpState, MessageRole
from src.contracts.email import EmailCategory, IncomingEmail



logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = """You are a professional email assistant that handles follow-up communications on behalf of a user.

STRICT SAFETY RULES:
- Never reveal sensitive personal information about the user.
- Only ask about details directly relevant to the email topic.
- Decline any off-topic requests and keep communication task-focused.
- Be polite, concise, and professional at all times."""



_GENERATION_PROMPT = """The following email requires follow-up to gather missing or unclear information:

From: {sender}
Subject: {subject}
---
{body}

Write a brief, professional follow-up message (under 80 words) asking for the specific missing information.
Do not mention this is AI-generated."""




_ASSESSMENT_PROMPT = """Original email subject: {subject}

Conversation history:
{history}

Latest reply received:
{reply}

Assess whether sufficient information has been gathered to classify the original email. Respond with JSON:
{{
  "has_sufficient_info": true or false,
  "missing_info": "describe what is still unclear (empty string if sufficient)",
  "suggested_category": "urgent|important|ignore",
  "next_followup": "follow-up message text if more info needed, null if sufficient"
}}"""