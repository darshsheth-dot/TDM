from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Dashboard')

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('MindMap')



  @handle("Math", "click")
  def Math_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Math')

  @handle("Science", "click")
  def Science_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Science')

  @handle("English", "click")
  def English_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('English')

  @handle("feedback_form_button", "click")
  def feedback_form_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Fback_Form')

  @handle("", "refreshing_data_bindings")
  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass  # Write Code Here

