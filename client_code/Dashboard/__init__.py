from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self._load_progress()

  # ---------------------------------------------------
  # LOAD MORNING MIND GAMES PROGRESS (PROGRESS BAR)
  # ---------------------------------------------------
  def _load_progress(self):
    count = anvil.server.call('get_progress')

    total = 30  # total bar segments

    if count == 0:
      filled = 0
      color = "black"
    elif count == 1:
      filled = total // 3
      color = "red"
    elif count == 2:
      filled = (total * 2) // 3
      color = "orange"
    else:
      filled = total
      color = "green"

    empty = total - filled

    bar = "█" * filled + "░" * empty

    self.progress_bar.text = bar
    self.progress_bar.foreground = color

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

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    open_form('Blok')

  @handle("feedback_button", "click")
  def feedback_button_click(self, **event_args):
    open_form('Fback_Form')

  @handle("flashcard_button", "click")
  def flashcard_button_click(self, **event_args):
    open_form('Flashcards')

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
