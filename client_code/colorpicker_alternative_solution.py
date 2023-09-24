from ._anvil_designer import colorpicker_alternative_solutionTemplate
from anvil import *
import anvil
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class colorpicker_alternative_solution(colorpicker_alternative_solutionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def set_color(self, col_hex):
    anvil.js.call('setcolor', col_hex)
    
  def my_change_func(self, msg):    
    print('color changed')
    self.raise_event('change')