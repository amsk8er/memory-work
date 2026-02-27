#!/usr/bin/env python3
"""Replace straight quotes with Chinese quotes in the speech draft."""
import re

with open('/Users/zzd/projects/memory-work/03 Projects/纪委扩大会发言稿/发言稿.md', 'r') as f:
    text = f.read()

# Replace paired straight double quotes with Chinese double quotes
result = []
in_quote = False
for ch in text:
    if ch == '"':
        if not in_quote:
            result.append('\u201c')  # left "
            in_quote = True
        else:
            result.append('\u201d')  # right "
            in_quote = False
    else:
        result.append(ch)
text = ''.join(result)

with open('/Users/zzd/projects/memory-work/03 Projects/纪委扩大会发言稿/发言稿.md', 'w') as f:
    f.write(text)

print('Done')
