Add:
void CPythonPlayer::RefreshInventory()
{
	PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
}