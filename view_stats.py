import re
with open('src/pages/index.astro', 'r') as f:
    html = f.read()

pattern = r'  <!-- Stats Section \(4 Metric Cards\) -->.*?  </section>'
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    print(match.group(0))
