from ._anvil_designer import EnglishTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class English(EnglishTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    open_form("Dashboard")

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    open_form("MindMap")

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    open_form("Routine")

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    open_form("Blok")

  # ---------------------------------------------------
  # SUBMIT BUTTON — GIVE EXAMPLE SENTENCE
  # ---------------------------------------------------

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):

    # Example sentence for the word of the day
    example_sentence = (
      "The author’s clever use of anthropomorphism allowed the grumpy old grandfather clock to lecture the children about wasting their time."
    )

    # Display feedback + example
    self.result_label.text = (
      "Nice sentence, here is an example sentence:\n\n" + example_sentence
    )
    self.result_label.foreground = "blue"
