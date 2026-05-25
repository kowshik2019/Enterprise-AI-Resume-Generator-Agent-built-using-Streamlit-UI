import requests

API_KEY = "enterprise-resume-secret-key"

print(f"Sending key: {repr(API_KEY)}")
print(f"Key length: {len(API_KEY)}")
print(f"URL: http://127.0.0.1:8000/generate-resume")
print("---")

response = requests.post(
    "http://127.0.0.1:8000/generate-resume",
    headers={
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "name": "Kowshik",
        "email": "kowshik4@gmail.com",
        "target_role": "Data Scientist",
        "skills": ["Python", "SQL", "ML"],
        "experience": [
            {
                "title": "Sr. Data Scientist",
                "company": "Chase",
                "years": 6,
                "description": "Built ML models and AI pipelines"
            }
        ],
        "education": [
            {
                "degree": "Master of Science in Computer Science",
                "institution": "University of Texas at Arlington",
                "year": 2023
            }
        ],
        "projects": ["AI Resume Generator"],
        "certifications": ["AWS Certified Developer Associate"]
    }
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")