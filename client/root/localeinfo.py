Add:

	def NumberToDecimalStringQuickSell(n):
		return "%s" % ('.'.join([i - 3 < 0 and str(n / 5)[:i] or str(n / 5)[i - 3:i] for i in range(len(str(n / 5)) % 3, len(str(n / 5)) + 1, 3) if i]))
