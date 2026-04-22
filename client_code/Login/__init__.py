from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
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

    if not password:
      alert("Please fill in all fields.")
      return

    open_form('Dashboard')

  @handle("sign_in_page_button", "click")
  def sign_in_page_button_click(self, **event_args):
    open_form('Signin')

  @handle("", "hide")
  def form_hide(self, **event_args):
    """This method is called when the form is removed from the page"""
    pass
