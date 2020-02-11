from collections import deque

"""
Given a trie, a look and the look's name (or tags), insert the look in the
trie.
"""
def insert_look_in_trie(trie, name, look):
    for subname in name.split(" "):
        current_dict = trie
        for letter in subname:
            if letter not in current_dict:
                current_dict = current_dict.setdefault(letter, {})
            else:
                current_dict = current_dict[letter]
        current_dict[subname] = look


"""Given a trie, return all the "leaves" for that trie."""
def get_all_leaves_for_trie(trie):
    leaves = set()
    q = deque()
    q.append(trie)

    while not len(q) == 0:
        current = q.popleft()
        for key, value in current.items():
            # if the value is a dict, add it to the deque, otherwise it's
            # a leaf.
            if isinstance(value, dict):
                q.append(value)
            if isinstance(value, str):
                leaves.add(value)
    return leaves

"""
Perform a lookup in the trie for the partial name we have and return all the
looks."""
def get_all_looks_for_partial_name(trie, name):
    current_dict = trie
    for letter in name:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return get_all_leaves_for_trie(current_dict)
