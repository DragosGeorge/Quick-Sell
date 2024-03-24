Search self.AddItemData( in def SetInventoryItem

Add below:

		if app.QUICK_SELL_SYSTEM:
			self.AppendQuckSellItem(slotIndex)

Search:

	def __IsNewHair(self, itemVnum):

Add below:

	if app.QUICK_SELL_SYSTEM:
		def AppendQuckSellItem(self,slotIndex):
			if player.IsEquipmentSlot(slotIndex):
				return
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				return
			else:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.QUICK_SELL_TOOLTIP, self.NORMAL_COLOR)
