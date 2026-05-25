# Enterprise-AI-Resume-Generator-Agent-built-using-Fast-API-Streamlit-UI at http://localhost:8501 (port 8501)

The Business Problem Problem: 
Job seekers — especially career changers and senior professionals — spend hours tailoring resumes to each job description. 
Most resumes fail before a human sees them — ATS filters reject them on keywords alone. Job seekers have no reliable, automated way to analyze their profile, optimize keywords, write professional content, and review quality in one step. 
This system solves that with a secure, production-grade multi-agent API Most resumes fail ATS (Applicant Tracking System) filters before a human ever sees them. 
No current free/open tool does end-to-end intelligent resume generation + ATS scoring + quality review in one automated pipeline. 

Our solution: An API-first, multi-agent AI system that:

Takes a raw user profile (skills, experience, education, projects) Analyzes the candidate's level and domain Scores and optimizes for ATS keyword matching. 
Writes a polished, professional resume Reviews it for grammar, consistency, and professionalism Returns a structured JSON response — ready to render into a PDF or UI

Architecture (All Required Stages) Here is the flow your main.py must follow, stage by stage:

APP INITIALIZATION → Create FastAPI app, set title/version
SECURITY CONFIG → API Key auth via HTTP header (X-API-Key)
REQUEST MODEL → Pydantic model for incoming user profile
LOGGING FUNCTION → log_step() writes to logs.txt + console
PROFILE ANALYZER AGENT → OpenAI call → candidate level, domain, years
ATS OPTIMIZATION AGENT → OpenAI call → missing keywords, ATS score
RESUME WRITER AGENT → OpenAI call → summary, bullets, skills, projects
REVIEWER AGENT → OpenAI call → grammar, consistency, final score
ORCHESTRATOR → Calls all 4 agents in sequence, builds result
ROOT ENDPOINT (GET /) → Health check
MAIN API ENDPOINT → POST /generate-resume → runs orchestrator
Architecture workflow Diagram


Execution Steps in order to run Streamlit UI

Create and enter project folder cd project-name

Install dependencies pip install -r requirements.txt

Create .env file (paste your OpenAI API Key here) OpenAI_API_KEY=YOUR-API-KEY-HERE API_APP_KEY=NAME-OF-API-APP-GIVEN

We need to run test_api.py before running streamlit to ensure the Key is passed correctly along with the status code 200 and the Expected Output printed as shsown below

<img width="1596" height="786" alt="image" src="https://github.com/user-attachments/assets/6b360592-2aa9-4f4e-ab0e-b7bb19000a1d" />

<img width="1457" height="772" alt="image" src="https://github.com/user-attachments/assets/a8ed95ec-f37d-41c8-a7f7-618f1d4f78ef" />

Nown Run the server streamlit run app_name.py

Executes and runs local host at port 8501 localhost:8501

<img width="1920" height="832" alt="image" src="https://github.com/user-attachments/assets/f71b9200-774a-440f-b957-80e846622fc3" />

<img width="1843" height="746" alt="image" src="https://github.com/user-attachments/assets/15942894-21fc-484f-aa59-65104be2201e" />

<img width="1916" height="812" alt="image" src="https://github.com/user-attachments/assets/3985a9ce-7c93-4904-97bf-8a2d7023caa5" />

When we hit Generate Resume
<img width="1837" height="678" alt="image" src="https://github.com/user-attachments/assets/de5eea57-3a87-4f94-813e-8286cbe1a1e8" />

<img width="1908" height="752" alt="image" src="https://github.com/user-attachments/assets/047653e7-911b-4b3f-a859-9c0ac3472237" />

<img width="1505" height="794" alt="image" src="https://github.com/user-attachments/assets/2ed07525-6c82-40b5-929b-e6146c448a3f" />

<img width="1451" height="653" alt="image" src="https://github.com/user-attachments/assets/59a29b87-2a52-4d4b-ac2b-30f83e79daca" />

<img width="1451" height="792" alt="image" src="https://github.com/user-attachments/assets/b1a0b087-b4f6-4126-9345-a5c521129fe1" />

<img width="1477" height="818" alt="image" src="https://github.com/user-attachments/assets/5958848d-eb2b-46e5-b6b6-eaab1baec70b" />

Raw JSON Response:

<img width="1425" height="771" alt="image" src="https://github.com/user-attachments/assets/1a6dbce3-837d-484d-a744-529b6025af7d" />

<img width="1499" height="691" alt="image" src="https://github.com/user-attachments/assets/5ec9e0cd-f337-4711-9302-1d5fd6cd7655" />


Enhancemennts to be made:

To Improve Quality Review with consistency score, professionalism score and status of approved with appropriate final recommendation

<img width="1515" height="736" alt="image" src="https://github.com/user-attachments/assets/8527a0db-4417-45ff-8557-c93b6e36c361" />
