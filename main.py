import logging
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import AsyncOpenAI
from pydantic import BaseModel

from backend.agents.classifier import EmailClassifier
from backend.agents.followup import FollowUpService
from backend.agents.qa_agent import QAAgent
from backend.agents.summarizer import EmailSummarizer
from backend.config import settings
from backend.contracts.conversation import FollowUpReplyRequest
from backend.contracts.email import EmailCategory, ProcessEmailRequest, ProcessEmailResponse
from backend.contracts.report import DailyReport, QueryRequest, QueryResponse
from backend.memory.short_term_memory import ShortTermMemory
from backend.rag import create_rag
from backend.services.push_notification import PushNotificationService
from backend.storage.azure_report_storage import AzureReportStorage
from backend.storage.local_report_storage import LocalReportStorage
from backend.storage.report_storage import ReportStorage