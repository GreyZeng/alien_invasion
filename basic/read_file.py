# coding=UTF-8
from pathlib import Path

# 在显示文件路径时，Windows 系统使用反斜杠(\) 而不是 斜杆(/) 但是在代码中应该
# 始终使用斜杠，即便在 Windows 中也应该如此。pathlib会自动使用正确的路径表达
path = Path('/README.md')
# path = Path('README.md')
# rstrip 是删除末尾的换行符
content = path.read_text(encoding='UTF-8', errors='ignore').rstrip()
print(content)

# 写文件
# path2 = Path('tmp.file')
# path2.write_text(path.read_text(encoding='UTF-8', errors='ignore').rstrip())