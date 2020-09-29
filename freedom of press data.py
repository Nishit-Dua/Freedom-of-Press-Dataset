import re
import pandas as pd

f = open('./Source Data (wiki).txt', 'r')
f2 = open('./intermidiate.txt', 'w')

data = f.read()
data = data.replace('| ', '')
data = data.split('|-')
data = ''.join(data).replace('\n{', '{')


f2.write(data)


patern = re.compile(
    r'(<br>)(−?\d+\.?\d+)|(flagcountry\|(\w+\s?\w+)|(\{\{n/a\}\}))')
matches = patern.finditer(data)


cleanCsv = open('./CleanData.csv', 'w')
# cleanJSON = open('./CleanData.json', 'w')

cleanCsv.write('Country, ')

for year in range(2020, 2001, -1):
    if year == 2011:
        # no Data for 2011
        continue
    elif year == 2002:
        cleanCsv.write(f'{year}')
    else:
        cleanCsv.write(f'{year}, ')

for match in matches:
    groups = match.groups()
    print(groups)
    if groups[3]:
        cleanCsv.write(f'\n{groups[3]}')
    elif groups[1]:
        cleanCsv.write(f', {groups[1]}')
    elif groups[-1]:
        cleanCsv.write(', null')

df = pd.read_csv('./CleanData.csv')

df.transpose().to_json('./CleanData.json')

f.close()
f2.close()
cleanCsv.close()
# cleanJSON.close()
