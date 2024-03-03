import ui
import net
import localeInfo
import player
import item
import constInfo

class QuickSell(ui.Window):
	QUICK_SELL_WIDTH = 170
	def __init__(self): 
		ui.Window.__init__(self)
		self.cancelButton = None
		self.sellPrice = None
		self.sellItemSelectedCount = None
		self.sellPriceBG = None
		self.sellItemSelectedCountBG = None
		self.sellButton = None
		self.SetSize(170, 100)
		self.SetCenterPosition()
		self.AddFlag("movable")
		self.AddFlag("float")
		self.Hide()

		self.BoardInterface()

	def __del__(self):
		ui.Window.__del__(self)

	def Destroy(self):
		self.Hide()
		self.ResetWindow()
		player.RefreshInventory()

	def Close(self):
		self.Hide()
		self.ResetWindow()
		player.RefreshInventory()

	def Open(self):
		self.SetTop()
		self.Show()

	def ResetWindow(self):
		constInfo.QUICK_SELL_ITEMS = []
		self.UpdatePrice()

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

	def RemoveSellSlot(self, slotIndex):
		constInfo.QUICK_SELL_ITEMS.remove(slotIndex)
		if len(constInfo.QUICK_SELL_ITEMS) == 0:
			self.Close()

	def BoardInterface(self):

		self.Board = ui.MakeBoardWithTitleBar(self, "not_pick", "Sell Object",ui.__mem_func__(self.Close), 170, 100)

		self.sellButton = ui.MakeButton(self, self.QUICK_SELL_WIDTH / 2 - 70, 100 - 32, "", "d:/ymir work/ui/public/", "AcceptButton00.sub", "AcceptButton01.sub", "AcceptButton02.sub")
		self.sellButton.SetEvent(self.__OnClickSellButton)

		self.cancelButton = ui.MakeButton(self, self.QUICK_SELL_WIDTH / 2 + 10, 100 - 32, "","d:/ymir work/ui/public/", "CancleButton00.sub","CancleButton01.sub", "CancleButton02.sub")
		self.cancelButton.SetEvent(self.Close)

		self.sellItemSelectedCountBG = ui.MakeImageBox(self, "d:/ymir work/ui/quick_sell_value.png", 20, 29)

		self.sellPriceBG = ui.MakeImageBox(self, "d:/ymir work/ui/quick_sell_value.png",20, 47)

		self.sellItemSelectedCount = ui.MakeTextLine(self.sellItemSelectedCountBG, True, True, 0, 0)

		self.sellPrice = ui.MakeTextLine(self.sellPriceBG, True, True, 0, 0)

	def AdjustPosition(self, x, y):
		self.SetPosition(x, y)

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

		self.sellPrice.SetText("|Ikey/yang|i"+localeInfo.NumberToDecimalStringQuickSell(price))
		self.sellPrice.SetHorizontalAlignCenter()
		self.sellItemSelectedCount.SetText("Items selected: %d" % selected_count)
		self.sellItemSelectedCount.SetHorizontalAlignCenter()

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

	def OnPressEscapeKey(self):
		self.Close()
		player.RefreshInventory()
		return True

	def OnPressExitKey(self):
		self.Close()
		player.RefreshInventory()
		return True
