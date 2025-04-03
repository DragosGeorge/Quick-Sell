Search: def MakeImageBox

Add:

def MakeBoardWithTitleBar(parent, flag, title, closeEvent, width, height):
	board = BoardWithTitleBar()
	board.SetParent(parent)
	board.SetSize(width, height)
	board.AddFlag(flag)
	board.SetTitleName(title)
	board.SetCloseEvent(closeEvent)
	board.Show()
	return board