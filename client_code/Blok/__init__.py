from ._anvil_designer import BlokTemplate
from anvil import *
import anvil.server
import time

class Blok(BlokTemplate):

  def __init__(self, **properties):
    self.init_components(**properties)

    # TIMER STATE
    self.total_seconds = 25 * 60
    self.remaining_seconds = self.total_seconds
    self.timer_running = False

    # STRICT MODE FLAG
    self.strict_mode = False

    # Update labels on load
    self._update_timer_labels()

  # ---------------------------------------------------
  # NAVIGATION BLOCKER
  # ---------------------------------------------------
  def _block_navigation_if_needed(self):
    if self.strict_mode:
      alert("Your study session is still running. Stay focused!")
      return True
    return False

  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    if self._block_navigation_if_needed():
      return
    open_form('Dashboard')

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    if self._block_navigation_if_needed():
      return
    open_form('MindMap')

  @handle("routine_button", "click")
  def routine_button_click(self, **event_args):
    if self._block_navigation_if_needed():
      return
    open_form('Routine')

  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    # Already on Blok, but still block if strict mode
    if self._block_navigation_if_needed():
      return
    open_form('Blok')

  # ---------------------------------------------------
  # TIMER DISPLAY UPDATE
  # ---------------------------------------------------
  def _update_timer_labels(self):
    mins = self.remaining_seconds // 60
    secs = self.remaining_seconds % 60
    self.timer_label.text = f"{mins:02d}:{secs:02d}"

    elapsed = self.total_seconds - self.remaining_seconds
    elapsed_m = elapsed // 60
    elapsed_s = elapsed % 60
    total_m = self.total_seconds // 60

    self.progress_label.text = f"{elapsed_m:02d}:{elapsed_s:02d} / {total_m:02d}:00"

  # ---------------------------------------------------
  # START / PAUSE BUTTON
  # ---------------------------------------------------
  def start_pause_button_click(self, **event_args):
    if not self.timer_running:
      # STARTING TIMER
      self.timer_running = True
      self.strict_mode = True
      self.start_pause_button.text = "Pause"
      self._start_timer_loop()
    else:
      # PAUSING TIMER
      self.timer_running = False
      self.start_pause_button.text = "Start"

  # ---------------------------------------------------
  # TIMER LOOP
  # ---------------------------------------------------
  def _start_timer_loop(self):
    while self.timer_running and self.remaining_seconds > 0:
      time.sleep(1)
      self.remaining_seconds -= 1
      self._update_timer_labels()
      self.refresh_data_bindings()

    # TIMER FINISHED
    if self.remaining_seconds == 0:
      self.timer_running = False
      self.strict_mode = False
      self.start_pause_button.text = "Start"
      alert("Session complete!")

  # ---------------------------------------------------
  # RESET BUTTON
  # ---------------------------------------------------
  def reset_button_click(self, **event_args):
    if self.strict_mode:
      if not confirm("Are you sure you want to reset? Your progress will be lost."):
        return

    self.timer_running = False
    self.strict_mode = False
    self.start_pause_button.text = "Start"

    # Reset to chosen duration
    minutes = int(self.duration_box.text or 25)
    self.total_seconds = minutes * 60
    self.remaining_seconds = self.total_seconds

    self._update_timer_labels()
