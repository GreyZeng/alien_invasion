from pathlib import Path

path = Path('README.md')
# rstrip ÊÇÉ¾³ýÄ©Î²µÄ»»ÐÐ·û
content = path.read_text(encoding='UTF-8', errors='ignore').rstrip()
print(content)
