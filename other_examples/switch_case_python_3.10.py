"""
Python 3.10 is adding a new feature called Structural Pattern Matching

Syntax

    match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
"""

status_code = int(input())
match status_code:
    case 400:
        print("bad request")
    case 200:
        print("good")
    case _:
        print("Something else bad")

# Combining Literals

status_code = int(input())
match status_code:
    case 400 | 401 | 403:
        print("bad request")
    case 200:
        print("good")
    case _:
        print("Something else bad")
