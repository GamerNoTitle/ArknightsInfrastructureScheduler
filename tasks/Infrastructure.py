def EnterInfrastructure(device, recongnize, temp_dir: str):
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
    
def RoomRecongnize(device, recongnize, temp_dir: str):
    Rooms = ['贸易站', '制造站', '发电站', '宿舍', '控制中枢', '会客室', '加工站', '办公室', '训练室']
    HomeButton = ['进驻总览', 'NOTIFICTION']

def run(device, recongnize, temp_dir: str):
    EnterInfrastructure(device, recongnize, temp_dir)