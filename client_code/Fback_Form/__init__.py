from ._anvil_designer import Fback_FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Fback_Form(Fback_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("Feedback submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()
    def clear_inputs(self):
    # Clear our three text boxes
      self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""