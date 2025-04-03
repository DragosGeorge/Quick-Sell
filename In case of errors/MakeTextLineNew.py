Search in ui.py:

def MakeTextLine(parent):

Add Bellow:

def MakeTextLineNew(parent, x, y, text):
	textLine = TextLine()
	textLine.SetParent(parent)
	textLine.SetPosition(x, y)
	textLine.SetText(text)
	textLine.Show()
	return textLine

Search in uiQuickSell.py:

ui.MakeTextLine

And replace with:

ui.MakeTextLineNew




