from ._anvil_designer import ScienceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Science(ScienceTemplate):
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

  # -----------------------------
  # TRUE / FALSE QUESTION LOGIC
  # -----------------------------

  @handle("true_button", "click")
  def true_button_click(self, **event_args):
    # Correct answer is FALSE
    self.result_label.text = "Wrong answer, nice try"
    self.result_label.foreground = "red"

  @handle("false_button", "click")
  def false_button_click(self, **event_args):
    # Correct answer is FALSE
    self.result_label.text = "Correct answer, keep it up!!!!"
    self.result_label.foreground = "green"
