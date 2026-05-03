from ._anvil_designer import StudyDeckTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StudyDeck(StudyDeckTemplate):
  def __init__(self, deck_name="", **properties):
    self.init_components(**properties)
    self.deck_name = deck_name
    self.deck_title_label.text = f"Deck: {deck_name}"
    self.cards = list(app_tables.flashcards.search(deck_name=deck_name))
    self.current_index = 0
    self.answer_label.visible = False
    self.show_card()

  def show_card(self):
    if not self.cards:
      self.question_label.text = "No cards in this deck yet! Add some."
      self.answer_label.visible = False
      return
    card = self.cards[self.current_index]
    self.question_label.text = card['question']
    self.answer_label.text = card['answer']
    self.answer_label.visible = False

  @handle("reveal_button", "click")
  def reveal_button_click(self, **event_args):
    self.answer_label.visible = True

  @handle("next_button", "click")
  def next_button_click(self, **event_args):
    if not self.cards:
      return
    self.current_index = (self.current_index + 1) % len(self.cards)
    self.show_card()

  @handle("prev_button", "click")
  def prev_button_click(self, **event_args):
    if not self.cards:
      return
    self.current_index = (self.current_index - 1) % len(self.cards)
    self.show_card()

  @handle("add_cards_button", "click")
  def add_cards_button_click(self, **event_args):
    open_form('NewCard', deck_name=self.deck_name)

  @handle("back_button", "click")
  def back_button_click(self, **event_args):
    open_form('Flashcards')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass