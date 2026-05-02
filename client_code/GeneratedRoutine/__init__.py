from ._anvil_designer import GeneratedRoutineTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


from ._anvil_designer import GeneratedRoutineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GeneratedRoutine(GeneratedRoutineTemplate):
  def __init__(self, tasks=[], **properties):
    self.init_components(**properties)

    if not tasks:
      self.routine_output.text = "No tasks found!"
      return

    output = ""
    for i, task in enumerate(tasks, 1):
      output += f"{i}. {task['task_name']}\n"
      output += f"   📚 Subject: {task['subject']}\n"
      output += f"   📅 Due: {task['due_date']}\n"
      output += f"   ⚡ Priority: {task['priority']}\n"
      output += "\n"

    self.routine_output.text = output

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form('Routine')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass

    
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

@handle("", "hide")
def form_hide(self, **event_args):
    pass
