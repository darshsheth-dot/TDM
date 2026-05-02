from ._anvil_designer import MathTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Math(MathTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  # ---------------------------------------------------
  # SIDEBAR NAVIGATION
  # ---------------------------------------------------

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

  # ---------------------------------------------------
  # SUBMIT BUTTON — CHECK ALL 5 ANSWERS + SEND SCORE
  # ---------------------------------------------------

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):

    # Correct answers for each question
    correct_answers = {
      "text_box_1": "4x",     # Q1: 7x - 3x
      "text_box_2": "30",     # Q2: 1/2 × 12 × 5
      "text_box_3": "10",     # Q3: hypotenuse of 6 and 8
      "text_box_4": "0.4",    # Q4: 4/10
      "text_box_5": "3200"    # Q5: 3.2 km → 3200m
    }

    # Labels for feedback
    labels = {
      "text_box_1": self.label_q1,
      "text_box_2": self.label_q2,
      "text_box_3": self.label_q3,
      "text_box_4": self.label_q4,
      "text_box_5": self.label_q5
    }

    # Count correct answers
    correct_count = 0
    total_questions = len(correct_answers)

    # Check each answer
    for box_name, correct in correct_answers.items():
      user_answer = getattr(self, box_name).text.strip().lower()
      label = labels[box_name]

      if user_answer == correct:
        label.text = "Correct answer, keep it up!!!!"
        label.foreground = "green"
        correct_count += 1
      else:
        label.text = "Wrong answer, nice try"
        label.foreground = "red"

    # ---------------------------------------------------
    # SEND SCORE TO SERVER FOR PERCENTAGE TRACKING
    # ---------------------------------------------------
    new_percentage = anvil.server.call(
      "update_math_score",
      correct_count,
      total_questions
    )

    # Optional: show the updated percentage on the page
    self.math_percentage_label.text = f"Math Accuracy: {new_percentage}%"
progress = anvil.server.call('increment_progress')