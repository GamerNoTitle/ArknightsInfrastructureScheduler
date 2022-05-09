# ArknightsInfrastructureScheduler

## 明日方舟排班换班助手

为啥要做这个？因为群友的鞭策 ![](https://valinecdn.bili33.top/QQ/wunai.gif)

![](https://gamernotitle.coding.net/p/assets/d/assets/git/raw/master/img/%23Miscellaneous/TIM-20220507-230435.png?download=true)

## Q&A

### 安装依赖时出错

```
  Running setup.py install for python-Levenshtein ... error
  error: subprocess-exited-with-error

  × Running setup.py install for python-Levenshtein did not run successfully.
  │ exit code: 1
  ╰─> [28 lines of output]
      running install
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-3.9
      creating build\lib.win-amd64-3.9\Levenshtein
      copying Levenshtein\StringMatcher.py -> build\lib.win-amd64-3.9\Levenshtein
      copying Levenshtein\__init__.py -> build\lib.win-amd64-3.9\Levenshtein
      running egg_info
      writing python_Levenshtein.egg-info\PKG-INFO
      writing dependency_links to python_Levenshtein.egg-info\dependency_links.txt
      writing entry points to python_Levenshtein.egg-info\entry_points.txt
      writing namespace_packages to python_Levenshtein.egg-info\namespace_packages.txt
      writing requirements to python_Levenshtein.egg-info\requires.txt
      writing top-level names to python_Levenshtein.egg-info\top_level.txt
      reading manifest file 'python_Levenshtein.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no previously-included files matching '*pyc' found anywhere in distribution
      warning: no previously-included files matching '*so' found anywhere in distribution
      warning: no previously-included files matching '.project' found anywhere in distribution
      warning: no previously-included files matching '.pydevproject' found anywhere in distribution
      adding license file 'COPYING'
      writing manifest file 'python_Levenshtein.egg-info\SOURCES.txt'
      copying Levenshtein\_levenshtein.c -> build\lib.win-amd64-3.9\Levenshtein
      copying Levenshtein\_levenshtein.h -> build\lib.win-amd64-3.9\Levenshtein
      running build_ext
      building 'Levenshtein._levenshtein' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> python-Levenshtein

note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.
```

安装VS C++ Build Tools，因为这个安装比较麻烦，所以建议直接下载我这个
```
链接：https://pan.baidu.com/s/1g5SEmiv2IQuZP5b5OJcjIw?pwd=ztyo 
提取码：ztyo
```
装载镜像后直接安装就好了。