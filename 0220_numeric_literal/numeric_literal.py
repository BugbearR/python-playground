# https://docs.python.org/ja/3/reference/lexical_analysis.html#numeric-literals

# integer
# bininteger
print(0b10) # 2
print(0b10_10)
# octinteger
print(0o10) # 8
print(0o10_10)
print(0o12345670)
print(0o1234_5670)
# decinteger
print(10) # 10
print(10_10)
# hexinteger
print(0x10) # 16
print(0x123456789abcdef0)
print(0x123456789ABCDEF0)
print(0x1234_5678_9ABC_DEF0)

# float
# pointfloat
print(.1) # 0.1
print(3.14)
print(1.)
print(1.0)
# exponentfloat
print(.1e10)
print(.1e+10)
print(.1e-10)
print(1e10)
print(1e+10)
print(1e-10)
print(1.e10)
print(1.e+10)
print(1.e-10)
print(1.1e10)
print(1.1e+10)
print(1.1e-10)

# complex
print(1j)
print(1.1j)
print(1e10j)
print(1J)
print(1.1J)
print(1e10J)
