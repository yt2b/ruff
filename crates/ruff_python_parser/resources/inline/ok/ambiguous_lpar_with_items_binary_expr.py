# It doesn't matter what's inside the parentheses, these tests need to make sure
# all binary expressions parses correctly.
with (a) and b: ...
with (a) is not b: ...
# Make sure precedence works
with (a) or b and c: ...
with (a) and b or c: ...
with (a | b) << c | d: ...
# Postfix should still be parsed first
with (a)[0] + b * c: ...
