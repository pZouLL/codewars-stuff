'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
'''


def number(lines):
    new_lines = []
    linescount = 1
    index = 0 
    if len(lines) == 0:
        return []
    else:
        for x in lines:
            new_lines.append(f"{linescount}: {x}")
            linescount += 1
    return new_lines