# DemoRE.py
#정규표현식

import re
result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())