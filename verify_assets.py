import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'(?:src|href)="([^":#]+)"', html)
print('Total local asset references:', len(matches))
missing = []
for m in sorted(set(matches)):
    # ignore anchor or empty
    if not m or m.startswith('#') or m.startswith('mailto:') or m.startswith('http'):
        continue
    if not os.path.exists(m):
        missing.append(m)
    else:
        print(f'[OK] {m} ({os.path.getsize(m)} bytes)')

if missing:
    print('MISSING ASSETS:', missing)
else:
    print('>>> ALL ASSETS EXIST AND VERIFIED SUCCESSFULLY! <<<')
