from ._anvil_designer import MindMapTemplate
from anvil import *
import anvil.server
import uuid
from ..NodeCard import NodeCard

class MindMap(MindMapTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refresh_dropdown()

    # ---------------------------
    # NEW MINDMAP
    # ---------------------------
  @handle("new_button", "click")
  def new_button_click(self, **event_args):
    self.title_box.text = ""
    self.nodes_panel.clear()

    # ---------------------------
    # ADD NODE
    # ---------------------------
  @handle("add_node_button", "click")
  def add_node_button_click(self, **event_args):
    node_id = str(uuid.uuid4())
    card = NodeCard(node_id=node_id, title="", notes="")
    self.nodes_panel.add_component(card)

    # ---------------------------
    # SAVE MINDMAP
    # ---------------------------
  def save_button_click(self, **event_args):
    title = self.title_box.text.strip()
    if not title:
      alert("Please enter a title before saving.")
      return

    nodes = [c.get_data() for c in self.nodes_panel.get_components()]

    anvil.server.call('save_mindmap', title, nodes)
    self.refresh_dropdown()
    alert("Mindmap saved successfully.")

    # ---------------------------
    # LOAD MINDMAP
    # ---------------------------
  @handle("load_button", "click")
  def load_button_click(self, **event_args):
    title = self.mindmap_dropdown.selected_value
    if not title:
      alert("Please select a mindmap to load.")
      return

    nodes = anvil.server.call('load_mindmap', title)
    if nodes is None:
      alert("Mindmap not found.")
      return

    self.title_box.text = title
    self.nodes_panel.clear()

    for n in nodes:
      card = NodeCard(
        node_id=n["id"],
        title=n["title"],
        notes=n["notes"]
      )
      self.nodes_panel.add_component(card)

    # ---------------------------
    # REFRESH DROPDOWN
    # ---------------------------
  def refresh_dropdown(self):
    titles = anvil.server.call('list_mindmaps')
    self.mindmap_dropdown.items = titles
