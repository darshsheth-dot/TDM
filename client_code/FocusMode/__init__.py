from ._anvil_designer import FocusModeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FocusMode(FocusModeTemplate):
  def __init__(self, minutes=25, blocked_apps=[], **properties):
    self.init_components(**properties)
    self.total_seconds = minutes * 60
    self.remaining = self.total_seconds
    self.running = True
    self.apps_label.text = "Blocked Apps:\n" + "\n".join(["• " + app for app in blocked_apps])
    self.update_display()
    self.timer_1.interval = 1

  def update_display(self):
    mins = self.remaining // 60
    secs = self.remaining % 60
    self.timer_label.text = f"{mins:02d}:{secs:02d}"

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    if self.running and self.remaining > 0:
      self.remaining -= 1
      self.update_display()
    elif self.remaining == 0:
      self.timer_1.interval = 0
      alert("Focus session complete! Great work! 🎉")
      open_form('Dashboard')

  @handle("pause_button", "click")
  def pause_button_click(self, **event_args):
    if self.running:
      self.running = False
      self.pause_button.text = "Resume"
    else:
      self.running = True
      self.pause_button.text = "Pause"

  @handle("end_button", "click")
  def end_button_click(self, **event_args):
    self.timer_1.interval = 0
    open_form('Blok')

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