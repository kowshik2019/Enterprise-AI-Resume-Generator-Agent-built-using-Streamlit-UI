

# ============================================================
# STREAMLIT UI — Enterprise AI Resume Generator
# ============================================================

import streamlit as st
import requests
import json

# ============================================================
# CONFIG
# ============================================================

API_URL = "http://localhost:8000/generate-resume"
API_KEY = "enterprise-resume-secret-key"

# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Enterprise AI Resume Generator",
    page_icon="📄",
    layout="wide"
)

st.title("Enterprise AI Resume Generator")
st.markdown("Multi-Agent AI System — Powered by OpenAI GPT-4o-mini")
st.divider()

# ============================================================
# INPUT FORM
# ============================================================

st.subheader("👤 Personal Information")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name", placeholder="Kowshik")
    email = st.text_input("Email", placeholder="kowshik4@gmail.com")

with col2:
    target_role = st.text_input("Target Role", placeholder="Senior Data Engineer")

st.divider()

# ============================================================
# SKILLS
# ============================================================

st.subheader("🛠️ Skills")
skills_input = st.text_area(
    "Enter skills separated by commas",
    placeholder="Python, PySpark, SQL, Snowflake, Airflow, AWS"
)

st.divider()

# ============================================================
# EXPERIENCE
# ============================================================

st.subheader("💼 Work Experience")
exp_title = st.text_input("Job Title", placeholder="Sr. Data Scientist")
exp_company = st.text_input("Company", placeholder="Chase")
exp_years = st.number_input("Years in this Role", min_value=0.0, max_value=40.0, step=0.5)
exp_description = st.text_area(
    "Role Description",
    placeholder="Describe your responsibilities and achievements"
)

st.divider()

# ============================================================
# EDUCATION
# ============================================================

st.subheader("🎓 Education")
edu_degree = st.text_input("Degree", placeholder="Master of Science in Computer Science")
edu_institution = st.text_input("Institution", placeholder="University of Texas at Arlington")
edu_year = st.number_input("Graduation Year", min_value=1990, max_value=2030, step=1, value=2023)

st.divider()

# ============================================================
# PROJECTS
# ============================================================

st.subheader("🚀 Projects")
projects_input = st.text_area(
    "Enter each project on a new line",
    placeholder="Multi Agent AI Resume Generator\nFraud Detection Pipeline\nCustomer Support Workflow"
)

st.divider()

# ============================================================
# CERTIFICATIONS
# ============================================================

st.subheader("🏆 Certifications")
certs_input = st.text_area(
    "Enter each certification on a new line",
    placeholder="AWS Certified Developer Associate\nAWS Certified Solutions Architect"
)

st.divider()

# ============================================================
# GENERATE BUTTON
# ============================================================

