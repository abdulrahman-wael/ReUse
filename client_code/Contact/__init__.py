from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.map_1.center = GoogleMap.LatLng(40.7128, -74.0060)
    # self.map_1.zoom = 15
    # icon = GoogleMap.Icon(url="_/theme/maps-icon.png")
    # self.marker = GoogleMap.Marker(animation=GoogleMap.Animation.DROP, 
                              # position=GoogleMap.LatLng(40.7128, -74.0060),
                              # icon = icon)
    # self.map_1.add_component(self.marker)
    
 #
  def send_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    message = self.message_box.text
    
    if name and email and message:
      anvil.server.call('add_message', name, email, message)
      self.name_box.text = ""
      self.email_box.text = ""
      self.message_box.text = ""
      alert("Thanks for getting in touch!")
    else:
      alert("Please fill out the entire form before sending your message")
      





