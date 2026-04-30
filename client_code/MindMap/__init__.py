from ._anvil_designer import MindMapTemplate
from anvil import *
import anvil.server

class MindMap(MindMapTemplate):

  def __init__(self, **properties):
    self.init_components(**properties)

    # This will store all nodes as dictionaries
    self.nodes = []

    # Load saved mindmap titles into dropdown
    self._refresh_mindmap_list()

  # -------------------------------
  # NAVIGATION BUTTONS
  # -------------------------------
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

  # -------------------------------
  # LOAD LIST OF SAVED MINDMAPS
  # -------------------------------
  def _refresh_mindmap_list(self):
    titles = anvil.server.call('list_mindmaps')
    self.mindmap_dropdown.items = titles

  # -------------------------------
  # NEW MINDMAP
  # -------------------------------
  @handle("new_button", "click")
  def new_button_click(self, **event_args):
    self.title_box.text = ""
    self.nodes = []
    self.nodes_panel.clear()

  # -------------------------------
  # ADD NODE
  # -------------------------------
  def add_node_button_click(self, **event_args):
    node = {
      "id": f"node_{len(self.nodes)+1}",
      "title": "New Node",
      "notes": "",
    }

    self.nodes.append(node)
    self._render_nodes()

  # -------------------------------
  # RENDER ALL NODES
  # -------------------------------
  def _render_nodes(self):
    self.nodes_panel.clear()

    for node in self.nodes:
      card = ColumnPanel(role="card", spacing="small")

      title_box = TextBox(text=node["title"], placeholder="Node title")
      notes_area = TextArea(text=node["notes"], placeholder="Notes...")

      delete_btn = Button(text="Delete Node", role="danger")

      # Update title
      def update_title(tb, n=node, **e):
        n["title"] = tb.text

      # Update notes
      def update_notes(ta, n=node, **e):
        n["notes"] = ta.text

      # Delete node
      def delete_node(btn, n=node, **e):
        self.nodes.remove(n)
        self._render_nodes()

      title_box.set_event_handler("change", update_title)
      notes_area.set_event_handler("change", update_notes)
      delete_btn.set_event_handler("click", delete_node)

      card.add_component(Label(text=node["id"], bold=True))
      card.add_component(title_box)
      card.add_component(notes_area)
      card.add_component(delete_btn)

      self.nodes_panel.add_component(card)

  # -------------------------------
  # SAVE MINDMAP
  # -------------------------------
  def save_button_click(self, **event_args):
    title = self.title_box.text

    if not title:
      alert("Please enter a title before saving.")
      return

    anvil.server.call('save_mindmap', title, self.nodes)
    alert("Mindmap saved successfully.")
    self._refresh_mindmap_list()

  # -------------------------------
  # LOAD MINDMAP
  # -------------------------------
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
    self.nodes = nodes
    self._render_nodes()
