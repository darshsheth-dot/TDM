from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("dashboard_button", "click")
  def dashboard_button_click(self, **event_args):
    open_form('Dashboard')

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    open_form('MindMap')

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    open_form('Routine')

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    open_form('Blok')

  @handle("Math", "click")
  def Math_click(self, **event_args):
    open_form('Math')

  @handle("Science", "click")
  def Science_click(self, **event_args):
    open_form('Science')

  @handle("English", "click")
  def English_click(self, **event_args):
    open_form('English')

  @handle("feedback_form_button", "click")
  def feedback_form_button_click(self, **event_args):
    open_form('Fback_Form')

  @handle("", "refreshing_data_bindings")
  def form_refreshing_data_bindings(self, **event_args):
    pass