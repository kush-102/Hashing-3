class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # rolling hash-rolling karps algo used with sliding window when substrings are to be formed where order matters basically

        # brute force
        # all_seq=set()
        # result=set()

        # for i in range(len(s)-9):
        #     sub=s[i:i+10]
        #     if sub in all_seq:
        #         result.add((sub))
        #     else:

        #         all_seq.add(sub)  # Add to seen if new

        # return list(result)

        # kmp
        if len(s) < 10:
            return []

        mapping = {"A": 1, "C": 2, "G": 3, "T": 4}

        seen = set()
        result = set()
        window_size = 10
        curr_hash = 0

        for i in range(window_size):
            curr_hash = curr_hash * 4 + mapping[s[i]]

        seen.add(curr_hash)

        for i in range(window_size, len(s)):
            old_char = s[i - window_size]
            new_char = s[i]
            old_contribution = mapping[old_char] * pow(4, window_size - 1)

            curr_hash = curr_hash - old_contribution

            curr_hash = curr_hash * 4

            curr_hash = curr_hash + mapping[new_char]

            curr_seq = s[i - window_size + 1 : i + 1]

            if curr_hash in seen:
                result.add(curr_seq)
            else:
                seen.add(curr_hash)

        return list(result)
