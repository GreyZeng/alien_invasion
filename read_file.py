from pathlib import Path

path = Path('README.md')
# rstrip ��ɾ��ĩβ�Ļ��з�
content = path.read_text(encoding='UTF-8', errors='ignore').rstrip()
print(content)
