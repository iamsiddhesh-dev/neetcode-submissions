class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            seen = {}
            current_streak = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    current_streak += 1
                    seen[s[j]] = j
                else:
                    break
            longest = max(longest, current_streak)
        return longest