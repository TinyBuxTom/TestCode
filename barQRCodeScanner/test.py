#import datetime as dt
#x = dt.datetime.now ()
#print (x.strftime ("%Y/%m/%d"))

#testString = "1003212"
#print ("string length:", len (testString))

from pynput.keyboard import Listener, Key  

keyList = list ()

def listToString (inputList): 
    returnString = "" 
    return (returnString.join(inputList))

def on_press (key):
    if (key == Key.enter):
        print (listToString(keyList))
        keyList.clear ()
    
    elif (hasattr (key, 'char')):
        keyList.append (key.char)

with Listener (on_press = on_press) as listener:  # Setup the listener
    listener.join ()  # Join the thread to the main thread