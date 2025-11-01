"""
Store words in a BST and return suggestions for a prefix that you type in.

(1) Define the Node class, which represents each node in the BST. Each node contains
a word and pointers to the left and right children.

(2) Define the BST class, which contains methods to insert words and to find all words
that start with a given prefix.
"""
import os
import sys
from BST import BST

def read_dictionary(filename: str) -> list[str]:
    """Reads a dictionary file and returns a list of words.

    Args:
        filename (str): The name of the file containing the dictionary.
    Returns:
        list[str]: A list of words from the dictionary.
    """
    pass



def get_char():
#     """Read one character from stdin without pressing Enter."""
     try:
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
     except ImportError:
#         # Windows fallback
         import msvcrt
         return msvcrt.getch().decode("utf-8")

if __name__ == "__main__":
    """create a loop that asks the user to input a prefix and prints out the suggestions after each character,
    until the user types 'exit' to quit the program.
    """
    print("Start typing (press ESC to quit):")
    prefix = ""
    bst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", url=True, file = False)
    while True:
        ch = get_char()

         # Exit on ESC
        if ord(ch) == 27:
           print("\nExiting...")
           break

    #     # Backspace (delete last char)
        if ch in ("\b", "\x7f"):  # \x7f for Linux/mac
            prefix = prefix[:-1]
        elif ch == "\r":  # ignore Enter key
            continue
        else:
            prefix += ch.lower()

    #     # Clear screen for neat output
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Current input >> {prefix}")
        suggestions = bst.autocomplete(prefix)
        if suggestions:
            for s in suggestions[:5]:  # show only first 5 suggestions
                print(s)
        else:
            print("No matches found.")
    pass