if st.button("🚀 Generate Resume", type="primary", use_container_width=True):

    # Validate required fields
    if not name or not email or not target_role:
        st.error("Please fill in Name, Email and Target Role before generating.")
    elif not skills_input:
        st.error("Please enter at least one skill.")
    elif not exp_title or not exp_company or not exp_description:
        st.error("Please fill in all Experience fields.")
    elif not edu_degree or not edu_institution:
        st.error("Please fill in all Education fields.")
    else:
        # Build request payload
        payload = {
            "name": name,
            "email": email,
            "target_role": target_role,
            "skills": [s.strip() for s in skills_input.split(",") if s.strip()],
            "experience": [
                {
                    "title": exp_title,
                    "company": exp_company,
                    "years": exp_years,
                    "description": exp_description
                }
            ],
            "education": [
                {
                    "degree": edu_degree,
                    "institution": edu_institution,
                    "year": int(edu_year)
                }
            ],
            "projects": [p.strip() for p in projects_input.split("\n") if p.strip()],
            "certifications": [c.strip() for c in certs_input.split("\n") if c.strip()]
        }

        st.sidebar.write(f"Using API Key: {API_KEY}")

        # Call FastAPI backend
        with st.spinner("🤖 Running AI agents... This may take 20-30 seconds..."):
            try:
                response = requests.post(
                    API_URL,
                    json=payload,
                    
                    headers={
                        "X-API-Key": "enterprise-resume-secret-key",
                        "Content-Type": "application/json"
                    },
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Resume Generated Successfully!")
                    st.divider()

                    # ----------------------------------------
                    # PROFILE ANALYSIS
                    # ----------------------------------------
                    st.subheader("🔍 Profile Analysis")
                    pa = data.get("profile_analysis", {})
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Candidate Level", pa.get("candidate_level", "N/A"))
                    with col2:
                        st.metric("Primary Domain", pa.get("primary_domain", "N/A"))
                    with col3:
                        st.metric("Years Experience", pa.get("years_experience", "N/A"))

                    st.markdown("**Key Strengths:**")
                    strengths = pa.get("key_strengths", [])
                    for strength in strengths:
                        st.markdown(f"- {strength}")

                    st.divider()

                    # ----------------------------------------
                    # ATS OPTIMIZATION
                    # ----------------------------------------
                    st.subheader("🎯 ATS Optimization")
                    ats = data.get("ats_optimization", {})
                    col1, col2 = st.columns(2)
                    with col1:
                        ats_score = ats.get("ats_score", 0)
                        st.metric("ATS Score", f"{ats_score}/100")
                        if ats_score >= 80:
                            st.success("Strong ATS alignment")
                        elif ats_score >= 60:
                            st.warning("Moderate ATS alignment")
                        else:
                            st.error("Weak ATS alignment — add more keywords")

                    with col2:
                        st.markdown("**Missing Keywords:**")
                        for kw in ats.get("missing_keywords", []):
                            st.markdown(f"- {kw}")

                    st.markdown("**Role Alignment Tips:**")
                    for tip in ats.get("role_alignment_tips", []):
                        st.info(tip)

                    st.divider()

                    # ----------------------------------------
                    # RESUME CONTENT
                    # ----------------------------------------
                    st.subheader("📄 Generated Resume Content")
                    rc = data.get("resume_content", {})

                    st.markdown("**Professional Summary:**")
                    st.write(rc.get("professional_summary", ""))

                    st.markdown("**Experience Bullets:**")
                    for bullet in rc.get("experience_bullets", []):
                        st.markdown(f"- {bullet}")

                    st.markdown("**Skills Section:**")
                    skills_section = rc.get("skills_section", {})
                    for category, skills_list in skills_section.items():
                        st.markdown(f"**{category}:** {', '.join(skills_list)}")

                    st.markdown("**Project Descriptions:**")
                    for proj in rc.get("project_descriptions", []):
                        st.markdown(f"- {proj}")

                    st.divider()

                    # ----------------------------------------
                    # REVIEW
                    # ----------------------------------------
                    st.subheader("✅ Quality Review")
                    rv = data.get("review", {})
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Consistency Score", f"{rv.get('consistency_score', 0)}/100")
                    with col2:
                        st.metric("Professionalism Score", f"{rv.get('professionalism_score', 0)}/100")
                    with col3:
                        approved = rv.get("approved", False)
                        st.metric("Approved", "✅ Yes" if approved else "❌ No")

                    st.markdown("**Final Recommendation:**")
                    st.success(rv.get("final_recommendation", ""))

                    if rv.get("grammar_issues"):
                        st.markdown("**Grammar Issues:**")
                        for issue in rv.get("grammar_issues", []):
                            st.warning(issue)

                    st.divider()

                    # ----------------------------------------
                    # RAW JSON OUTPUT
                    # ----------------------------------------
                    with st.expander("🔧 View Raw JSON Response"):
                        st.json(data)

                else:
                    st.error(f"API Error {response.status_code}: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to FastAPI backend. Make sure uvicorn is running on port 8000.")
            except requests.exceptions.Timeout:
                st.error("Request timed out. The AI agents are taking too long. Try again.")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")