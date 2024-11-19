# Write a function `findWord` that takes a list of letter combinaisons as input, and returns the
# word issued from the combinaisons.

# The symbol `>` acts as an arrow, meaning for "A>B" that the letter `A`
# is followed by the letter `B` within the final word.

# There is always a unique solution.

# Some test cases:

# ["P>E", "E>R", "R>U"] -> "PERU"
# ["I>N", "A>I", "P>A", "S>P"] -> "SPAIN"
# ["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"] -> "HUNGARY"
# ["I>F", "W>I", "S>W", "F>T"] -> "SWIFT"
# ["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"] -> "PORTUGAL"
# ["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"] -> "SWITZERLAND"

# amir version

from typing import List

def findWord(pairs: List[str]) -> str:
     follows = {}
     precedes = {}
     
     for pair in pairs:
         a, b = pair.split('>')
         follows[a] = b
         precedes[b] = a
         
     start = None
     for key in follows:
         if key not in precedes:
             start = key
             break
     word = [start]
     
     while start in follows:
         start = follows[start]
         word.append(start)
     
     return ''.join(word)

print(findWord(["M>A", "A>R", "R>O", "O>C", "C>"]))

# thomas version

# from collections import defaultdict
 
# def find_word(lst: List[str]) -> str:
#    # Adjacency matrix
#    adj = defaultdict()
# 
#    for pair in lst:
#        a, b = pair.split(">")
# 
#        adj[a] = b
#        adj[b] = adj.get(b)
# 
#    VALUES = list(adj.values())
#    KEYS = list(adj.keys())
# 
#    # Find last letter
#    last_idx = VALUES.index(None)
#    last = KEYS[last_idx]
# 
#    # Go back steps
#    word = last
#    for _ in range(len(lst)):
#        prev_idx = VALUES.index(last)
#        last = KEYS[prev_idx]
# 
#        word = last + word
# 
#    return word

# print(find_word(["P>E", "E>R", "R>U"]))



