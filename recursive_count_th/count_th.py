'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    if len(word) <= 2:
        return int(word[-2:] == "th")
    
    return (word[:2] == "th") + count_th(word[1:])