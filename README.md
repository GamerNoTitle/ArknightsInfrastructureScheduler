# ArknightsInfrastructureScheduler

## 明日方舟排班换班助手

为啥要做这个？因为群友的鞭策 ![](https://valinecdn.bili33.top/QQ/wunai.gif)

![](https://gamernotitle.coding.net/p/assets/d/assets/git/raw/master/img/%23Miscellaneous/TIM-20220507-230435.png?download=true)

## 快速开始

### 环境要求

- Python 3.6 - 3.9（不支持 3.10，因为 Ocr 库没有 3.10 的版本，以后如果有的话再适配）
- NVIDIA CUDA（如果你要用 GPU 进行识别的话就要装，反正我是没配置好，而且虚拟机里面测试的时候 GPU 虚拟化没搞定）【CUDA 11.2：https://developer.download.nvidia.com/compute/cuda/11.2.1/local_installers/cuda_11.2.1_461.09_win10.exe | https://developer.nvidia.com/cuda-11.2.1-download-archive】

### 安装依赖

在本项目中，依赖并不是直接使用`pip install -r requirements.txt`就能完成的，取而代之的是你需要运行`requirements.py`文件，这个文件的运行方式如下，各参数将会在下面进行说明

- Windows

```bash
python requirements.py [-h] [-g | -c] [--cuda {11.2,11.1,11.0,10.2,10.1}] [-e EXECUTE]
```

- Linux

```bash
python3 requirements.py [-h] [-g | -c] [--cuda {11.2,11.1,11.0,10.2,10.1}] [-e EXECUTE]
```

> -h 显示帮助信息
>
> -g 使用 GPU 进行识别（不能与-c 连用，且用了-g 后一定要用--cuda 指定 CUDA 版本，且要提前配置要 CUDA 并加入 PATH）
>
> -c 使用 CPU 进行识别（不能与-g 连用）
>
> --cuda 指定 CUDA 版本，只有使用 GPU 进行识别时有效
>
> -e 指定 python 可执行文件的路径（因为我自己电脑是 3.10，后来装了个 3.9，所以就加了这个参数用来指定 python3.9 运行）
>
> -i 指定 Pip Index，可以用于替换官方源来加快依赖的安装速度，默认用清华源

#### 实例

- 使用 CPU 进行识别

```bash
python requirements.py -c
```

- 使用 GPU 进行识别，并且安装 CUDA11.2

```bash
python requirements.py -g --cuda 11.2
```

- 使用 GPU 进行识别，并且安装 CUDA11.0，使用特定路径下的 python3.9

```bash
python requirements.py -g --cuda 11.0 -e "C:\Users\GamerNoTitle\AppData\Local\Programs\Python\Python39\python.exe"
```

安装完成依赖后，你可以运行`./utils/Ocr.py`来测试 Ocr 识别结果

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

安装 VS C++ Build Tools，因为这个安装比较麻烦，所以建议直接下载我这个

```
链接：https://pan.baidu.com/s/1g5SEmiv2IQuZP5b5OJcjIw?pwd=ztyo
提取码：ztyo
```

装载镜像后直接安装就好了。

## Credit

- PaddleOcr https://paddlepaddle.org.cn
