import anvil.email
from datetime import datetime
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
import json

# -------------------------------
# FEEDBACK SYSTEM (your original)
# -------------------------------

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name,
    email=email,
    feedback=feedback,
    created=datetime.now()
  )

  anvil.email.send(
    to="ishaan.sarin@education.nsw.gov.au",
    subject=f"Feedback from {name}",
    text=f"""
A new person has filled out the feedback form!

Name: {name}
Email address: {email}

Feedback:
{feedback}
"""
  )

# -------------------------------
# AI MINDMAP GENERATOR (GROQ)
# -------------------------------

GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"   # <-- Replace this

@anvil.server.callable
def generate_mindmap(subject, subtopic, branch, grade):

  prompt = f"""
Create a full educational mindmap for:

Subject: {subject}
Sub-topic: {subtopic}
Branch: {branch}
Grade/Year: {grade}

The mindmap must include:

- Main topic
- 3 major subtopics
- 3 branches under each subtopic
- Definitions
- Examples
- Prerequisites
- Overview
- Key diagrams (describe them)
- Real-world applications
- A clean structured layout

Format it clearly using headings and bullet points.
"""

  url = "https://api.groq.com/openai/v1/chat/completions"

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROQ_API_KEY}"
  }

  data = {
    "model": "llama3-70b-8192",
    "messages": [
      {"role": "user", "content": prompt}
    ]
  }

  response = requests.post(url, headers=headers, data=json.dumps(data))
  result = response.json()

  if "choices" not in result:
    return f"⚠️ Groq Error:\n\n{json.dumps(result, indent=2)}"

  return result["choices"][0]["message"]["content"]
