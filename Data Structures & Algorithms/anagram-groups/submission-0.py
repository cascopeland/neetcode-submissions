class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        list_groups = []
        # go through each string in list
        for i in strs:
            alph = [0] * 26
            # go through each character in word
            for char in i:
                # 
                alph[(ord(char) - ord("a"))] += 1
            # groups key is a list where the index represents alphabet and index value is frequency
            # groups value is the words
            groups[tuple(alph)].append(i)
        # so for each word in groups, append the values into the list
        for key in groups:
            list_groups.append(groups[key])
        return list_groups
        