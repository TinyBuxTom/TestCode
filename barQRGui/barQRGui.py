from guizero import App, Text, Window, PushButton, Picture, Box, TextBox
from pynput.keyboard import Listener, Key
import threading

workshop = "Houtwerkplaats"

# ===============================================

app = App(title="IncheckProto", width=800, height=480)
#app.set_full_screen()

text = Text(app, "\n")
pictureBox = Box(app)
hrlogo = Picture(pictureBox, image="hrlogo3.png", width=750, height=150)

text1 = Text(app, "\nWelkom bij de {}".format(workshop), size=20)
text2 = Text(app, "Scan uw QR-code in de HR-app", size=20)
text3 = Text(app, "Of scan de barcode op uw HR-pas", size=20)

windowSuccess = Window(app, title="Success", visible=False, width=800, height=480)
#windowSuccess.set_full_screen()
text = Text(windowSuccess, "\n")
successImg = Picture(windowSuccess, image="vinkje.png", width=400, height=400)

windowFailed = Window(app, title="Failed", visible=False, width=800, height=480)
#windowFailed.set_full_screen()
text = Text(windowFailed, "\n")
failedImg = Picture(windowFailed, image="kruis.png", width=400, height=400)

def open_window(currentWindow):
    currentWindow.show(wait=True)
    currentWindow.after(3000, lambda: close_window(currentWindow))

def close_window(currentWindow):
    currentWindow.hide()

# ===============================================

studentNumList = list ()
listener = None

def listToString (inputList): 
    returnString = "" 
    return (returnString.join(inputList))

def on_press (key):
    if (key == Key.enter):
        print (studentNumList)
        codeType = studentNumList.pop (0)

        if (codeType == 'b' or codeType == 'B'): 
            print ("CodeType: Barcode (Code 39)")
            codeType = "Barcode"
        elif (codeType == 'Q' or codeType == 'q'):
            print ("CodeType: QR-Code")
            codeType = "QR-code"

        studentNumString = listToString (studentNumList)
        print (studentNumString)
        studentNumList.clear ()

        if (studentNumString.isnumeric() and len (studentNumString) == 7):
            #success
            print ("Success")
            open_window (windowSuccess)
        else:
            #failed
            print ("Failed")
            open_window (windowFailed)
    
    elif (hasattr (key, 'char')):
        studentNumList.append (key.char)

if listener == None:  
    listener = Listener (on_press = on_press)
    listener.start ()

app.display()
