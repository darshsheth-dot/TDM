from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self._load_progress()

  # ---------------------------------------------------
  # LOAD MORNING MIND GAMES PROGRESS
  # ---------------------------------------------------
  def _load_progress(self):
    count = anvil.server.call('get_progress')

    # Change colour based on how many games completed
    if count == 0:
      self.progress_label.text = "●"
      self.progress_label.foreground = "black"

    elif count == 1:
      self.progress_label.text = "●"
      self.progress_label.foreground = "red"

    elif count == 2:
      self.progress_label.text = "●"
      self.progress_label.foreground = "orange"

    elif count >= 3:
      self.progress_label.text = "●"
      self.progress_label.foreground = "green"

  # ---------------------------------------------------
  # SIDEBAR NAVIGATION
  # ---------------------------------------------------
  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
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

  # ---------------------------------------------------
  # MAIN BUTTONS
  # ---------------------------------------------------
  @handle("Math", "click")
  def Math_click(self, **event_args):
    open_form('Math')

  @handle("Science", "click")
  def Science_click(self, **event_args):
    open_form('Science')

  @handle("English", "click")
  def English_click(self, **event_args):
    open_form('English')
