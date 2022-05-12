from paddleocr import PaddleOCR, draw_ocr
from pprint import pformat

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# need to run only once to download and load model into memory
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def recongnize(path, logger):
    img_path = path
    result = ocr.ocr(img_path, cls=True)
    # 显示结果
    from PIL import Image

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores,
                       font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(f'{path.replace(".png","")}-result.png')
    logger.info(f'{path} OCR result: \n{pformat(result)}')
    return result


if __name__ == '__main__':
    import time
    from Logger import logger
    t = time.localtime(time.time())
    mo = str(t.tm_mon) if len(str(t.tm_mon)) == 2 else '0' + str(t.tm_mon)
    day = str(t.tm_mday) if len(str(t.tm_mday)) == 2 else '0' + str(t.tm_mday)
    hour = str(t.tm_hour) if len(str(t.tm_hour)) == 2 else '0' + str(t.tm_hour)
    minute = str(t.tm_min) if len(str(t.tm_min)) == 2 else '0' + str(t.tm_min)
    log_file = f'./logs/{t.tm_year}-{mo}-{day}-{hour}-{minute}.log'
    log = logger('DEBUG', f'./logs/{t.tm_year}-{mo}-{day}-{hour}-{minute}.log')
    while True:
        filename = input('File: ')
        recongnize(filename, log)
