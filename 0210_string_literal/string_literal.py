# https://docs.python.org/ja/3/reference/lexical_analysis.html#string-and-bytes-literals
# String literals are written in a variety of ways:

# single line string
# Double quotes: "allows embedded 'single' quotes"
print("allows embedded 'single' quotes")
# Single quotes: 'allows embedded "double" quotes'
print('allows embedded "double" quotes')
# long string
# Triple quoted: '''Three single quotes''', """Three double quotes"""
# Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.
# String literals inside triple quotes, can be split over several lines.
print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
allows embedded "double" quotes''')
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
allows embedded 'single' quotes""")
