# Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).

# Sequence types (list, tuple, string, range) support slicing.
# Therefore, you can sort in reverse order by setting text[::-1] in the slice operation.
text = "stressed"
print(text[::-1])

# You can also use reversed() method.
print(''.join(reversed(text)))