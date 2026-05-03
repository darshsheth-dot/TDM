from ._anvil_designer import EnglishTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class English(EnglishTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # -----------------------------
    # WORDS + DEFINITIONS + EXAMPLES
    # -----------------------------
    self.words = [
      {
        "word": "Anthropomorphism (noun)",
        "definition": "The attribution of human characteristics or behaviour to a god, animal, or object.",
        "example": "Disney movies often use anthropomorphism by giving animals human emotions."
      },
      {
        "word": "Interdependence (noun)",
        "definition": "A relationship where two or more organisms, systems, or factors rely on each other to function or survive.",
        "example": "Plants and animals show interdependence because they rely on each other for oxygen and carbon dioxide."
      }
    ]

    self.current_index = 0
    self._load_word()

  # -----------------------------
  # SIDEBAR NAVIGATION
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
  # LOAD WORD + DEFINITION
  # -----------------------------
  def _load_word(self):
    w = self.words[self.current_index]
    self.word_label.text = w["word"]
    self.definition_label.text = w["definition"]

    # Clear previous results
    self.result_label.text = ""
    self.sentence_box.text = ""

    # Show/hide navigation buttons
    self.back_button.visible = self.current_index > 0
    self.next_button.visible = self.current_index < len(self.words) - 1

  # -----------------------------
  # SUBMIT BUTTON — SHOW EXAMPLE SENTENCE
  # -----------------------------
  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    w = self.words[self.current_index]
    example_sentence = w["example"]

    self.result_label.text = (
      "Nice try, here is an example sentence:\n\n" + example_sentence
    )
    self.result_label.foreground = "blue"

  # -----------------------------
  # NEXT BUTTON
  # -----------------------------
  @handle("next_button", "click")
  def next_button_click(self, **event_args):
    if self.current_index < len(self.words) - 1:
      self.current_index += 1
      self._load_word()

  # -----------------------------
  # BACK BUTTON
  # -----------------------------
  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    if self.current_index > 0:
      self.current_index -= 1
      self._load_word()
