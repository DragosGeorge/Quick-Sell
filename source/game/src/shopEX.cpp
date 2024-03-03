Search:

    if (bOtherEmpire) // no empire price penalty for pc shop
		pack2.items[i].price = item.price * 3;
	else
		pack2.items[i].price = item.price;

Change with:

#ifdef REMOVE_SHOP_EMPIRE_TAX
	if (bOtherEmpire) // no empire price penalty for pc shop
		pack_tab.items[i].price = shop_tab.items[i].price;
	else
		pack_tab.items[i].price = shop_tab.items[i].price;
#else
	if (bOtherEmpire) // no empire price penalty for pc shop
		pack_tab.items[i].price = shop_tab.items[i].price * 3;
	else
		pack_tab.items[i].price = shop_tab.items[i].price;
#endif

Search:

    if (it->second) // if other empire, price is triple
		dwPrice *= 3;

Change with:

#ifdef REMOVE_SHOP_EMPIRE_TAX
        if (it->second) // if other empire, price is triple
            dwPrice *= 0;
#else
        if (it->second) // if other empire, price is triple
            dwPrice *= 3;
#endif

