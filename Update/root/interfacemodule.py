Search and delete:

		if app.QUICK_SELL_SYSTEM:
			self.__MakeQuickSell()

Search and delete:

	if app.QUICK_SELL_SYSTEM:
		def __MakeQuickSell(self):
			self.wndQuickSell = uiQuickSell.QuickSell()
			self.wndQuickSell.Hide()

Search def __MakeWindows(self):

Add:

		if app.QUICK_SELL_SYSTEM:
			self.wndQuickSell = uiQuickSell.QuickSell()
			self.wndQuickSell.BindInterface(self)

Search:

		def MarkUnusableInvenSlotOnTopWnd(self

Add:

				elif onTopWnd == player.ON_TOP_WND_QUICK_SELL and self.wndQuickSell and self.wndQuickSell.CantSellItem(InvenSlot):
					return True
