from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    self.colorpicker.set_color('#ff0000')
    self._update_label()

  def colorpicker_change(self, **event_args):
    self._update_label()
    
  def _update_label(self):
    self.label_1.foreground = self.colorpicker.get_color()


