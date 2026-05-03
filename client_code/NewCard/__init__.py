from ._anvil_designer import NewCardTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from anvil.tables import app_tables


class NewCard(NewCardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    open_form("Dashboard")

  @handle("flashcard_button", "click")
  def flashcard_button_click(self, **event_args):
    open_form("Flashcards")

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    open_form("Routine")

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    open_form("Blok")

  @handle("feedback_button", "click")
  def feedback_button_click(self, **event_args):
    open_form("Fback_Form")
