import re
with open('inputDay-5.txt', 'r') as we:
    text = we.readlines()
for i in range(0, (len(text))):
    text[i] = text[i].rstrip('\n')
# compile filters
filter1 = re.compile(r'.*[aeiou].*[aeiou].*[aeiou].*')
filter2 = re.compile(r'(.*(ab|cd|pq|xy).*)')
filter3 = re.compile(r'.*([a-z])\1.*')
# create results list
result1 = []
# append elements matching all regexes
for ele in text:
    if filter1.match(ele) is not None and filter3.match(ele) is not None and filter2.match(ele) is None:
        result1.append(ele)
# print results
print(f'Part one result: {len(result1)}')
# compile filters
filter4 = re.compile(r'.*([a-z]{2}).*\1.*')
filter5 = re.compile(r'.*([a-z])[a-z]\1.*')
# empty results list
result2 = []
# populate list
for ele in text:
    if filter4.match(ele) is not None and filter5.match(ele) is not None:
        result2.append(ele)
# print results
print(f'Part two result: {len(result2)}')
