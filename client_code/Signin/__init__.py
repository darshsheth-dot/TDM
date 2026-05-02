from ._anvil_designer import SigninTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Signin(SigninTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.error_label.visible = False

  @handle("sign_in_button", "click")
  def sign_in_button_click(self, **event_args):
    email = self.email_enter.text.strip()
    password = self.password_enter.text.strip()
    username = self.username_enter.text.strip()

    if not email.endswith("@gmail.com") and not email.endswith("@education.nsw.gov.au"):
      self.error_label.visible = True
      return

    self.error_label.visible = False

    if not username or not password:
      alert("Please fill in all fields.")
      return

    try:
      anvil.users.signup_with_email(email, password)
      open_form('Dashboard')
    except Exception as e:
      alert(f"Sign up error: {e}")

  @handle("login_page_button", "click")
  def login_page_button_click(self, **event_args):
    open_form('Login')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass