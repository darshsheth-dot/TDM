from ._anvil_designer import MindMapTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MindMap(MindMapTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

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
  # GENERATE MINMAP USING AI
  # ---------------------------------------------------
  @handle("generate_button", "click")
  def generate_button_click(self, **event_args):

    subject = self.subject_box.text
    subtopic = self.subtopic_box.text
    branch = self.branch_box.text
    grade = self.grade_box.text

    # Call the AI on the server
    mindmap_text = anvil.server.call(
      "generate_mindmap",
      subject,
      subtopic,
      branch,
      grade
    )

    # Display the mindmap
    self.mindmap_output.text = mindmap_text
