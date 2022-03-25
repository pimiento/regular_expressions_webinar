#!/usr/bin/env python3
import numpy as np


class KMP:

    def __init__(self, pattern: str, R: int = 2**16):
        self.R = R
        self.pattern = pattern
        self.M = len(pattern)
        self.dfa = np.empty((R, self.M), dtype=np.int16)
        self.dfa[ord(self.pattern[0])][0] = 1
        X = 0
        for j in range(1, self.M):
            for c in range(R):
                # copy mismatch cases
                self.dfa[c][j] = self.dfa[c][X]
            # set match case
            self.dfa[ord(self.pattern[j])][j] = j+1
            # update restart state
            X = self.dfa[ord(self.pattern[j])][X]

    def search(self, text: str) -> int:
        N = len(text)
        j = 0
        for i in range(N):
            if j >= self.M:
                break
            j = self.dfa[ord(text[i])][j]
        if j == self.M:
            # found
            return i - self.M
        # not found
        return -1

kmp1 = KMP("abc")
print(kmp1.search("abcd"))
print(kmp1.search("fooabcd"))
print(kmp1.search("foobar"))
