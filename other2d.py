shoe_rack = []

shoe_rack.append(['trainers','sandals'])
shoe_rack.append(['brown shoes', 'sneakers'])
shoe_rack.append(['red pumps', 'soccer shoes'])

shoe_rack = shoe_rack[0:1] + shoe_rack[-1]
print(shoe_rack)

shoe_rack = [['brown shoes', 'sneakers', 'black high heels'],['blue converse','sandals','ballet shoes'],['red pumps','soccer shoes','red high heels']]

shoe_rack.sort()
print(shoe_rack)

shoe_rack.reverse()
print(shoe_rack)