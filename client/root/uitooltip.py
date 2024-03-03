Search self.AddItemData( in def SetInventoryItem

Add below:

		if app.QUICK_SELL_SYSTEM:
			self.AppendQuckSellItem()

Search:

	def __IsNewHair(self, itemVnum):

Add below:

	if app.QUICK_SELL_SYSTEM:
		def AppendQuckSellItem(self):
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				return
			else:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.QUICK_SELL_TOOLTIP, self.NORMAL_COLOR)