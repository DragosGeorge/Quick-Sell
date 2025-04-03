Search: def __SendMoveItemPacket(

Add:

		if self.interface and self.interface.wndQuickSell and self.interface.wndQuickSell.IsShow():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DONT_USE_ITEM_WHEN_SHOW_CONFIRM)
			return