import heapq as hq
#TC - 0(nlogk),SC - O(k)
class heapNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
    
    def __lt__(self,other):
        if self.val == other.val:
            return self.key>other.key
        return self.val<other.val
    
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.hmap={}
        for i,word in enumerate(sentences):
            self.hmap[word] = times[i]
        self.sb = []
            
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c=='#':
            search_term = "".join(self.sb)
            self.hmap[search_term] = self.hmap.get(search_term,0)+1
            self.sb = []
            return # after the end of input we are returning
        else:    
            self.sb.append(c)
            heap =[]
            search_term = "".join(self.sb)
            for key in self.hmap.keys():
                if key.startswith(search_term):
                    hq.heappush(heap,heapNode(key,self.hmap[key]))
                    if len(heap)>3:
                        hq.heappop(heap)

            result = [None]*len(heap)
            i = len(heap)-1
            while heap:
                res = hq.heappop(heap)
                result[i] = res.key
                i-=1
                
        return result
#==================================================
#Approach -2 
#TC - 0(1),SC - huge
class TrieNode:
    def __init__(self):
        self.children = [None]*128
        self.top3 = []
        
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.hmap={}
        for i,word in enumerate(sentences):
            self.hmap[word] = times[i]
            self.insert(word)
        self.sb = []
    
    def insert(self,word):
        curr = self.root
        for char in word:
            idx = ord(char) 
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            if word not in curr.top3:
                curr.top3.append(word)
            curr.top3.sort(key = lambda x:(-1*self.hmap[x],x))
            while len(curr.top3)>3:
                curr.top3.pop()
    
    def search(self,search_term):
        curr = self.root
        for char in search_term:
            idx= ord(char) 
            if curr.children[idx] == None:
                return []
            curr = curr.children[idx]
        return curr.top3
                 
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            search_term = "".join(self.sb)
            self.hmap[search_term] = self.hmap.get(search_term,0)+1
            self.insert(search_term)
            self.sb=[]
            return []
        else:
            self.sb.append(c)
        
        return self.search("".join(self.sb))
