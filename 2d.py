shoe_rack = []

shoe_rack.append(['trainers','sandals'])
shoe_rack.append(['brown shoes', 'sneakers'])
shoe_rack.append(['red pumps', 'soccer shoes'])
print(shoe_rack)

print(len(shoe_rack))

row = shoe_rack[0]
print(len(row))

shoe_rack.insert(1, ['ballet shoes', 'red high heels'])
print(shoe_rack)

shoe_rack = shoe_rack[0:2]
print(shoe_rack)

shoe_rack = shoe_rack[-1]
print(shoe_rack)

shoe_rack = shoe_rack[:2]
shoe_rack = shoe_rack[0:]
print(shoe_rack)

shoe_rack.pop(2)
print(shoe_rack)

shoe_rack.remove(['ballet shoes', 'red high heels'])
print(shoe_rack)
