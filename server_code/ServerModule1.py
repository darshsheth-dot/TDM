import anvil.users
import anvil.email
import anvil.server
from anvil.tables import app_tables
from datetime import datetime

# FEEDBACK SYSTEM

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name,
    email=email,
    feedback=feedback,
    created=datetime.now()
  )

  anvil.email.send(
    to="darsh.sheth@education.nsw.gov.au",
    subject=f"Feedback from {name}",
    text=f"""
A new person has filled out the feedback form!

Name: {name}
Email address: {email}

Feedback:
{feedback}
"""
  )

# MINDMAP STORAGE (NO AI)

@anvil.server.callable
def save_mindmap(title, nodes):
  row = app_tables.mindmaps.get(title=title)
  if row:
    row['nodes'] = nodes
    row['updated'] = datetime.now()
  else:
    app_tables.mindmaps.add_row(
      title=title,
      nodes=nodes,
      created=datetime.now(),
      updated=datetime.now()
    )
  return "saved"

@anvil.server.callable
def load_mindmap(title):
  row = app_tables.mindmaps.get(title=title)
  if row:
    return row['nodes']
  return None

@anvil.server.callable
def list_mindmaps():
  return [r['title'] for r in app_tables.mindmaps.search()]
