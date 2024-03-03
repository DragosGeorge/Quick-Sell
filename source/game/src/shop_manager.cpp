Search and modify as below:

void CShopManager::Sell(LPCHARACTER ch, WORD wCell, WORD wCount, BYTE bType)
{
	if (!ch->CanHandleItem())
		return;
	
#ifdef REMOVE_SHOP_CHECK
	if (ch->GetShop())
	{
		if (ch->GetShop()->IsPCShop())
			return;
	}

#else
	if (!ch->GetShop())
		return;

	if (!ch->GetShopOwner())
		return;

	if (ch->GetShop()->IsPCShop())
		return;

	if (DISTANCE_APPROX(ch->GetX() - ch->GetShopOwner()->GetX(), ch->GetY() - ch->GetShopOwner()->GetY()) > 2000)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You are too far away from the shop to sell something."));
		return;
	}
#endif

	LPITEM item = ch->GetInventoryItem(wCell);

Search int iVal = 3; and modify as below:

#ifdef REMOVE_SHOP_EMPIRE_TAX
	int iVal = 0;
#else
	int iVal = 3;
#endif



