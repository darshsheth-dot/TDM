from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.error_label2.visible = False

  @handle("login_button", "click")
  def login_button_click(self, **event_args):
    email = self.email_enter2.text.strip()
    password = self.password_enter2.text.strip()

    if not email.endswith("@gmail.com") and not email.endswith("@education.nsw.gov.au"):
      self.error_label2.visible = True
      return

    self.error_label2.visible = False

    try:
      anvil.users.login_with_email(email, password)
      open_form('Dashboard')
    except Exception as e:
      alert("Incorrect email or password. Please try again!")

  @handle("sign_in_page_button", "click")
  def sign_in_page_button_click(self, **event_args):
    open_form('Signin')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass