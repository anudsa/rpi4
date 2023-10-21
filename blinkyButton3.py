#Code to make an LED blink with a push button
from gpiozero import LED,Button
from signal import pause
#A new LED object is created and the gpio pin 26 is used
blueLED=LED(26)
#A new button object is instantiated with the gpio pin 2
pushButton=Button(2)
#The LED is turned on when the button is pressed
pushButton.when_pressed = blueLED.on
#The LED is turned off when the button is released
pushButton.when_released = blueLED.off

#A pause is added so that it can be seen how LED blinks
pause()
