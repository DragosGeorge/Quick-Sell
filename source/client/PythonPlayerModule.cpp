Add:
PyObject* playerRefreshInventory(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer::Instance().RefreshInventory();

	return Py_BuildNone();
}

Add:
		{ "RefreshInventory",			playerRefreshInventory,				METH_VARARGS },