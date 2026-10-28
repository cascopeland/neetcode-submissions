class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        string_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            #so this would get the 5
            word_len = s[i:j]
            word = s[j + 1:j + 1 + int(word_len)]
            string_list.append(word)
            i = j + 1 + int(word_len)
        return string_list