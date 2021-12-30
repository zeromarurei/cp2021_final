# ref: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
# ref: https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
with open("1a_grouping.txt", encoding="utf-8") as f:
    data = f.read().splitlines()
data = list(filter(None, data))
#print(data)
for i in data:
    print(i)
'''
['1a grouping', '1ag1', '41023146', '41023143', '41023147', '41023113', '41023116', '41023111', '41023145', '1ag2', '41023104', '41023103', '41023105', '41023106', '41023107', '41023109', '1ag3', '41023125', '41023119', '41023120', '41023124', '41023118', '41023122', '41023130', '1ag4', '40923129', '41023135', '41023150', '41023151', '41023152', '40923115', '41023132', 'lag5', '41023114', '41023126', '41023101', '41023110', '41023108', '40823214', 'lag6', '41023121', '41023140', '41023133', '41023112', '41023153', '41023134', '41023138', '40832244', 'lag7', '41023142', '41023137', '41023129', '41023131', '41023127', '41023141', '40823227', '41023154']

'''