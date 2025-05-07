# Removes leading and trailing whitespace.

Name = "  Rabnawaz Dogar   "

print(Name.strip())


# Centers string within the given width.

Text = "Hello"

print(Text.center(10 , "-"))


# Left-aligns string within the given width.
print(Text.ljust(10,"-"))

# Right-aligns string within the given width.

print(Text.rjust(10,"-"))



# Pads the string with zeros.
# zfill(width)	Pads the string with zeros.	"42".zfill(5) → "00042"

number = "42"

print(number.zfill(10))

