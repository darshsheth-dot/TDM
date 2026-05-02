from ._anvil_designer import BlokTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables

class Blok(BlokTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # -----------------------------
    # TIMER OPTIONS
    # -----------------------------
    self.timer_dropdown.items = ["25 minutes", "30 minutes", "45 minutes", "60 minutes"]
    self.timer_dropdown.selected_value = "25 minutes"

    # -----------------------------
    # MUSIC OPTIONS (YOUR NAMES)
    # -----------------------------
    self.music_dropdown.items = ["Focus", "Chill", "Peaceful"]
    self.music_dropdown.selected_value = "Focus"

  # -----------------------------
  # SIDEBAR NAVIGATION
  # -----------------------------
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

  # -----------------------------
  # PLAY BUTTON → GO TO FOCUS MODE
  # -----------------------------
  @handle("play_button", "click")
  def play_button_click(self, **event_args):
    selected_time = self.timer_dropdown.selected_value
    minutes = int(selected_time.split(" ")[0])

    # Collect selected blocked apps
    blocked_apps = []
    if self.tiktok_check.checked:
      blocked_apps.append("TikTok")
    if self.snapchat_check.checked:
      blocked_apps.append("Snapchat")
    if self.instagram_check.checked:
      blocked_apps.append("Instagram")
    if self.youtube_check.checked:
      blocked_apps.append("YouTube")
    if self.google_check.checked:
      blocked_apps.append("Google")

    if not blocked_apps:
      alert("Please select at least one app to block!")
      return

    # Pass timer, blocked apps, and music choice to FocusMode
    open_form(
      'FocusMode',
      minutes=minutes,
      blocked_apps=blocked_apps,
      music_choice=self.music_dropdown.selected_value
    )
