from ast import In


def Infrastructure(device, recongnize: function, temp_dir: str):
    # 进入基建
    InInfrastructure = False
    while not InInfrastructure:
        pic = device.screencapture(temp_dir)
        result = recongnize(pic)
        for i in result:
            InInfrastructure = True
            if i[1][0] == '基建': device.touch(i)
            break
        else:
            if i == result[-1]:
                print('无法找到点击目标：基建，重新截取并识别中……')
                InInfrastructure = False
    