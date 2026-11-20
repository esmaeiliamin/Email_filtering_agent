import logging
from typing import Optional

from openai import AsyncOpenAI

from src.config import Settings
from src.contracts.conversation import MessageRole
from src.contracts.report import QueryResponse
from src.memory.short_term_memory import ShortTermMemory
from src.rag.report_retriever import ReportRetriever



logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = """You are a helpful email assistant that answers user questions about their email activity.

Rules:
- Answer based solely on the email data provided with each question.
- If the information is not in the provided data, say so clearly — do not guess.
- Be concise and specific; cite the report date when referencing a specific email.
- Maintain context across multi-turn conversations."""