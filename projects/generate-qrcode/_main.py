# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-04-02 16:59:44 UTC+08:00
"""

import qrcode
from PIL import Image


class QRCode:

    @classmethod
    def generate(cls):
        # 网址
        url = 'https://fairy.host'

        # 生成二维码
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=30,
            border=1,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white').convert('RGB')

        # 打开logo文件，并确保使用ANTIALIAS（LANCZOS）滤波器缩放
        logo = Image.open("fairylnadfuture-logo.png").convert("RGBA")  # 确保logo是透明的
        logo_size = 250  # 根据需要调整logo大小
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

        # 创建一个透明层用于合成
        logo_layer = Image.new("RGBA", img.size)
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        logo_layer.paste(logo, pos)
        final = Image.alpha_composite(img.convert("RGBA"), logo_layer)

        # 保存二维码
        final.save("qr_with_logo.png")


if __name__ == '__main__':
    QRCode.generate()
