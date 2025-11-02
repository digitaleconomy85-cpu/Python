# 1. capitalize()
print("hello world".capitalize())  # Output: Hello world

# 2. casefold()
print("HELLO".casefold())  # Output: hello

# 3. center()
print("Hi".center(10, "-"))  # Output: ----Hi----

# 4. count()
print("banana".count("a"))  # Output: 3

# 5. encode()
print("Hello".encode())  # Output: b'Hello'  (bytes ko‘rinishda)

# 6. endswith()
print("python".endswith("on"))  # Output: True

# 7. expandtabs()
print("H\te\tl\tl\to".expandtabs(2))  # Output: H e l l o

# 8. find()
print("Welcome".find("l"))  # Output: 2 (birinchi topilgan “l” indeksi)

# 9. format()
print("My name is {}".format("Ali"))  # Output: My name is Ali

# 10. format_map()
person = {"name": "Ali", "age": 20}
print("My name is {name}, age {age}".format_map(person))  # Output: My name is Ali, age 20

# 11. index()
print("Hello".index("e"))  # Output: 1

# 12. isalnum()
print("Python3".isalnum())  # Output: True (faqat harf va raqamlar bor)

# 13. isalpha()
print("Python".isalpha())  # Output: True (faqat harflar)

# 14. isascii()
print("Hello!".isascii())  # Output: True (ASCII belgilar)

# 15. isdecimal()
print("1234".isdecimal())  # Output: True (raqamlar)

# 16. isdigit()
print("²".isdigit())  # Output: True (raqam belgisi sifatida)

# 17. isidentifier()
print("my_var".isidentifier())  # Output: True (Python identifikatoriga mos)

# 18. islower()
print("hello".islower())  # Output: True

# 19. isnumeric()
print("½".isnumeric())  # Output: True (son ifodalaydi)

# 20. isprintable()
print("Hello".isprintable())  # Output: True (chop etilishi mumkin bo‘lgan belgilar)

# 21. isspace()
print("   ".isspace())  # Output: True (faqat bo‘sh joylar)

# 22. istitle()
print("Hello World".istitle())  # Output: True (har so‘z bosh harf bilan)

# 23. isupper()
print("HELLO".isupper())  # Output: True

# 24. join()
print("-".join(["2025", "11", "02"]))  # Output: 2025-11-02

# 25. ljust()
print("Hi".ljust(6, "*"))  # Output: Hi****

# 26. lower()
print("PYTHON".lower())  # Output: python

# 27. lstrip()
print("   Hello".lstrip())  # Output: Hello

# 28. maketrans() + translate()
table = str.maketrans("ae", "12")
print("apple".translate(table))  # Output: 1ppl2

# 29. partition()
print("I love Python".partition("love"))  # Output: ('I ', 'love', ' Python')

# 30. replace()
print("I love Python".replace("Python", "Data"))  # Output: I love Data

# 31. rfind()
print("banana".rfind("a"))  # Output: 5 (oxirgi “a” indeksi)

# 32. rindex()
print("banana".rindex("a"))  # Output: 5

# 33. rjust()
print("Hi".rjust(6, "*"))  # Output: ****Hi

# 34. rpartition()
print("I love Python".rpartition("love"))  # Output: ('I ', 'love', ' Python')

# 35. rsplit()
print("apple,banana,grape".rsplit(",", 1))  # Output: ['apple,banana', 'grape']

# 36. rstrip()
print("Hello   ".rstrip())  # Output: Hello

# 37. split()
print("apple,banana,grape".split(","))  # Output: ['apple', 'banana', 'grape']

# 38. splitlines()
print("Hello\nWorld\n!".splitlines())  # Output: ['Hello', 'World', '!']

# 39. startswith()
print("Python".startswith("Py"))  # Output: True

# 40. strip()
print("  Hello  ".strip())  # Output: Hello

# 41. swapcase()
print("Hello World".swapcase())  # Output: hELLO wORLD

# 42. title()
print("hello world".title())  # Output: Hello World

# 43. upper()
print("python".upper())  # Output: PYTHON

# 44. zfill()
print("42".zfill(5))  # Output: 00042
