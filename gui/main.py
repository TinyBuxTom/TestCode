from guizero import App, Text, Window, PushButton, Picture, Box

app = App(title="IncheckProto", width=800, height=480)
app.set_full_screen()


def open_window(currentWindow):
    currentWindow.show(wait=True)
    currentWindow.after(3000, lambda: close_window(currentWindow))


def close_window(currentWindow):
    currentWindow.hide()


text = Text(app, "\n")
pictureBox = Box(app)
# bar = Picture(pictureBox, image="barcode.png", width=200, height=100, align="right")
# spacer = Picture(pictureBox, image="spacer.png", width=100, height=200, align="right")
# qr = Picture(pictureBox, image="QR2.png", width=200, height=200, align="left")
hrlogo = Picture(pictureBox, image="hrlogo3.png", width=750, height=150)

text1 = Text(app, "Welkom bij het protolab", size=20)
text2 = Text(app, "Scan uw QR-code in de HR-app", size=20)
text3 = Text(app, "Of scan de barcode op uw HR-pas", size=20)

#open_button = PushButton(app, text="Open", command=lambda: open_window(windowSuccess))
#open_button1 = PushButton(app, text="Open", command=lambda: open_window(windowFailed))

windowSuccess = Window(app, title="Success", visible=False, width=800, height=480)
windowSuccess.set_full_screen()
text = Text(windowSuccess, "\n")
successImg = Picture(windowSuccess, image="vinkje.png", width=400, height=400)

windowFailed = Window(app, title="Failed", visible=False, width=800, height=480)
windowFailed.set_full_screen()
text = Text(windowFailed, "\n")
failedImg = Picture(windowFailed, image="kruis.png", width=400, height=400)


app.display()
