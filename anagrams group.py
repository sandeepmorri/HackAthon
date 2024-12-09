 from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort each word and use the sorted word as a key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = group_anagrams(strs)
print(grouped_anagrams)