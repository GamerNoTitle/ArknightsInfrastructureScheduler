from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# need to run only once to download and load model into memory
ocr = PaddleOCR(use_angle_cls=True, lang="ch")


def recongnize(path):
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
    return result


if __name__ == '__main__':
    while True:
        filename = input('File: ')
        recongnize(filename)
