import requests as rq
import datetime as dt
import time as tm

workshop = "Houtwerkplaats"

def listToString (inputList): 
    returnString = "" 
    return (returnString.join(inputList))

while (True):
    tm.sleep (0.01)
    rawInput = input()

    studentNumList = list (rawInput)
    codeType = studentNumList.pop (0)

    if (codeType == 'b'): 
        print ("CodeType: Barcode (Code 39)")
        codeType = "Barcode"
    elif (codeType == 'Q'):
        print ("CodeType: QR-Code")
        codeType = "QR-code"

    studentNumString = listToString (studentNumList)
    print (studentNumString)
    
    url = 'http://145.24.222.39:8001/register'
    x = dt.datetime.now ()
    
    jsonData = { 
            'stnum' : studentNumString,
            'date' : x.strftime ("%Y-%m-%d"),
            'method' : codeType,
            'workshop' : workshop
            }

    x = rq.post (url, json = jsonData)
    print (x.status_code)
    print ()
    
    #check for int (if not, return false and red light on)