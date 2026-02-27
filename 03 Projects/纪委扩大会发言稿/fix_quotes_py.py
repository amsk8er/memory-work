#!/usr/bin/env python3
"""Fix quotes in gen_docx.py - replace straight quotes inside Chinese text with Chinese quotes."""
import re

with open('/Users/zzd/projects/memory-work/03 Projects/纪委扩大会发言稿/gen_docx.py', 'r') as f:
    text = f.read()

# Fix the garbled text
text = text.replace('也\ufffd\ufffd我们', '也是我们')

# We need to only replace quotes inside add_body() and add_heading_text() string arguments
# Strategy: find Chinese text strings and replace straight quotes within them

lines = text.split('\n')
new_lines = []
for line in lines:
    # Only process lines that contain add_body or add_heading_text calls with Chinese content
    if ("add_body(" in line or "add_heading_text(" in line) and "\\u" not in line:
        # Find the string content between the outer quotes
        # These lines use single quotes: add_body('...')
        m = re.match(r"^(add_body\(')(.*)('\))$", line.strip())
        if m:
            prefix, content, suffix = m.groups()
            # Replace paired straight double quotes in content with Chinese quotes
            result = []
            in_q = False
            for ch in content:
                if ch == '"':
                    if not in_q:
                        result.append('\u201c')
                        in_q = True
                    else:
                        result.append('\u201d')
                        in_q = False
                else:
                    result.append(ch)
            content = ''.join(result)
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(f"{indent}{prefix}{content}{suffix}")
            continue
    new_lines.append(line)

text = '\n'.join(new_lines)

with open('/Users/zzd/projects/memory-work/03 Projects/纪委扩大会发言稿/gen_docx.py', 'w') as f:
    f.write(text)

print('Done')
