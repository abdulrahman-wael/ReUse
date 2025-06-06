from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Product import Product

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    best_sellers = app_tables.products.search(best_seller=True)
    
    # self.banner.role = ['spaced-title', 'left-right-padding']
    
    for p in best_sellers:
      self.flow_panel_1.add_component(Product(item=p), width='30%')




