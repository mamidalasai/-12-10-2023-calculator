from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    sub = self.text_box_1.text - self.text_box_2.text
    alert("substract of number1 and number2 is:-  " + str(sub))
    self.button_2.background = '#00FF00'
    self.button_2.foreground = 'white'
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    sum = self.text_box_1.text + self.text_box_2.text
    alert("sum of number1 and number2 is:-  " + str(sum))
    self.button_1.background = '#00FF00'
    self.button_1.foreground = 'white'
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    mul = self.text_box_1.text * self.text_box_2.text
    alert("multiplication of number1 and number2 is:-  " + str(mul))
    self.button_3.background = '#00FF00'
    self.button_3.foreground = 'white'
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    div = self.text_box_1.text / self.text_box_2.text
    alert("division of number1 and number2 is:-  " + str(div))
    self.button_4.background = '#00FF00'
    self.button_4.foreground = 'white'
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    per = self.text_box_1.text % self.text_box_2.text
    alert("percentage of number1 and number2 is  " + str(per))
    self.button_5.background = '#00FF00'
    self.button_5.foreground = 'white'
    pass

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    pow = self.text_box_1.text ** self.text_box_2.text
    alert("power of number1 and number2 is  " + str(pow))
    self.button_6.background = '#00FF00'
    self.button_6.foreground = 'white'
    pass








