from ._anvil_designer import MainTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Shop import Shop
from ..Contact import Contact
from ..About import About
from ..Cart import Cart


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.navigate(self.home_link, Home())
    self.change_sign_in_text()
    self.cart_items = []
    
    for link in [self.home_link_copy, self.about_link_copy, self.contact_link_copy, self.my_items_link_copy, self.sign_in_copy, self.cart_link_copy]:
      link.role = ['spaced-title', 'display-responsive']
    
    for link in [self.home_link, self.about_link, self.contact_link, self.my_items_link, self.sign_in_link, self.cart_link]:
      link.role = ['spaced-title', 'display-none-responsive']
    
  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
    for i in self.cart_items:
      if i['product'] == product:
        i['quantity'] += quantity
        break
    else:
      self.cart_items.append({'product': product, 'quantity': quantity})
    
  def navigate(self, active_link, form):
    for i in [self.home_link, self.about_link, self.contact_link, self.my_items_link, self.sign_in_link, self.cart_link]:
      i.foreground = 'theme:Primary 700'
    active_link.foreground = 'theme:Secondary 500'
    self.column_panel_1.clear()
    self.column_panel_1.add_component(form, full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.home_link, Home())


  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.about_link, About())
    
  def contact_link_click(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    self.navigate(self.contact_link, Contact())

  def cart_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.cart_link, Cart(items=self.cart_items))

  def sign_in_link_click(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:
      anvil.users.login_with_form()
    self.change_sign_in_text()

  def subscribe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.subscribe_textbox.text
    if email:
      anvil.server.call('add_subscriber', email)
      self.subscribe_textbox.text = None
      Notification("Thanks for subscribing!").show()

  def toggle_my_items_link(self):
    self.my_items_link.visible = anvil.users.get_user() != None

  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.sign_in_link.text = email
    else:
      self.sign_in_link.text = "Sign In"
    
    self.toggle_my_items_link()

  def my_items_link(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.my_items_link, My_items() )








