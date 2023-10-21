from pathlib import Path

path = Path('README.md')
content = path.read_text(encoding='UTF-8', errors='ignore')
print(content)
