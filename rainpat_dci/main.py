import requests
import os

from PIL import Image
# pillow
from io import BytesIO
from aip import AipOcr
# baidu-aip



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}


def BD_img_to_str(image):
    print("image: " + str(image))
    # Image对象变成字节流对象
    imgByteArr = BytesIO()
    image.save(imgByteArr, format='PNG')  # format: PNG / JPEG
    imgByteArr = imgByteArr.getvalue()
    
    baidu_ocr_info = os.getenv('BAIDUOCR_CONFIG').strip().split()
    
    
    config = {
        'appId': baidu_ocr_info[0],
        'apiKey': baidu_ocr_info[1],
        'secretKey': baidu_ocr_info[2]
    }
    print("config %s" % config)
    client = AipOcr(**config)
    result = client.basicGeneral(imgByteArr)
    print("res: %s" %result)

    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


def rainpat_logn_in(user_n, pass_w):
    r = requests.get('https://www.rainpat.com/User/Login', headers=headers)
    cookie_dict = requests.utils.dict_from_cookiejar(r.cookies)
    cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
    s = requests.Session()
    s.cookies = cookies
    re_yzm = s.get('https://www.rainpat.com/Home/Vericode', headers=headers)

    image = Image.open(BytesIO(re_yzm.content))

    image = image.convert('L')
    out = image.resize((60 * 5, 20 * 5), Image.Resampling.LANCZOS)
    print(out)

    threshold = 80

    im = Image.new('RGB', (60 * 5, 20 * 5))
    img_str = out.load()
    for i in range(60 * 5):
        for j in range(20 * 5):
            if img_str[i, j] > threshold:
                im.putpixel((i, j), (255, 255, 255))
            else:
                im.putpixel((i, j), (0, 0, 0))
    im.show()
    itt = BD_img_to_str(im)
    print("itt: " + str(itt))
    yzm = ''
    for i in itt:
        if i.isdigit():
            yzm += i

    data = {
        'email': user_n,
        'pass': pass_w,
        'auto': 'false',
        'code': yzm.strip()
    }

    re_logn = s.post('https://www.rainpat.com/User/AjaxLogin', data=data)
    rep = 0
    if '{"msg":"","redurl":""}' == re_logn.text:
        print('rainpat 登录成功!')
        return requests.utils.dict_from_cookiejar(s.cookies)
    else:
        if rep == 3:
            print('无法登录')
            raise
        rep += 1
        rainpat_logn_in(user_n, pass_w)


def main(user_n, pass_w):
    cookie_dict = rainpat_logn_in(user_n, pass_w)
    resp = requests.post('https://www.rainpat.com/User/EverydaySignin', headers=headers, cookies=cookie_dict)
    s_info = eval(resp.text)
    print(s_info['err'])
    return(s_info['err'])


if __name__ == '__main__':
    rainpat_info = os.getenv('RAINPAT_INFO').strip().split()
    rept = 0
    for i in range(len(rainpat_info)):
        if i%2 == 0:
            while 1:
                isC = main(rainpat_info[i], rainpat_info[i+1])
                if '超时' not in isC:
                    break
                else:
                    rept += 1
                if rept == 3:
                    raise
