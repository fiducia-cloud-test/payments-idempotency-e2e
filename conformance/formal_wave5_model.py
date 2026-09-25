seen = set()
charges = 0
for key in ('pay-1', 'pay-1', 'pay-1', 'pay-1'):
    if key not in seen:
        seen.add(key)
        charges += 1
assert charges == 1

seen.clear(); charges = 0
for key in ('pay-1', 'pay-2', 'pay-1', 'pay-2'):
    if key not in seen:
        seen.add(key); charges += 1
assert charges == 2
print('formal_wave5_model: ok')
