Add:

#if defined(QUICK_SELL_SYSTEM)
	PyModule_AddIntConstant(poModule, "QUICK_SELL_SYSTEM", true);
#else
	PyModule_AddIntConstant(poModule, "QUICK_SELL_SYSTEM", false);
#endif