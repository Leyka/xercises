"""
String compression
Ex. "a" => a, "aabb" => a2b2, "aabcc" => a2b1c2
"""

def compress(string: str) -> str:
    if len(string) == 1:
        return string

    count = 1
    out = ""
    
    for i, char in enumerate(string):
        next_char = string[i+1] if i != (len(string) - 1) else ""
        if char == next_char:
            count += 1
        else:
            out += "{}{}".format(char, count)
            count = 1

    return out
        
assert(compress("a") == "a")
assert(compress("aaa") == "a3")
assert(compress("aaabccc") == "a3b1c3")
assert(compress("aaaxaabbb") == "a3x1a2b3")