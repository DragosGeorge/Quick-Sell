Add in :

	def RefreshBagSlotWindow(self):

This:

		if app.QUICK_SELL_SYSTEM:
			self.RefreshQuickSell()

Search in def __UseItem(self, slotIndex): 

		item.SelectItem(ItemVNum)

Add below:

		if app.QUICK_SELL_SYSTEM:
			if app.IsPressed(app.DIK_LSHIFT):
				if slotIndex in constInfo.QUICK_SELL_ITEMS:
					self.interface.RemoveSellSlot(slotIndex)
					self.RefreshBagSlotWindow()
					return
				else:
					self.interface.AppendSellSlot(slotIndex)
					self.RefreshBagSlotWindow()
					return

Add at the end:

	if app.QUICK_SELL_SYSTEM:
		def RefreshQuickSell(self):
			for k in xrange(player.INVENTORY_PAGE_SIZE * 5):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(k)
				if slotNumber in constInfo.QUICK_SELL_ITEMS:
					self.wndItem.SetSlotCoverImage(k, "inventory/selected_icon.tga")
				else:
					self.wndItem.EnableSlotCoverImage(k, False)