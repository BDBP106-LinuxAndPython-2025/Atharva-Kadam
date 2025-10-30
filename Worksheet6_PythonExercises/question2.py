"""(2) Here’s a DNA sequence with the bits that we want to extract in bold: ACTGCAT-
TATATCGTACGAAATTATACGCGCG Extract the bits of the string that match the
pattern (highlighted in bold) using findall():"""

"ACTGCATTATATCGTACGAAATTATACGCGCG"

import re

seq="ACTGCATTATATCGTACGAAATTATACGCGCG"
pattern=r"TATATCGTACGAAATTATACGCGCG"


match=re.findall(pattern,seq)

print(match)
