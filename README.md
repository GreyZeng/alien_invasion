# Python解压版安装方法

解压缩zip file文件后，

把python.exe文件的路径配置在环境变量里

2.2 配置pip安装

2.2.1 修改pythonXX._pth文件

修改`pythonXX._pth`文件，去掉`#import site` 前的`#`号，即放开 import site；若不放开pip将会无法正确安装。

2.2.2 下载get-pip.py文件

从https://bootstrap.pypa.io/get-pip.py 下载get-pip.py，放到python的安装目录下，记住不用用360浏览器，它只是打开文件而不是下载，可以用火狐或谷歌浏览器打开下载

2.2.3 安装pip

执行

```python
python get-pip.py
```

注意：必须在放置该文件的文件夹下执行该命令

指定国内源下载
```python
python get-pip.py -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

将`C:\Python\Scripts`加入环境变量

验证

```python
pip install numpy
```


指定国内下载源

```python
pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```