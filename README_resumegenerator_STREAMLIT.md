# Enterprise AI Resume Generator Agent System

> A production-grade, multi-agent AI application that automatically analyzes candidate profiles,
> optimizes for ATS, generates professional resume content, and reviews quality —
> all accessible through a clean Streamlit web interface.

---

## Table of Contents

- [Business Problem](#business-problem)
- [Solution Overview](#solution-overview)
- [System Architecture](#system-architecture)
- [Agent Pipeline](#agent-pipeline)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Using the Streamlit UI](#using-the-streamlit-ui)
- [API Reference](#api-reference)
- [Security](#security)
- [Logging and Observability](#logging-and-observability)
- [Troubleshooting](#troubleshooting)
- [Key Design Decisions](#key-design-decisions)

---

## Business Problem

Over **75% of resumes are rejected by Applicant Tracking Systems (ATS)** before a human
ever reviews them — purely because they lack the right keywords, formatting, or role alignment.

Job seekers — especially career changers and senior professionals — spend hours manually
tailoring resumes for each application with no reliable feedback on whether the resume
will actually pass ATS filters.

**No existing open tool provides:**
- End-to-end intelligent resume generation
- Real-time ATS keyword scoring and gap analysis
- Professional quality review with actionable feedback
- All in one secure, API-driven pipeline

---

## Solution Overview

This system solves that by orchestrating **four specialized AI agents** in sequence:

```
User fills Streamlit form
         ↓
FastAPI receives and validates the request
         ↓
Security layer validates API key
         ↓
Orchestrator runs 4 agents in sequence:
  Agent 1 → Analyzes candidate profile
  Agent 2 → Scores and optimizes for ATS
  Agent 3 → Writes professional resume content
  Agent 4 → Reviews quality and approves
         ↓
Streamlit displays structured results
         ↓
Logs written to logs.txt + console
```

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  STREAMLIT FRONTEND                      │
│              http://localhost:8501                       │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Personal Info │ Skills │ Experience │ Education  │   │
│  │  Projects │ Certifications │ Generate Button      │   │
│  └──────────────────────┬───────────────────────────┘   │
└─────────────────────────┼───────────────────────────────┘
                          │ HTTP POST with X-API-Key header
                          ▼
┌─────────────────────────────────────────────────────────┐
│               FASTAPI BACKEND (Uvicorn)                  │
│                http://localhost:8000                     │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │            SECURITY LAYER                          │ │
│  │         X-API-Key Header Validation                │ │
│  └───────────────────┬────────────────────────────────┘ │
│                      │                                   │
│  ┌───────────────────▼────────────────────────────────┐ │
│  │               ORCHESTRATOR                         │ │
│  │         Sequences all four agents                  │ │
│  └──┬──────────────┬──────────────┬──────────────┬───┘ │
│     │              │              │              │       │
│  ┌──▼───┐      ┌───▼──┐      ┌───▼──┐      ┌───▼──┐   │
│  │Agent │      │Agent │      │Agent │      │Agent │   │
│  │  1   │      │  2   │      │  3   │      │  4   │   │
│  │Prof. │─────▶│ ATS  │─────▶│Resume│─────▶│Revie-│   │
│  │Anlzr │      │Optmz │      │Writr │      │ wer  │   │
│  └──────┘      └──────┘      └──────┘      └──────┘   │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │              OpenAI GPT-4o-mini                    │ │
│  │         Shared call_openai() function              │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
               ┌──────────────────┐
               │     logs.txt     │
               │  Console Output  │
               └──────────────────┘
```

---

## Agent Pipeline

### Agent 1 — Profile Analyzer
**Input:** Raw candidate profile (skills, experience, education, projects, certifications)

**Output:**
```json
{
  "candidate_level": "Senior",
  "primary_domain": "Data Engineering",
  "years_experience": 9,
  "key_strengths": ["Pipeline architecture", "Cloud platforms", "Real-time streaming"],
  "career_summary_hint": "Seasoned Data Engineer with expertise in cloud-native pipelines"
}
```

---

### Agent 2 — ATS Optimization Agent
**Input:** Candidate profile + Agent 1 output

**Output:**
```json
{
  "ats_score": 82,
  "missing_keywords": ["Delta Lake", "Databricks", "CI/CD"],
  "recommended_keywords": ["PySpark", "dbt", "Kafka", "Snowflake"],
  "formatting_suggestions": ["Use standard section headers", "Avoid tables"],
  "role_alignment_tips": ["Emphasize cloud experience", "Quantify pipeline scale"]
}
```

---

### Agent 3 — Resume Writer Agent
**Input:** Candidate profile + Agent 1 output + Agent 2 output

**Output:**
```json
{
  "professional_summary": "Results-driven Senior Data Engineer with 9 years of experience...",
  "experience_bullets": ["Architected ETL pipelines...", "Designed fraud detection system..."],
  "skills_section": {
    "Programming": ["Python", "PySpark", "SQL"],
    "Cloud Platforms": ["AWS", "Snowflake", "Databricks"]
  },
  "project_descriptions": ["Built real-time fraud detection pipeline..."]
}
```

---

### Agent 4 — Reviewer Agent
**Input:** Resume content from Agent 3 + original candidate profile

**Output:**
```json
{
  "grammar_issues": [],
  "consistency_score": 94,
  "professionalism_score": 91,
  "formatting_feedback": ["Add LinkedIn URL", "Ensure consistent bullet style"],
  "final_recommendation": "Resume is enterprise-ready and ATS-optimized.",
  "approved": true
}
```

---

## Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend UI | Streamlit 1.35.0 | Web interface for form input and result display |
| API Framework | FastAPI 0.111.0 | RESTful API with automatic Swagger docs |
| ASGI Server | Uvicorn 0.29.0 | Production-grade async server |
| LLM Backend | OpenAI GPT-4o-mini | Powers all four AI agents |
| Data Validation | Pydantic 2.7.1 | Request body validation and type safety |
| Authentication | FastAPI APIKeyHeader | X-API-Key header security |
| HTTP Client | Requests 2.31.0 | Streamlit to FastAPI communication |
| Environment Config | python-dotenv 1.0.1 | Secure API key management |
| Logging | Python logging + file | Console + logs.txt observability |

---

## Project Structure

```
capstone_resume_agent/
├── main_Resumegenerator.py     # FastAPI backend — all 11 stages
├── streamlit_app.py            # Streamlit frontend UI
├── test_api.py                 # API testing script
├── requirements.txt            # All Python dependencies
├── .env                        # API keys (create this — never commit)
├── .gitignore                  # Excludes .env and logs from git
├── logs.txt                    # Auto-generated at runtime
└── README.md                   # This file
```

---

## Prerequisites

- Python 3.10 or higher
- pip package manager
- An active OpenAI API account with credits
- Two terminal windows (one for FastAPI, one for Streamlit)

---

## Installation

### Step 1 — Create project folder

```bash
mkdir capstone_resume_agent
cd capstone_resume_agent
```

### Step 2 — Create virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Mac/Linux
source venv/bin/activate

# Activate — Windows Command Prompt
venv\Scripts\activate

# Activate — Windows PowerShell
.\venv\Scripts\Activate.ps1
```

### Step 3 — Install all dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Verify installation

```bash
python -c "import fastapi, uvicorn, openai, streamlit, pydantic, dotenv; print('All packages installed successfully')"
```

---

## Configuration

### Create your `.env` file

Create a file named `.env` in the project root using your terminal:

**Windows Command Prompt:**
```cmd
(
echo OPENAI_API_KEY=sk-proj-your-actual-key-here
echo OPENAI_MODEL=gpt-4o-mini
echo APP_API_KEY=enterprise-resume-secret-key
) > .env
```

**Mac/Linux:**
```bash
cat > .env << EOF
OPENAI_API_KEY=sk-proj-your-actual-key-here
OPENAI_MODEL=gpt-4o-mini
APP_API_KEY=enterprise-resume-secret-key
EOF
```

### Verify `.env` contents

```bash
# Windows
type .env

# Mac/Linux
cat .env
```

Expected output — no quotes, no spaces around `=`:
```
OPENAI_API_KEY=sk-proj-yourrealkeyhere
OPENAI_MODEL=gpt-4o-mini
APP_API_KEY=enterprise-resume-secret-key
```

### Create `.gitignore`

```bash
echo .env > .gitignore
echo logs.txt >> .gitignore
echo __pycache__/ >> .gitignore
echo venv/ >> .gitignore
```

> **CRITICAL:** Never commit `.env` to GitHub. Your OpenAI key will be exposed and compromised.

---

## Running the Application

You need **two terminals open simultaneously** — one for FastAPI, one for Streamlit.

### Terminal 1 — Start FastAPI Backend FIRST

```bash
cd capstone_resume_agent
uvicorn main_Resumegenerator:app --port 8000
```

Wait until you see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Terminal 2 — Start Streamlit Frontend SECOND

```bash
cd capstone_resume_agent
streamlit run streamlit_app.py
```

Streamlit automatically opens your browser at:
```
http://localhost:8501
```

### Important Rule
Always start uvicorn **before** streamlit. Streamlit sends requests to FastAPI — if FastAPI is not running, every Generate Resume click will show a connection error.

---

## Using the Streamlit UI

### Step 1 — Fill Personal Information
- Full Name
- Email address
- Target Role (e.g. Senior Data Engineer, Data Scientist, ML Engineer)

### Step 2 — Enter Skills
Type skills separated by commas:
```
Python, PySpark, SQL, Snowflake, Airflow, Kafka, AWS, dbt
```

### Step 3 — Fill Work Experience
- Job Title
- Company Name
- Years in this role
- Role description (be specific — mention technologies and achievements)

### Step 4 — Fill Education
- Degree name
- Institution name
- Graduation year (integer only — e.g. 2023)

### Step 5 — Enter Projects
One project per line:
```
Real-time fraud detection pipeline using Kafka and Spark
Medical Q&A RAG system using BioBERT and ChromaDB
```

### Step 6 — Enter Certifications
One certification per line:
```
AWS Certified Developer Associate
AWS Certified Solutions Architect
```

### Step 7 — Click Generate Resume
The spinner appears while all 4 agents run. This takes approximately **20–40 seconds**.

### Step 8 — View Results
Results display in four sections:
- **Profile Analysis** — candidate level, domain, strengths
- **ATS Optimization** — score, missing keywords, tips
- **Resume Content** — summary, bullets, skills, projects
- **Quality Review** — scores, approval, recommendation

---

## API Reference

### Health Check

```
GET http://localhost:8000/
```

No authentication required. Returns server status.

**Response:**
```json
{
  "status": "running",
  "service": "Enterprise AI Resume Generator",
  "version": "1.0.0",
  "agents": ["ProfileAnalyzer", "ATSOptimizer", "ResumeWriter", "Reviewer"],
  "llm_backend": "OpenAI GPT-4o-mini"
}
```

---

### Generate Resume

```
POST http://localhost:8000/generate-resume
```

**Required Headers:**
```
X-API-Key: enterprise-resume-secret-key
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "Kowshik",
  "email": "kowshik@gmail.com",
  "target_role": "Senior Data Engineer",
  "skills": ["Python", "PySpark", "SQL", "Snowflake", "Airflow"],
  "experience": [
    {
      "title": "Sr. Data Engineer",
      "company": "Chase",
      "years": 6,
      "description": "Built ETL pipelines processing 10M records daily"
    }
  ],
  "education": [
    {
      "degree": "Master of Science in Computer Science",
      "institution": "University of Texas at Arlington",
      "year": 2023
    }
  ],
  "projects": [
    "Real-time fraud detection pipeline using Kafka and Spark"
  ],
  "certifications": [
    "AWS Certified Developer Associate"
  ]
}
```

**Field Rules:**
| Model | Field | Type | Notes |
|---|---|---|---|
| UserProfile | name | string | Required |
| UserProfile | email | string | Required |
| UserProfile | target_role | string | Required |
| UserProfile | skills | list of strings | At least one required |
| Experience | title | string | Job title |
| Experience | company | string | Company name |
| Experience | years | float | e.g. 4.0 or 6 |
| Experience | description | string | Role description |
| Education | degree | string | Full degree name |
| Education | institution | string | School name |
| Education | year | integer | Graduation year — NOT graduation_year |

**Response Codes:**
| Code | Meaning |
|---|---|
| 200 | Success — full resume generated |
| 403 | Invalid or missing X-API-Key header |
| 422 | Validation error — check field names and types |
| 500 | Internal error — check uvicorn logs |

---

### Interactive Swagger Docs

```
http://localhost:8000/docs
```

FastAPI auto-generates interactive documentation. Click Authorize, enter your API key, and test directly from the browser.

---

## Security

- Every `/generate-resume` request requires the `X-API-Key` header
- Incorrect or missing key returns HTTP 403 Forbidden immediately
- No agent runs, no OpenAI call is made on failed auth
- API key loaded from `.env` via `python-dotenv`
- Never hardcode keys in source files

---

## Logging and Observability

Every agent execution writes a timestamped log entry to both console and `logs.txt`.

**Log format:**
```
[TIMESTAMP] [AGENT] [STATUS] detail
```

**Example log for a successful run:**
```
[2024-01-15 10:30:00] [API] [REQUEST_RECEIVED] User=Kowshik | Role=Senior Data Engineer
[2024-01-15 10:30:00] [Orchestrator] [STARTED] Pipeline initiated for Kowshik
[2024-01-15 10:30:01] [ProfileAnalyzer] [STARTED] Analyzing profile for Kowshik
[2024-01-15 10:30:03] [ProfileAnalyzer] [COMPLETED] Level=Senior | Domain=Data Engineering
[2024-01-15 10:30:03] [ATSOptimizer] [STARTED] Running ATS analysis for role: Senior Data Engineer
[2024-01-15 10:30:05] [ATSOptimizer] [COMPLETED] ATS Score=82 | Missing Keywords=3
[2024-01-15 10:30:05] [ResumeWriter] [STARTED] Generating professional resume content
[2024-01-15 10:30:08] [ResumeWriter] [COMPLETED] Summary generated | Bullets=6 | Skill Categories=4
[2024-01-15 10:30:08] [Reviewer] [STARTED] Reviewing resume for quality and professionalism
[2024-01-15 10:30:11] [Reviewer] [COMPLETED] Approved=True | Professionalism=91 | Consistency=94
[2024-01-15 10:30:11] [Orchestrator] [COMPLETED] All 4 agents finished — assembling final response
[2024-01-15 10:30:11] [API] [SUCCESS] Resume successfully generated for Kowshik
```

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `403 Invalid API Key` | Key mismatch between Streamlit and FastAPI | Ensure `API_KEY` in `streamlit_app.py` matches `APP_API_KEY` in `.env` |
| `422 graduation_year missing` | Wrong field name in request | Use `year` not `graduation_year` in Education |
| `422 years missing` | Wrong field name in request | Use `years` not `year` in Experience |
| `500 sequence item expected str` | Agent returned list of dicts | Use `safe_join()` helper for list fields |
| `500 JSON parsing failed` | GPT returned markdown fences | `parse_json_response()` strips fences automatically |
| `Cannot connect to FastAPI` | uvicorn not running | Start uvicorn first on port 8000 |
| `proxies TypeError` | httpx version conflict | Run `pip install httpx==0.27.0` |
| `Security not defined` | Missing import | Add `Security` to FastAPI imports in Stage 1 |
| `tuple error on API key` | Trailing comma on API_KEY | Remove comma: `API_KEY = "key"` not `API_KEY = "key",` |
| OpenAI `401 Invalid key` | Wrong or expired key | Generate new key at platform.openai.com/api-keys |

---

## Key Design Decisions

**Why OpenAI and not Claude?**
The project uses `call_openai()` exclusively because the API key is an OpenAI key.
`call_claude()` is not applicable here. The shared helper calls `gpt-4o-mini` which
balances quality and cost for resume generation tasks.

**Why two separate servers?**
FastAPI handles business logic, security, and agent orchestration.
Streamlit handles only the UI. Separating them means the API can be tested independently
via Swagger or curl — and a different frontend (React, mobile app) could use the same API
without any changes to the backend.

**Why four separate agents?**
Each agent has a single, well-defined responsibility (separation of concerns).
This makes the system testable, debuggable, and extensible — adding a new agent
(e.g. Cover Letter Writer) requires no changes to existing agents.

**Why Pydantic models?**
Pydantic validates every incoming request before any agent runs. Bad data is rejected
at the door with a clear 422 error — preventing garbage from reaching OpenAI
and wasting API credits.

**Why `load_dotenv(override=True)`?**
`override=True` forces Python to re-read `.env` every time, ignoring any
system-level environment variables that might contain stale values.
This solves the "different key showing in console" problem on Windows.
