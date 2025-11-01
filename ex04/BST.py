from urllib import request
from Node import Node

class BST:

    def __init__(self, source:str, **kwargs):
        self.source = source
        words = []
        valbool = [False] * 2 
        for key, val in kwargs.items():
            match key:
                case "url":
                    #print("Url " + str(val))
                    valbool[0] = val
                case "file":
                    #print("File " + str(val))
                    valbool[1] = val
        if valbool[0] == valbool[1]:
            print("cannot do anything")
            exit()
        if valbool[0] == True:
            resp = request.urlopen(source)
            data = resp.read()
            text = data.decode("UTF-8")
            words = text.split("\n")
        else:
            if valbool[1] == True:
                with open("words.txt") as f:
                    strg = f.read()
                    words = strg.split("\n")
        
        if words:
            self.root = self.bstBuild(0,(len(words)-1),words)
            
    
    def bstBuild(self,start:int, end:int, words:list[str]) -> Node:
        if start > end:
            return None
        mid = (start + end) //2

        node = Node(words[mid])

        node.left = self.bstBuild(start, mid-1,words)
        node.right = self.bstBuild(mid+1, end, words)

        return node
    def _collect(self,node: Node,prefix: str, sgglist: list[str])-> None:
        if node is None:
            return
        self._collect(node.left,prefix,sgglist)

        if(node.word.startswith(prefix)):
            sgglist.append(node.word)

        self._collect(node.right,prefix,sgglist)
    
    def autocomplete(self, prefix)-> list[str]:
        suggestions = []
        self._collect(self.root,prefix,suggestions)
        return suggestions
        
        

        
    
    