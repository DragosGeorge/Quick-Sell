Search:

void CSlotWindow::SetSlotCoolTimeInverse(DWORD dwIndex, float fCoolTime, float fRemainingTime)

Add above or after whole function:

void CSlotWindow::SetSlotCoverImage(const DWORD dwIndex, const char* FileName)
{
	TSlot* pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	auto& CoverImage = pSlot->pCoverImage;
	if (CoverImage == nullptr)
		CoverImage = std::make_shared<CImageBox>(nullptr);

	CoverImage->LoadImage(FileName);
	CoverImage->Show();
}

void CSlotWindow::EnableSlotCoverImage(const DWORD dwIndex, const bool bEnable)
{
	TSlot* pSlot;
	if (!GetSlotPointer(dwIndex, &pSlot))
		return;

	const auto& CoverImage = pSlot->pCoverImage;
	if (CoverImage == nullptr)
		return;

	if (bEnable)
		CoverImage->Show();
	else
		CoverImage->Hide();
}

Search: Slot.pSignImage = nullptr;

Bellow add:

	Slot.pCoverImage = nullptr;

Search:

	if (pSlot->pSignImage)
	{
 		pSlot->pSignImage->Hide();
	}

Bellow add:

	if (pSlot->pCoverImage)
	{
		pSlot->pCoverImage->Hide();
	}


Search:

		if (rSlot.pNumberLine)
		{
			int ix = rSlot.byxPlacedItemSize*ITEM_WIDTH + rSlot.ixPosition - 4;
			int iy = rSlot.iyPosition + rSlot.byyPlacedItemSize*ITEM_HEIGHT - 12 + 2;
			rSlot.pNumberLine->SetPosition(ix, iy);
			rSlot.pNumberLine->Update();
			rSlot.pNumberLine->Render();
		}

Bellow add:

		if (rSlot.pCoverImage)
		{
			rSlot.pCoverImage->SetPosition(m_rect.left + rSlot.ixPosition, m_rect.top + rSlot.iyPosition);
			rSlot.pCoverImage->Render();
		}

