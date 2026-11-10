import uuid
from typing import Dict, List, Optional

from openai import AsyncOpenAI

from src.contracts.conversation import (
    ConversationMessage,
    ConversationSession,
    FollowUpState,
    MessageRole,
)
_SUMMARIZE_SYSTEM_PROMPT = """\
You are compressing older turns of a conversation into a compact memory block.
Your output will be injected as context for an AI assistant continuing the conversation.

Rules:
- Preserve every fact, decision, question asked, and answer given — nothing important may be lost.
- Keep named entities (people, email senders, subjects, dates, categories) verbatim.
- Note any unresolved questions or pending actions explicitly.
- Write in past tense, third-person neutral ("The user asked...", "The assistant confirmed...").
- Be as concise as possible without omitting anything load-bearing.
- Output plain prose — no bullet lists, no headers.\
"""