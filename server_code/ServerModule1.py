import anvil.email
from datetime import datetime
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  # Send yourself an email each time feedback is submitted
  anvil.email.send(to="ishaan.sarin@education.nsw.gov.au",
    subject=f"Feedback from {name}",
    text=f"""
  A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)