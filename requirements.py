import sys
import os
import argparse

parser = argparse.ArgumentParser(
    description='Help you install the environment that this project needs.')
mode_group = parser.add_mutually_exclusive_group()
mode_group.add_argument('-g', '--gpu', help='GPU Mode', action="store_true")
mode_group.add_argument('-c', '--cpu', help='CPU Mode', action="store_true")
parser.add_argument('--cuda', help='Specify CUDA version',
                    type=float, choices=[11.2, 11.1, 11.0, 10.2, 10.1])
parser.add_argument('-e', '--execute',
                    help='Specify executable python program path', type=str)
parser.add_argument('-i', '--index', help='Python index',
                    type=str, default='https://pypi.tuna.tsinghua.edu.cn/simple')
parser.parse_args()

ver_major = sys.version_info.major
ver_minor = sys.version_info.minor

CUDA_Version = {
    11.2: '2.2.2.post112',
    11.1: '2.2.2.post111',
    11.0: '2.2.2.post110',
    10.2: '2.2.2',
    10.1: '2.2.2.post101'
}

args = parser.parse_args()

platform = 'windows' if sys.platform == 'win32' else 'linux'
python = 'python' if sys.platform == 'win32' else 'python3'

# Check Arguments
if ver_major != 3 or ver_minor not in [6, 7, 8, 9]:
    raise RuntimeError(
        f'Please use Python 3.6/3.7/3.8/3.9! Current version: {ver_major}.{ver_minor}')
if not args.gpu and not args.cpu:
    raise RuntimeError('You must specify a mode between GPU(-g) and CPU(-g)!')
if args.cuda == None and args.gpu:
    raise RuntimeError(
        'You must specify a CUDA version (11.2/11.1/11.0/10.2/10.1) when using GPU mode!')

# Install wheel: paddlepaddle
if sys.platform == 'win32':
    if args.execute:
        if args.gpu and args.cuda:
            os.system(
                f'{args.execute} -m pip install paddlepaddle-gpu=={CUDA_Version[args.cuda]} -f https://www.paddlepaddle.org.cn/whl/{platform}/mkl/avx/stable.html')
        elif args.cpu:
            os.system(
                f'{args.execute} -m pip install paddlepaddle==2.2.2 -f https://www.paddlepaddle.org.cn/whl/{platform}/mkl/avx/stable.html')
    else:
        if args.gpu and args.cuda:
            os.system(
                f'{python} -m pip install paddlepaddle-gpu=={CUDA_Version[args.cuda]} -f https://www.paddlepaddle.org.cn/whl/{platform}/mkl/avx/stable.html')
        elif args.cpu:
            os.system(
                f'{python} -m pip install paddlepaddle==2.2.2 -f https://www.paddlepaddle.org.cn/whl/{platform}/mkl/avx/stable.html')

# Install Other Wheels
if sys.platform == 'win32':
    if args.execute:
        os.system(f'{args.execute} -m pip install -r requirements.txt')
    else:
        os.system(f'{python} -m pip install -r requirements.txt')
if args.gpu:
    print('Installation completed! After this installation, you still need to install cuda from NVIDIA website: https://developer.nvidia.com/cuda-downloads')
else:
    print('Installation completed!')
