Search in ui.py:

def MakeTextLine(parent):

Add Bellow:

def MakeTextLineNew(parent, horizontalAlign=True, verticalAlgin=True, x=0, y=0):
	textLine = TextLine()
	textLine.SetParent(parent)

	if horizontalAlign == True:
		textLine.SetWindowHorizontalAlignCenter()

	if verticalAlgin == True:
		textLine.SetWindowVerticalAlignCenter()

	textLine.SetHorizontalAlignCenter()
	textLine.SetVerticalAlignCenter()

	if x != 0 and y != 0:
		textLine.SetPosition(x, y)

	textLine.Show()
	return textLine

Search in uiQuickSell.py:

ui.MakeTextLine

And replace with:

ui.MakeTextLineNew




