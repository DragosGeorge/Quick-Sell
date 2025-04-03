Add before void initwndMgr()

PyObject *wndMgrSetSlotCoverImage(PyObject *poSelf, PyObject *poArgs)
{
	UI::CWindow *pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();

	DWORD dwSlotIndex;
	if (!PyTuple_GetUnsignedLong(poArgs, 1, &dwSlotIndex))
		return Py_BuildException();

	char *szFileName;
	if (!PyTuple_GetString(poArgs, 2, &szFileName))
		return Py_BuildException();

	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	dynamic_cast<UI::CSlotWindow*>(pWin)->SetSlotCoverImage(dwSlotIndex, szFileName);

	return Py_BuildNone();
}

PyObject *wndMgrEnableSlotCoverImage(PyObject *poSelf, PyObject *poArgs)
{
	UI::CWindow *pWin;
	if (!PyTuple_GetWindow(poArgs, 0, &pWin))
		return Py_BuildException();

	DWORD dwSlotIndex;
	if (!PyTuple_GetUnsignedLong(poArgs, 1, &dwSlotIndex))
		return Py_BuildException();

	bool bOnOff;
	if (!PyTuple_GetBoolean(poArgs, 2, &bOnOff))
		return Py_BuildException();

	if (!pWin->IsType(UI::CSlotWindow::Type()))
		return Py_BuildException();

	dynamic_cast<UI::CSlotWindow*>(pWin)->EnableSlotCoverImage(dwSlotIndex, bOnOff);

	return Py_BuildNone();
}

And look for:

{ "ShowOverInWindowName",		wndMgrShowOverInWindowName,			METH_VARARGS },

Add after:

		{ "SetSlotCoverImage",			wndMgrSetSlotCoverImage,			METH_VARARGS },
		{ "EnableSlotCoverImage",		wndMgrEnableSlotCoverImage,			METH_VARARGS },