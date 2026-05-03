from ._anvil_designer import NodeCardTemplate
from anvil import *
import anvil.users

class NodeCard(NodeCardTemplate):
  def __init__(self, node_id=None, title="", notes="", **properties):
    self.init_components(**properties)

    # Store the node's unique ID
    self.node_id = node_id

    # Populate fields
    self.title_box.text = title
    self.notes_box.text = notes

    # Return node data as a clean dictionary for saving
  def get_data(self):
    return {
      "id": self.node_id,
      "title": self.title_box.text,
      "notes": self.notes_box.text
    }

    # Delete this node from the panel
  def delete_button_click(self, **event_args):
    self.parent.remove_component(self)

  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Dashboard")

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("MindMap")

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Routine")

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Blok")
