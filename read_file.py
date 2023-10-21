# coding=UTF-8
from pathlib import Path

# 在显示文件路径时，Windows 系统使用反斜杠(\) 而不是 斜杆(/) 但是在代码中应该
# 始终使用斜杠，即便在 Windows 中也应该如此。pathlib会自动使用正确的路径表达
path = Path('C:/workspace/hello-python/README.md')
# path = Path('README.md')
# rstrip 是删除末尾的换行符
content = path.read_text(encoding='UTF-8', errors='ignore').rstrip()
print(content)
