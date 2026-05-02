from ._anvil_designer import RoutineTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Routine(RoutineTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_tasks()

  def load_tasks(self):
    self.routine_grid.items = list(app_tables.tasks.search())

  @handle("add_row_button", "click")
  def add_row_button_click(self, **event_args):
    app_tables.tasks.add_row(
      task_name="",
      subject="",
      due_date="",
      priority="",
      username=""
    )
    self.load_tasks()

  @handle("remove_row_button", "click")
  def remove_row_button_click(self, **event_args):
    rows = list(app_tables.tasks.search())
    if rows:
      rows[-1].delete()
      self.load_tasks()
    else:
      alert("No tasks to remove!")

  @handle("generate_button", "click")
  def generate_button_click(self, **event_args):
    tasks = list(app_tables.tasks.search())
    if not tasks:
      alert("No tasks to generate a routine from!")
      return
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda t: (
      priority_order.get(t["priority"], 4),
      t["due_date"] or ""
    ))
    open_form('GeneratedRoutine', tasks=sorted_tasks)

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

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass