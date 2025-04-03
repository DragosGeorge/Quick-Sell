Search:

void RefreshSlot();

Add:

			void SetSlotCoverImage(const DWORD dwIndex, const char* FileName);
			void EnableSlotCoverImage(const DWORD dwIndex, const bool bEnable);


Search:

CAniImageBox* pFinishCoolTimeEffect;

Add bellow:

std::shared_ptr< CImageBox > pCoverImage;