from ._anvil_designer import MindMapTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MindMap(MindMapTemplate):
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

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Routine')

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Blok')
