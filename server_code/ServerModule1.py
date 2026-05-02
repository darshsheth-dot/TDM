import anvil.email
import anvil.server
from anvil.tables import app_tables
from datetime import datetime

# ---------------------------------------------------
# FEEDBACK SYSTEM
# ---------------------------------------------------

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


# ---------------------------------------------------
# MINDMAP STORAGE (NO AI)
# ---------------------------------------------------

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


# ---------------------------------------------------
# MORNING MIND GAMES PROGRESS SYSTEM (NO LOGIN)
# ---------------------------------------------------

@anvil.server.callable
def increment_progress():
  """Increase progress count when a game is completed."""
  row = app_tables.progress.get()
  row['count'] += 1
  return row['count']


@anvil.server.callable
def reset_progress():
  """Reset progress back to 0 (optional)."""
  row = app_tables.progress.get()
  row['count'] = 0
  return 0


@anvil.server.callable
def get_progress():
  """Return the current progress count."""
  row = app_tables.progress.get()
  return row['count']
