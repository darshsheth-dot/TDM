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
# MATHS PERCENTAGE SYSTEM
# ---------------------------------------------------

@anvil.server.callable
def update_math_score(correct, total):
  """Update the user's maths accuracy percentage."""
  user = anvil.users.get_user()
  if not user:
    return 0

  # Initialise if missing
  if user['math_correct'] is None:
    user['math_correct'] = 0
  if user['math_total'] is None:
    user['math_total'] = 0

  # Update totals
  user['math_correct'] += correct
  user['math_total'] += total

  # Avoid division by zero
  if user['math_total'] == 0:
    return 0

  return round((user['math_correct'] / user['math_total']) * 100)


# ---------------------------------------------------
# SCIENCE PERCENTAGE SYSTEM
# ---------------------------------------------------

@anvil.server.callable
def update_science_score(correct, total):
  """Update the user's science accuracy percentage."""
  user = anvil.users.get_user()
  if not user:
    return 0

  # Initialise if missing
  if user['science_correct'] is None:
    user['science_correct'] = 0
  if user['science_total'] is None:
    user['science_total'] = 0

  # Update totals
  user['science_correct'] += correct
  user['science_total'] += total

  # Avoid division by zero
  if user['science_total'] == 0:
    return 0

  return round((user['science_correct'] / user['science_total']) * 100)
