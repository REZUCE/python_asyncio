import functools
from typing import Dict


def map_frequency(text: str) -> Dict[str, int]: # B
    words = text.split(' ') # Result List
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else: # add in dict word, key = word
            frequencies[word] = 1
    return frequencies # Dict[str, int]


def merge_dictionaries(first: Dict[str, int], # E
                       second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


lines = ["I know what I know",
         "I know that I know",
         "I don't know much",
         "They don't know much"]

mapped_results = [map_frequency(line) for line in lines] # A - list(mapped_results(Dict[str, int]))

print('Mapped results:')
for result in mapped_results: # C - print result dict in mapped_results
    print(result) 

print('Reduce result:')
print(functools.reduce(merge_dictionaries, mapped_results)) # D - first arg=func executor, second arg=iter collectionz
# first arg in merge_dictionaries first elem in mapped_results, second arg in merge_dictionaries second elem in mapped_results, new itiration first arg in merge_dictionaries result first and second in mapped_results.

