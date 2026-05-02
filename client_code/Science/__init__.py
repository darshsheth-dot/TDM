from ._anvil_designer import ScienceTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Science(ScienceTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # -----------------------------
    # YOUR 3 QUESTIONS
    # -----------------------------
    self.questions = [
      {"text": "Methyl Orange is a known indicator to measure potential hydrogen in chemicals.", "answer": False},
      {"text": "All cells contain a cell wall to give them shape and support.", "answer": False},
      {"text": "Sound can't travel through a vacuum, such as outer space.", "answer": True}
    ]

    self.current_index = 0
    self.correct_count = 0   # Track correct answers
    self._load_question()

  # -----------------------------
  # NAVIGATION BUTTONS
  # -----------------------------
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

  # -----------------------------
  # LOAD QUESTION
  # -----------------------------
  def _load_question(self):
    q = self.questions[self.current_index]
    self.question_label.text = q["text"]
    self.result_label.text = ""

    # Show/hide navigation buttons
    self.back_button.visible = self.current_index > 0
    self.next_button.visible = self.current_index < len(self.questions) - 1

  # -----------------------------
  # TRUE BUTTON
  # -----------------------------
  @handle("true_button", "click")
  def true_button_click(self, **event_args):
    correct = self.questions[self.current_index]["answer"]
    if correct is True:
      self.result_label.text = "Correct answer, keep it up!!!!"
      self.result_label.foreground = "green"
      self.correct_count += 1
    else:
      self.result_label.text = "Wrong answer, nice try"
      self.result_label.foreground = "red"

  # -----------------------------
  # FALSE BUTTON
  # -----------------------------
  @handle("false_button", "click")
  def false_button_click(self, **event_args):
    correct = self.questions[self.current_index]["answer"]
    if correct is False:
      self.result_label.text = "Correct answer, keep it up!!!!"
      self.result_label.foreground = "green"
      self.correct_count += 1
    else:
      self.result_label.text = "Wrong answer, nice try"
      self.result_label.foreground = "red"

  # -----------------------------
  # NEXT BUTTON
  # -----------------------------
  @handle("next_button", "click")
  def next_button_click(self, **event_args):
    # If moving to the last question → after answering it, send score
    if self.current_index == len(self.questions) - 1:
      return

    self.current_index += 1
    self._load_question()

  # -----------------------------
  # BACK BUTTON
  # -----------------------------
  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    if self.current_index > 0:
      self.current_index -= 1
      self._load_question()

  # -----------------------------
  # FINISH BUTTON (OPTIONAL)
  # -----------------------------
  @handle("finish_button", "click")
  def finish_button_click(self, **event_args):
    total_questions = len(self.questions)

    # Send score to server
    new_percentage = anvil.server.call(
      "update_science_score",
      self.correct_count,
      total_questions
    )

    # Show updated percentage
    self.science_percentage_label.text = f"Science Accuracy: {new_percentage}%"
progress = anvil.server.call('increment_progress')