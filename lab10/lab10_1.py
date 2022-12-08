import re
line = " Yesterday is 2021-1-12, Today is 2021-1-13, Tomorrow is 2021-1-14"
pattern = r"([1-2][0-9][0-9][0-9])-(\d*\d)-(\d*\d)" 
result = re.findall(pattern, line)
print (result)
