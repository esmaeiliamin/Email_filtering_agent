import logging
from typing import Optional

from openai import AsyncOpenAI

from src.config import Settings
from src.contracts.conversation import MessageRole
from src.contracts.report import QueryResponse
from src.memory.short_term_memory import ShortTermMemory
from src.rag.report_retriever import ReportRetriever