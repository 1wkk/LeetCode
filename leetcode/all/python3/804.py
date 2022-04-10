from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len(
            set(
                [''.join(map(lambda a: dic[ord(a) - ord('a')], word)) for word in words]
            )
        )
