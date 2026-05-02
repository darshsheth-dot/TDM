from ._anvil_designer import FocusModeTemplate
from anvil import *
import anvil.js

class FocusMode(FocusModeTemplate):
  def __init__(self, minutes=25, blocked_apps=[], music_choice="Focus", **properties):
    self.init_components(**properties)

    self.total_seconds = minutes * 60
    self.remaining = self.total_seconds
    self.running = True
    self.music_choice = music_choice

    self.apps_label.text = "Blocked Apps:\n" + "\n".join(["• " + app for app in blocked_apps])

    self.update_display()

    self.timer_1.interval = 1
    self.timer_1.enabled = True

  # ---------------------------------------------------
  # RUNS ONLY AFTER UI IS FULLY LOADED
  # ---------------------------------------------------
  def form_show(self, **event_args):
    # Insert audio element AFTER render
    self.audio_panel.content = """
    <audio id="bgm" loop></audio>
    """

    # Now the element exists → safe to set music
    self._set_music()

    # Start music
    anvil.js.call_js("eval", "document.getElementById('bgm').play()")

  # ---------------------------------------------------
  # SET MUSIC FILE
  # ---------------------------------------------------
  def _set_music(self):
    if self.music_choice == "Focus":
      src = "_/theme/focus.mp3"
    elif self.music_choice == "Chill":
      src = "_/theme/chill.mp3"
    else:
      src = "_/theme/peaceful.mp3"

    js = f"document.getElementById('bgm').src = '{src}'"
    anvil.js.call_js("eval", js)

  # ---------------------------------------------------
  # UPDATE TIMER
  # ---------------------------------------------------
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
      self.running = False
      self.timer_1.enabled = False

      anvil.js.call_js("eval", "var a=document.getElementById('bgm'); a.pause(); a.currentTime=0")

      alert("Focus session complete! Great work! 🎉")
      open_form('Dashboard')

  # ---------------------------------------------------
  # PAUSE / RESUME
  # ---------------------------------------------------
  @handle("pause_button", "click")
  def pause_button_click(self, **event_args):
    if self.running:
      self.running = False
      self.pause_button.text = "Resume"
      anvil.js.call_js("eval", "document.getElementById('bgm').pause()")
    else:
      self.running = True
      self.pause_button.text = "Pause"
      anvil.js.call_js("eval", "document.getElementById('bgm').play()")

  # ---------------------------------------------------
  # END SESSION
  # ---------------------------------------------------
  @handle("end_button", "click")
  def end_button_click(self, **event_args):
    self.running = False
    self.timer_1.enabled = False

    anvil.js.call_js("eval", "var a=document.getElementById('bgm'); a.pause(); a.currentTime=0")

    open_form('Blok')

  # ---------------------------------------------------
  # NAVIGATION
  # ---------------------------------------------------
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
