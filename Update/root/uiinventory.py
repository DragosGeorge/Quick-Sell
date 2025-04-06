Search: def __SendMoveItemPacket(

Add:

		if self.interface and self.interface.wndQuickSell and self.interface.wndQuickSell.IsShow():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DONT_USE_ITEM_WHEN_SHOW_CONFIRM)
			return

Search in class BeltInventoryWindow(ui.ScriptWindow):

        self.wndBeltInventorySlot.RefreshSlot()

Add above:

        if app.QUICK_SELL_SYSTEM:
            self.RefreshIconSlot()

Add this function:

    if app.QUICK_SELL_SYSTEM:
        def RefreshIconSlot(self):
            for k in xrange(item.BELT_INVENTORY_SLOT_COUNT):
                slotNumber = item.BELT_INVENTORY_SLOT_START + k
                itemVnum = player.GetItemIndex(slotNumber)
                if slotNumber in constInfo.QUICK_SELL_ITEMS:
                    self.wndBeltInventorySlot.SetSlotCoverImage(slotNumber, "d:/ymir work/inventory/selected_icon.tga")
                else:
                   self.wndBeltInventorySlot.EnableSlotCoverImage(slotNumber, False)

