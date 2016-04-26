
my_dict = {"alan": 22, "bill": 33}

from collections import defaultdict

my_dict = defaultdict(lambda: 0)

my_dict['eric'] = 33

print my_dict['eric']


