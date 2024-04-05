Add:

if app.QUICK_SELL_SYSTEM:
	import uiQuickSell

Search:

		self.wndGuild = None

Add below:

		if app.QUICK_SELL_SYSTEM:
			self.wndQuickSell = None

Search:

	def __MakeGuildWindow(self):
		self.wndGuild = uiGuild.GuildWindow()

Add below:

	if app.QUICK_SELL_SYSTEM:
		def __MakeQuickSell(self):
			self.wndQuickSell = uiQuickSell.QuickSell()
			self.wndQuickSell.Hide()

Search:

		self.__MakeCubeResultWindow()

Add below:

		if app.QUICK_SELL_SYSTEM:
			self.__MakeQuickSell()

Search:

		self.wndChatLog.Destroy()

Search def Close(self): and add :

		if app.QUICK_SELL_SYSTEM:
			if self.wndQuickSell:
				self.wndQuickSell.Hide()

Search def HideAllWindows(self): and add:

		if app.QUICK_SELL_SYSTEM:
			if self.wndQuickSell:
				self.wndQuickSell.Hide()

Search:

		del self.wndItemSelect

Add below:

		if app.QUICK_SELL_SYSTEM:
			del self.wndQuickSell

Search:

		if self.wndExpandedTaskBar:
			hideWindows += self.wndExpandedTaskBar,

Add below:

		if app.QUICK_SELL_SYSTEM:
			if self.wndQuickSell:
				hideWindows += self.wndQuickSell,

Search:

	def EmptyFunction(self):
		pass

Add below:

	if app.QUICK_SELL_SYSTEM:
		def IsShowQuickSell(self):
			return self.wndQuickSell.IsShow()

		def AppendQuickSellSlot(self, slotIndex):
			if self.wndInventory.IsShow() and not self.IsShowQuickSell():
				self.AdjustQuickSell()
			self.wndQuickSell.AppendSellSlot(slotIndex)

		def AppendQuickSellSlotSpecialInventory(self, slotIndex):
			if self.wndSpecialInventory.IsShow() and not self.IsShowQuickSell():
				self.AdjustQuickSell()
			self.wndQuickSell.AppendSellSlot(slotIndex)
		
		def RemoveQuickSellSlot(self, slotIndex):
			self.wndQuickSell.RemoveSellSlot(slotIndex)

		def UpdateQuickSellPrice(self):
			self.wndQuickSell.UpdatePrice()

		def AdjustQuickSell(self):
			x, y = self.wndInventory.GetGlobalPosition()
			x -= self.wndQuickSell.QUICK_SELL_WIDTH

			self.wndQuickSell.AdjustPosition(x, y + 150)

		def AppendSellSlot(self, slotIndex):
			self.AppendQuickSellSlot(slotIndex)
			self.UpdateQuickSellPrice()

		def AppendSellSlotSpecialInventory(self, slotIndex):
			self.AppendQuickSellSlotSpecialInventory(slotIndex)
			self.UpdateQuickSellPrice()
		
		def RemoveSellSlot(self, slotIndex):
			self.RemoveQuickSellSlot(slotIndex)
			self.UpdateQuickSellPrice()
