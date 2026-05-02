from ._anvil_designer import RoutineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Routine(RoutineTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_tasks()

  def load_tasks(self):
    rows = list(app_tables.tasks.search())
    if not rows:
      self.tasks_display.text = "No tasks yet. Click 'Add Task' to begin!"
      return
    output = ""
    for i, row in enumerate(rows, 1):
      output += f"{i}. {row['task_name']} | {row['subject']} | Due: {row['due_date']} | {row['priority']}\n"
    self.tasks_display.text = output

  @handle("add_row_button", "click")
  def add_row_button_click(self, **event_args):
    task = ask("Enter task name:")
    if task is None: return
    subject = ask("Enter subject:")
    if subject is None: return
    due_date = ask("Enter due date (DD/MM):")
    if due_date is None: return
    priority = ask("Enter priority (High / Medium / Low):")
    if priority is None: return
    app_tables.tasks.add_row(
      task_name=task,
      subject=subject,
      due_date=due_date,
      priority=priority,
      username=""
    )
    self.load_tasks()

  @handle("remove_row_button", "click")
  def remove_row_button_click(self, **event_args):
    rows = list(app_tables.tasks.search())
    if not rows:
      alert("No tasks to remove!")
      return
    task_names = [r["task_name"] for r in rows]
    to_remove = ask("Enter task name to remove:\n" + "\n".join(task_names))
    if to_remove is None: return
    for row in rows:
      if row["task_name"].lower() == to_remove.lower():
        row.delete()
        self.load_tasks()
        return
    alert("Task not found!")

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