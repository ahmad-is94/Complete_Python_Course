# simple example to show the use of regular expression

# importing the re module
import re

# given string
str_1 ="RegEx, is a sequence of unique characters that forms a search pattern."

# searching for specified pattern in given string
matched_str = re.search(r'unique', str_1)  # using the search() method

# printing the starting and ending index
print('Beginning Index:', matched_str.start())
print('Ending Index:', matched_str.end())


#Methods


# import re
#
# # given string
# str_1 = 'I have been working as a Web Developer since 2023.'
# regex_pattern = r"([a-zA-Z]+) (\d+)"
#
# # searching for specified pattern in given string
# matched_str = re.search(regex_pattern, str_1)  # using the search() method
#
# # checking the returned object
# if matched_str:
#     # printing the matched pattern details
#     print('Match Found:', matched_str.group())
#     print('Beginning Index:', matched_str.start())
#     print('Ending Index:', matched_str.end())
# else:
#     print('Match Not Found')


#method 2
import re

# given string
str_1 = """My house no. is 4567 and 
          my office no. is 8910."""

regex_pattern = r"([a-zA-Z]+) (\d+)"
# searching all occurrences in the given string
matched_str_list = re.findall(regex_pattern, str_1)
# checking the returned object
if matched_str_list:
    print(matched_str_list)
else:
    print("No match found")



#re
# importing the re module
import re

# given string
str_1 = "Welcome to Tpoint Tech."

# using compile() function
regex_pattern = re.compile('[a-e]')

# searching all occurrences in the given string
matched_str_list = re.findall(regex_pattern, str_1)

if matched_str_list:
    print(matched_str_list)
else:
    print("No match found")
