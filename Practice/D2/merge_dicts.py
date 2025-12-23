d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 7}

d3 = {}

for key in d1:
    d3[key] = d1[key]


for key in d2:
    if key in d3:
        d3[key] += d2[key]
    else:
        d3[key] = d2[key]

print(d3)
