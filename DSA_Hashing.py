def get_hash(key):
    h = 0
    for char in key:
        h += ord(char) #Ord func will ASCII value to a character
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char) #Ord func will ASCII value to a character
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx ,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append([key,value])
        

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h].pop(idx)
                break
            
t = HashTable()
#t.add("March 6",130)
#print(t.get("March 6"))
#print(t.get_hash("March 6"))

t["March 6"] = 120
t["March 6"] = 78
t["March 17"] = 459
t["Feb 2"] = 120
t["April 1"] = 105

print(t.arr)
print("Python way of Getting : ",t["March 17"])
del t["March 6"]

print(t.arr)


################################################################     #######################################################################
########
#### LEET CODE QUESTION 


from collections import defaultdict
class Solution:
    def groupAnagram(self,strs : list[str]) -> list[list[str]] :
        anagram_map = defaultdict(list)
        result = []
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_map[sorted_word].append(word)
        
        for value in anagram_map.values():
            result.append(value)
        return result

sol = Solution()
print(sol.groupAnagram(["eat","tea","tan","ate","nat","bat"]))
