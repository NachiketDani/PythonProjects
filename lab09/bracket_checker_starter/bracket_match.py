from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # TODO: Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py
    def __init__(self):
        """
        Class for checking bracket closures
        """
        self.stack_of_brackets = Stack()
        self.bracket_pair_dict = {")": "(", "}": "{", "]": "["}
        self.match = False

    def brackets_match(self, line):
        """
        Loop through characters,
        Compare to keys/values in bracket pair dictionary
        Add to stack object if its an opening bracket
        Pop from stack object if its a closing bracket
        Return True/False for self.match object
        """
        for char in line:
            if char in self.bracket_pair_dict.values():
                # Char is a opening bracket
                self.stack_of_brackets.push(char)
                print(char)
            elif char in self.bracket_pair_dict.keys():
                # Char is a closing bracket
                if self.stack_of_brackets.peek() is not None:
                    if (self.stack_of_brackets.peek()
                            == self.bracket_pair_dict[char]):
                        self.stack_of_brackets.pop()
                    else:
                        return self.match
                else:
                    return self.match
        # Check if stack is empty after looping through all characters
        if self.stack_of_brackets.peek() is None:
            self.match = True
            return self.match
        else:
            return self.match