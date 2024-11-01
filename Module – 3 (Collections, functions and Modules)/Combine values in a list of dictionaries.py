from collections import Counter

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined_data = Counter()
for d in data:
    combined_data[d['item']] += d['amount']
print("Combined values:", combined_data)
