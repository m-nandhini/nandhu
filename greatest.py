count = {}
for s in check_string:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1
for key in count:
  if count[key] > 1:
    print key, count[key]
