from ._anvil_designer import NewCardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class NewCard(NewCardTemplate):
  def __init__(self, deck_name="", **properties):
    self.init_components(**properties)
    self.deck_name_input.text = deck_name

  @handle("save_button", "click")
  def save_button_click(self, **event_args):
    deck_name = self.deck_name_input.text.strip()
    question = self.question_input.text.strip()
    answer = self.answer_input.text.strip()

    if not deck_name or not question or not answer:
      alert("Please fill in all fields!")
      return

    deck = app_tables.decks.get(deck_name=deck_name)
    if not deck:
      alert("Deck not found! Please create the deck first.")
      return

    app_tables.flashcards.add_row(
      question=question,
      answer=answer,
      deck_name=deck_name
    )
    self.question_input.text = ""
    self.answer_input.text = ""
    alert("Card saved! Add another or go back to decks.")

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form('Flashcards')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass