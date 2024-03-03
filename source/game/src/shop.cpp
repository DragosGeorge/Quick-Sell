Search and modify as below:
#ifdef REMOVE_SHOP_EMPIRE_TAX
if (it->second)
      dwPrice *= 0;
#else
if (it->second)   // if other empire, price is triple
      dwPrice *= 3;
#endif


Search iVal = 3; and modify as below:

#ifdef REMOVE_SHOP_EMPIRE_TAX
			iVal = 0;
#else
			iVal = 3;
#endif

Search:

    if (bOtherEmpire) // no empire price penalty for pc shop
         pack2.items.price = item.price * 3;
    else
		pack2.items[i].price = item.price;

Change with:

#ifdef REMOVE_SHOP_EMPIRE_TAX
		if (bOtherEmpire) // no empire price penalty for pc shop
			pack2.items[i].price = item.price;
		else
			pack2.items[i].price = item.price;
#else
		if (bOtherEmpire) // no empire price penalty for pc shop
			pack2.items[i].price = item.price * 3;
		else
			pack2.items[i].price = item.price;
#endif