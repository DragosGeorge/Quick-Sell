import ui
import net
import localeInfo
import player
import item
import constInfo
import app
import skill

class QuickSell(ui.Window):
	QUICK_SELL_WIDTH = 170
	BASE_HEIGHT = 100
	LOG_LINE_HEIGHT = 20
	MAX_NAME_LENGTH = 29
	ITEMS_PER_PAGE = 3

	def __init__(self):
		ui.Window.__init__(self)
		self.Board = None
		self.logBoard = None
		self.interface = None
		self.cancelButton = None
		self.sellPrice = None
		self.sellItemSelectedCount = None
		self.sellPriceBG = None
		self.sellItemSelectedCountBG = None
		self.sellButton = None
		self.logList = []
		self.logTextLines = []
		self.currentPage = 0
		self.prevButton = None
		self.nextButton = None
		self.pageText = None
		self.SetSize(self.QUICK_SELL_WIDTH, self.BASE_HEIGHT)
		self.SetCenterPosition()
		self.AddFlag("movable")
		self.AddFlag("float")
		self.Hide()

		self.BoardInterface()

	def BoardInterface(self):
		self.logBoard = ui.ThinBoard()
		self.logBoard.SetParent(self)
		self.logBoard.SetSize(self.QUICK_SELL_WIDTH - 20, 30)
		self.logBoard.SetPosition(10, self.BASE_HEIGHT - 10)
		self.logBoard.Show()

		self.Board = ui.MakeBoardWithTitleBar(self, "not_pick", localeInfo.QUICK_SELL_TITLE_NAME,ui.__mem_func__(self.Close), self.QUICK_SELL_WIDTH, self.BASE_HEIGHT)

		self.sellButton = ui.MakeButton(self.Board, self.QUICK_SELL_WIDTH / 2 - 70, self.BASE_HEIGHT - 32, "","d:/ymir work/ui/public/", "AcceptButton00.sub", "AcceptButton01.sub","AcceptButton02.sub")
		self.sellButton.SetEvent(self.__OnClickSellButton)

		self.cancelButton = ui.MakeButton(self.Board, self.QUICK_SELL_WIDTH / 2 + 10, self.BASE_HEIGHT - 32, "","d:/ymir work/ui/public/", "CancleButton00.sub", "CancleButton01.sub","CancleButton02.sub")
		self.cancelButton.SetEvent(self.Close)

		self.sellItemSelectedCountBG = ui.MakeImageBox(self.Board, "d:/ymir work/ui/quick_sell_value.png", 20, 29)
		self.sellPriceBG = ui.MakeImageBox(self.Board, "d:/ymir work/ui/quick_sell_value.png", 20, 47)
		self.sellItemSelectedCount = ui.MakeTextLine(self.sellItemSelectedCountBG, True, True, 0, 0)
		self.sellPrice = ui.MakeTextLine(self.sellPriceBG, True, True, 0, 0)

		self.logTextLines = []
		for i in xrange(self.ITEMS_PER_PAGE):
			textLine = ui.MakeTextLine(self.Board, False, True, 85, 60 + i * self.LOG_LINE_HEIGHT)
			textLine.SetHorizontalAlignCenter()
			textLine.SetTextColor(0xffffffff)
			textLine.Hide()
			self.logTextLines.append(textLine)

		self.prevButton = ui.MakeButton(self.logBoard, 40, self.ITEMS_PER_PAGE * self.LOG_LINE_HEIGHT + 15, "","d:/ymir work/ui/privatesearch/", "private_prev_btn_01.sub", "private_prev_btn_02.sub","private_prev_btn_01.sub")
		self.prevButton.SetEvent(self.__OnClickPrevPage)
		self.prevButton.Hide()

		self.pageText = ui.MakeTextLine(self.Board, False, True, 85, self.ITEMS_PER_PAGE * self.LOG_LINE_HEIGHT + 12+47)
		self.pageText.SetHorizontalAlignCenter()
		self.pageText.Hide()

		self.nextButton = ui.MakeButton(self.logBoard, 100, self.ITEMS_PER_PAGE * self.LOG_LINE_HEIGHT + 15, "","d:/ymir work/ui/privatesearch/", "private_next_btn_01.sub", "private_next_btn_02.sub","private_next_btn_01.sub")
		self.nextButton.SetEvent(self.__OnClickNextPage)
		self.nextButton.Hide()

		self.UpdateLogDisplay()

	def __del__(self):
		ui.Window.__del__(self)

	def Destroy(self):
		self.Hide()
		self.ResetWindow()
		player.RefreshInventory()

	def Close(self):
		self.Hide()
		self.ResetWindow()
		if self.interface:
			self.interface.SetOnTopWindow(player.ON_TOP_WND_NONE)
			self.interface.RefreshMarkInventoryBag()
		player.RefreshInventory()

	def Open(self):
		self.SetTop()
		self.Show()
		self.OnTop()
		if self.logBoard:
			self.logBoard.SetPosition(10, self.BASE_HEIGHT - 10)
		self.UpdateLogDisplay()

	def ResetWindow(self):
		constInfo.QUICK_SELL_ITEMS = []
		self.logList = []
		self.UpdatePrice()
		self.UpdateLogDisplay()

	def AppendSellSlot(self, slotIndex):
		if slotIndex in constInfo.QUICK_SELL_ITEMS:
			return

		if player.IsEquipmentSlot(slotIndex):
			return

		itemVnum = player.GetItemIndex(player.INVENTORY, slotIndex)
		if itemVnum == 0:
			return

		item.SelectItem(itemVnum)

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			return

		if not self.IsShow():
			self.Open()

		constInfo.QUICK_SELL_ITEMS.append(slotIndex)

		itemName = item.GetItemName()
		if itemVnum == 50300:
			metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			skillName = skill.GetSkillName(metinSlot[0])
			if skillName:
				itemName = "%s %s" % (skillName, itemName)

		if len(itemName) > self.MAX_NAME_LENGTH:
			itemName = itemName[:self.MAX_NAME_LENGTH] + "..."

		self.logList.append((slotIndex, itemName))
		self.UpdateLogDisplay()
		self.UpdatePrice()

	def RemoveSellSlot(self, slotIndex):
		if slotIndex in constInfo.QUICK_SELL_ITEMS:
			constInfo.QUICK_SELL_ITEMS.remove(slotIndex)
			self.logList = [entry for entry in self.logList if entry[0] != slotIndex]
			self.UpdateLogDisplay()
			if len(constInfo.QUICK_SELL_ITEMS) == 0:
				self.Close()
			self.UpdatePrice()

	def AdjustPosition(self, x, y):
		self.SetPosition(x, y)
		self.UpdateLogDisplay()

	def UpdatePrice(self):
		price = 0
		selected_count = 0
		for itemSlotIndex in constInfo.QUICK_SELL_ITEMS:
			itemIndex = player.GetItemIndex(itemSlotIndex)
			if itemIndex == 0:
				continue
			item.SelectItem(itemIndex)
			itemPrice = item.GetISellItemPrice()
			itemCount = player.GetItemCount(itemSlotIndex)
			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 1
			else:
				itemPrice = itemPrice * max(1, itemCount) / 1
			price += itemPrice
			selected_count += 1
		self.sellPrice.SetText("|Ikey/yang|i" + localeInfo.NumberToDecimalStringQuickSell(price))
		self.sellPrice.SetHorizontalAlignCenter()
		self.sellItemSelectedCount.SetText(localeInfo.QUICK_SELL_SELECTED_ITEMS + " %d" % selected_count)
		self.sellItemSelectedCount.SetHorizontalAlignCenter()

	def UpdateLogDisplay(self):
		for textLine in self.logTextLines:
			textLine.SetText("")
			textLine.Hide()

		activeItems = []
		for slotIndex in constInfo.QUICK_SELL_ITEMS:
			itemVnum = player.GetItemIndex(player.INVENTORY, slotIndex)
			if itemVnum:
				item.SelectItem(itemVnum)
				itemName = item.GetItemName()
				itemCount = player.GetItemCount(slotIndex)
				if itemVnum == 50300:
					metinSlot = [player.GetItemMetinSocket(slotIndex, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
					skillName = skill.GetSkillName(metinSlot[0])
					if skillName:
						itemName = "%s %s" % (skillName, itemName)
				if itemCount > 1:
					itemName = "%s (x%d)" % (itemName, itemCount)
				if len(itemName) > self.MAX_NAME_LENGTH:
					itemName = itemName[:self.MAX_NAME_LENGTH] + "..."
				activeItems.append((slotIndex, itemName))

		remainingItems = [entry for entry in self.logList if entry[0] not in constInfo.QUICK_SELL_ITEMS]
		displayItems = activeItems + remainingItems

		totalItems = len(displayItems)
		totalPages = max(1, (totalItems + self.ITEMS_PER_PAGE - 1) / self.ITEMS_PER_PAGE)
		self.currentPage = min(self.currentPage, totalPages - 1)
		if totalItems == 0:
			self.currentPage = 0

		displayItems = displayItems[::-1]

		startIndex = self.currentPage * self.ITEMS_PER_PAGE
		endIndex = min(startIndex + self.ITEMS_PER_PAGE, totalItems)
		pageItems = displayItems[startIndex:endIndex]

		for i, (slotIndex, itemName) in enumerate(pageItems):
			self.logTextLines[i].SetText(itemName)
			if slotIndex in constInfo.QUICK_SELL_ITEMS and self.HasBonus(slotIndex):
				self.logTextLines[i].SetTextColor(0xffFFC800)
			else:
				self.logTextLines[i].SetTextColor(0xffF2E7C1)
			self.logTextLines[i].Show()

		numItemsToShow = len(pageItems)
		if totalItems == 0:
			logBoardHeight = 30
			self.logBoard.SetSize(self.QUICK_SELL_WIDTH - 20, logBoardHeight)
			self.prevButton.Hide()
			self.nextButton.Hide()
			self.pageText.SetText("")
			self.pageText.Hide()
		elif totalItems < 3:
			logBoardHeight = numItemsToShow * self.LOG_LINE_HEIGHT + 10
			self.logBoard.SetSize(self.QUICK_SELL_WIDTH - 20, logBoardHeight)
			self.prevButton.Hide()
			self.nextButton.Hide()
			self.pageText.SetText("")
			self.pageText.Hide()
		else:
			logBoardHeight = self.ITEMS_PER_PAGE * self.LOG_LINE_HEIGHT + 36
			self.logBoard.SetSize(self.QUICK_SELL_WIDTH - 20, logBoardHeight)
			self.pageText.SetText("|cffb8a95e%d/%d" % (self.currentPage + 1, totalPages))
			self.pageText.Show()
			if self.currentPage > 0:
				self.prevButton.Show()
			else:
				self.prevButton.Hide()
			if self.currentPage < totalPages - 1:
				self.nextButton.Show()
			else:
				self.nextButton.Hide()

		totalHeight = self.BASE_HEIGHT + logBoardHeight - 10
		self.SetSize(self.QUICK_SELL_WIDTH, totalHeight)

	if app.WJ_ENABLE_TRADABLE_ICON:
		def BindInterface(self, interface):
			from _weakref import proxy
			self.interface = proxy(interface)
			if self.interface:
				self.interface.wndQuickSell = self

		def CantSellItem(self, slotIndex):
			itemIndex = player.GetItemIndex(slotIndex)
			if itemIndex:
				if app.ENABLE_SOUL_BIND_SYSTEM:
					if player.GetItemSealDate(player.INVENTORY, slotIndex) == -1 or player.GetItemSealDate(player.INVENTORY, slotIndex) > 0:
						return True
				return player.IsAntiFlagBySlot(slotIndex, item.ITEM_ANTIFLAG_SELL)
			return False

		def OnTop(self):
			if not self.interface:
				return
			self.interface.SetOnTopWindow(player.ON_TOP_WND_QUICK_SELL)
			self.interface.RefreshMarkInventoryBag()

	def HasBonus(self, slotIndex):
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrType, attrValue = player.GetItemAttribute(player.INVENTORY, slotIndex, i)
			if attrValue != 0:
				return True
		return False

	def __OnClickSellButton(self):
		for itemSlotIndex in constInfo.QUICK_SELL_ITEMS:
			self.sellingSlotNumber = itemSlotIndex
			itemIndex = player.GetItemIndex(itemSlotIndex)
			itemCount = player.GetItemCount(itemSlotIndex)
			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount
			net.SendShopSellPacketNew(self.sellingSlotNumber, self.sellingSlotitemCount, player.INVENTORY)
		constInfo.QUICK_SELL_ITEMS = []
		self.Close()
		player.RefreshInventory()

	def __OnClickPrevPage(self):
		if self.currentPage > 0:
			self.currentPage -= 1
			self.UpdateLogDisplay()

	def __OnClickNextPage(self):
		totalItems = len(self.logList)
		totalPages = (totalItems + self.ITEMS_PER_PAGE - 1) / self.ITEMS_PER_PAGE
		if self.currentPage < totalPages - 1:
			self.currentPage += 1
			self.UpdateLogDisplay()

	def OnPressEscapeKey(self):
		self.Close()
		player.RefreshInventory()
		return True

	def OnPressExitKey(self):
		self.Close()
		player.RefreshInventory()
		return True
