import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()_+[]"

all_chars = lower + upper + number + symbols
length = int(input("Enter a length:"))

password = ".join(random.sample(all_chars, length))"
print("Generate Password:", password)