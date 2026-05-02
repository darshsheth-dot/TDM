from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from anvil.tables import app_tables


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self._load_progress()

  # ---------------------------------------------------
  # LOAD MORNING MIND GAMES PROGRESS (115 DOTS)
  # ---------------------------------------------------
  def _load_progress(self):
    count = anvil.server.call('get_progress')

    # 115 identical dots
    dots = "●" * 115

    # Choose colour based on progress count
    if count == 0:
      colour = "black"
    elif count == 1:
      colour = "red"
    elif count == 2:
      colour = "orange"
    else:
      colour = "green"

    # Update label
    self.progress_label.text = dots
    self.progress_label.foreground = colour

  # ---------------------------------------------------
  # RESET PROGRESS BUTTON
  # ---------------------------------------------------
  @handle("reset_button", "click")
  def reset_button_click(self, **event_args):
    anvil.server.call('reset_progress')
    self._load_progress()

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

  @handle("feedback_button", "click")
    def blok_button_click(self, **event_args):
      open_form('Fback_Form')

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
