import time

def EnterInfrastructure(device, recongnize, temp_dir: str, logger):
    # 进入基建
    InInfrastructure = False
    while not InInfrastructure:
        pic = device.screencapture(temp_dir)
        result = recongnize(pic, logger)
        for i in result:
            if i[1][0] == '基建': 
                logger.info(f'已经找到基建的位置 {i[0]}, 正在进入……')
                device.touch(i)
                logger.info(f'已发送基建按钮点击指令！')
                InInfrastructure = True
                break
            else:
                if i == result[-1]:
                    logger.warning('无法找到点击目标：基建，重新截取并识别中……')
                    InInfrastructure = False
    
def RoomRecongnize(device, recongnize, temp_dir: str, logger):
    Rooms = ['贸易站', '制造站', '发电站', '宿舍', '控制中枢', '会客室', '加工站', '办公室', '训练室']
    ButtonPressOrder = ['NOTIFICATION', ['订单交付', '']]

def ClearNotificationAward(device, recongnize, temp_dir: str, logger):
    pic = device.screencapture(temp_dir)
    result = recongnize(pic, logger)
    Notification_found = False
    while not Notification_found:   # 点击基建通知按钮
        logger.info('正在尝试找到基建通知按钮位置……')
        for i in result:
            if i[1][0] == 'NOTIFICATION':
                logger.info(f'已经找到基建通知位置 {i[0]}，正在发送点击指令……')
                device.touch(i)
                Notification_found = True
            else:
                pass

def TradeAwardGet(device, recongnize, temp_dir: str, logger):
    pic = device.screencapture(temp_dir)
    result = recongnize(pic, logger)


def run(device, recongnize, temp_dir: str, logger):
    EnterInfrastructure(device, recongnize, temp_dir, logger)
    time.sleep(10)
    ClearNotificationAward(device, recongnize, temp_dir, logger)