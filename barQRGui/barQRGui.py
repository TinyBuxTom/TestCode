from guizero import App, Text, Window, Picture, Box
from pynput.keyboard import Listener, Key
import threading
from gpiozero import Buzzer, LED
from time import sleep
import requests as rq

# ===============================================

workshopList = ["Aqualab", "Elektrolab", "Energielab", "Houtwerkplaats", "Lijmlab", "Materialenlab", "Metaalwerkplaats", "Mobiliteitslab", "Protolab"]
articleList = ["de", "het"]

# ===============================================

workshop = workshopList [8] #change number to according workshop

# ===============================================

articleGUIText = ""
if (workshop == workshopList [3] or workshop == workshopList [6]):
    articleGUIText = articleList [0]
else: 
    articleGUIText = articleList [1] 

# ===============================================

studentNumList = list ()
listener = None

def makeListener ():
    global listener
    listener = None
    listener = Listener (on_press = on_press)
    listener.start ()

def listToString (inputList): 
    returnString = "" 
    return (returnString.join (inputList))

# ===============================================

app = App (title="RegistratiePaalGUI", width=800, height=480)
app.set_full_screen ()

text = Text (app, "\n")
pictureBox = Box (app)
hrlogo = Picture (pictureBox, image="hrlogo3.png", width=750, height=150)

Text (app, "\nWelkom bij {} {}\n\nScan uw QR-code in de HR-app\nOf scan de barcode op uw HR-pas".format (articleGUIText, workshop), size=30)

windowSuccess = Window (app, title="Success", visible=False, width=800, height=480)
windowSuccess.set_full_screen ()
Text (windowSuccess, "\n")
successImg = Picture (windowSuccess, image="vinkje.png", width=400, height=400)

windowFailed = Window (app, title="Failed", visible=False, width=800, height=480)
windowFailed.set_full_screen ()
Text (windowFailed, "\n")
failedImg = Picture (windowFailed, image="kruis.png", width=400, height=400)

windowConnError = Window (app, title="Connection Error", visible=False, width=800, height=480)
windowConnError.set_full_screen ()
Text (windowConnError, "\n\nEr kan geen connectie worden gemaakt\nmet het internet of de API.\n\nControleer de internetaansluiting en\nraadpleeg anders een medewerker.\n\nProbeer het later opnieuw.", size=30)

windowAPI404 = Window (app, title="API 404 Error Code", visible=False, width=800, height=480)
windowAPI404.set_full_screen ()
Text (windowAPI404, "\n\nHTTP 404\n\nDe opgevraagde pagina kan niet\nworden geladen.\nProbeer het later opnieuw.", size=30)

#windowAPI404, windowAPI...

def open_window (currentWindow):
    currentWindow.show (wait=True)
    currentWindow.after (2000, lambda: close_window (currentWindow))

def open_window_error (currentWindow):
    listener.stop ()
    currentWindow.show (wait=True)
    currentWindow.after (10000, lambda: close_window(currentWindow))
    makeListener ()

def close_window (currentWindow):
    currentWindow.hide ()

# ===============================================

buzzer = Buzzer (12)

def buzzValid ():
    buzzer.value = 1
    sleep (0.6)
    buzzer.value = 0

timeX = 0.2
def buzzInvalid ():
    buzzer.value = 1
    sleep (timeX)
    buzzer.value = 0
    sleep (timeX)
    buzzer.value = 1
    sleep (timeX)
    buzzer.value = 0
    sleep (timeX)
    buzzer.value = 1
    sleep (timeX)
    buzzer.value = 0

def threadBuzzValid ():
    buzzerThread = threading.Thread (target = buzzValid ())
    buzzerThread.start ()
    
def threadBuzzInvalid ():
    buzzerThread = threading.Thread (target = buzzInvalid ())
    buzzerThread.start ()

# ===============================================

def on_press (key):
    if (key == Key.enter):
        #print (studentNumList)
        if not (studentNumList):
            open_window (windowFailed)
        else:   
            codeType = studentNumList.pop (0)

            if (codeType == 'b' or codeType == 'B'): 
                print ("CodeType: Barcode (Code 39)")
                codeType = "Barcode"
            elif (codeType == 'Q' or codeType == 'q'):
                print ("CodeType: QR-Code")
                codeType = "QR-code"
                
            studentNumString = listToString (studentNumList)
            print ("StudentNumString:", studentNumString)
            studentNumList.clear ()
            
            if (studentNumString.isnumeric () and len (studentNumString) == 7): #studentNumString is correct format (studentnumber from HR)
                try:
                    url = 'https://81.169.254.222/register'
                    
                    jsonData = {
                                'stnum' : studentNumString,
                                'method' : codeType,
                                'workshop' : workshop
                                }
                    
                    postReq = rq.post (url, json = jsonData)
                    print ("Status Code:", postReq.status_code)
                    
                    if (postReq.status_code == 200): #success
                        open_window (windowSuccess)
                        threadBuzzValid ()
                    elif (postReq.status_code == 401):
                        open_window_error (windowFailed) 
                        threadBuzzInvalid ()
                    elif (postReq.status_code == 404):
                        open_window_error (windowAPI404)
                        threadBuzzInvalid ()
                    
                except:
                    open_window_error (windowConnError) 
                    threadBuzzInvalid ()
                
            else:
                #failed
                print ("Failed\n")
                open_window (windowFailed)
                threadBuzzInvalid ()
    
    elif (hasattr (key, 'char')):
        studentNumList.append (key.char)

makeListener ()
app.display()
