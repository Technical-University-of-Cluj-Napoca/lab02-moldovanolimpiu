from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] +=1
        key = tuple(count)
        anagrams_dict[key].append(s)
    return anagrams_dict.values()

def main():
    inpstr = input("introduce strings:")
    splitstr = inpstr.split(" ")
    anagram = group_anagrams(splitstr)
    print(anagram)


main()