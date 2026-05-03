from ._anvil_designer import FlashcardsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Flashcards(FlashcardsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_decks()

  def load_decks(self):
    decks = list(app_tables.decks.search())
    if not decks:
      self.decks_label.text = "No decks yet. Create one above!"
      return
    self.decks_label.text = "\n".join([f"• {d['deck_name']}" for d in decks])

  @handle("create_deck_button", "click")
  def create_deck_button_click(self, **event_args):
    name = self.deck_name_input.text.strip()
    if not name:
      alert("Please enter a deck name!")
      return
    existing = app_tables.decks.get(deck_name=name)
    if existing:
      alert("A deck with that name already exists!")
      return
    app_tables.decks.add_row(deck_name=name, username="")
    self.deck_name_input.text = ""
    self.load_decks()

  @handle("open_deck_button", "click")
  def open_deck_button_click(self, **event_args):
    name = self.deck_name_input.text.strip()
    if not name:
      alert("Enter the deck name you want to open!")
      return
    deck = app_tables.decks.get(deck_name=name)
    if not deck:
      alert("Deck not found!")
      return
    open_form('StudyDeck', deck_name=name)

  @handle("add_cards_button", "click")
  def add_cards_button_click(self, **event_args):
    name = self.deck_name_input.text.strip()
    if not name:
      alert("Enter the deck name you want to add cards to!")
      return
    open_form('NewCard', deck_name=name)


  @handle("Dashboard_button", "click")
  def Dashboard_button_click(self, **event_args):
    open_form('Dashboard')

  @handle("mindmap_button", "click")
  def mindmap_button_click(self, **event_args):
    open_form('MindMap')


  @handle("blok_button", "click")
  def blok_button_click(self, **event_args):
    open_form('Blok')

  @handle("feedback_button", "click")
  def feedback_button_click(self, **event_args):
    open_form('Fback_Form')

  @handle("flashcard_button", "click")
  def flashcard_button_click(self, **event_args):
    open_form('Flashcards')

  @handle("", "hide")
  def form_hide(self, **event_args):
    pass