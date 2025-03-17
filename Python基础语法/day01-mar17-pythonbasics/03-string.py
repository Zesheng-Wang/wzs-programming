course = "Python for Beginners"
course[0]  # returns the first character
course[1]  # returns the second character
course[-1]  # returns the first character from the end
course[-2]  # returns the second character from the end
message = """

醉后不知天在水
满船清梦压星河

"""
print(len(course))
name = "Zesheng"
message = f"Hi, my name is {name}"

message.upper()  # to convert to uppercase
message.lower()  # to convert to lowercase
message.title()  # to capitalize the first letter of every word
message.find("p")  # returns the index of the first occurrence of p (or -1 if not found)
message.replace("p", "q")

# \ 转义字符
