import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'src=\"data:[^\"]+\"', 'src=\"images/logo 2.jpeg\"', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
