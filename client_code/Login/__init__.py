from ._anvil_designer import LoginTemplate
from anvil import *

class Login(LoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
import anvil.users

def login_button_click(self, **event_args):
  email = self.email_enter2.text.strip()
  password = self.password_enter2.text.strip()

  if not email or not password:
    alert("Please fill in all fields.")
    return

  if not email.endswith("@gmail.com") and not email.endswith("@education.nsw.gov.au"):
    self.error_label2.visible = True
    return

  self.error_label2.visible = False

  try:
    user = anvil.users.login_with_email(email, password)
    open_form('Dashboard')
  except:
    alert("Invalid email or password.")