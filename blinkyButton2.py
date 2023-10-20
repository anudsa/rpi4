#Code to make an LED blink with a push button
from gpiozero import LED,Button
from signal import pause
#A new LED object is created and the gpio pin 26 is used
blueLED=LED(26)
#A new button object is instantiated with the gpio pin 2
pushButton=Button(2)

#pushButton.when_pressed = blueLED.on
#pushButton.when_released = blueLED.off

#The method blink is called
blueLED.blink()
#A pause is added so that it can be seen how LED blinks
pause()
