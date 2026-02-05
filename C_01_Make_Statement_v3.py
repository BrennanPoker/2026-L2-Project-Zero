# Functions go here
def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasized text / mini-headings (1 line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

# Main Routine goes here
make_statement(statement= "Cats are Cool!", decoration="=", lines= 3)
print()
make_statement(statement= "Super Cool!", decoration="*", lines= 2)
print()
make_statement(statement= "I like cats!", decoration="🐈")