from collections import Counter
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = Counter(re.findall('\w+', paragraph.lower())).most_common()
        for k, _ in words:
            if k not in banned:
                return k
        return ''
