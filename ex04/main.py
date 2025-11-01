from BST import BST 
import Node

def main():
    mybst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", url=True, file = False)
    
    #print(mybst.source)
    print(mybst.autocomplete("tr"))
main()