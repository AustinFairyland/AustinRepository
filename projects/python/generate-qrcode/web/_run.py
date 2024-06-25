# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 04 02, 2024
"""

from flask import Flask, send_file, request, abort
import qrcode
from PIL import Image
import io

app = Flask(__name__)


@app.route('/create_qr', methods=['POST'])
def create_qr():
    try:
        # 获取请求数据
        url = request.form['url']
        logo_file = request.files['logo']

        # 生成二维码
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=30,
            border=1,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # 处理logo
        logo = Image.open(logo_file).convert("RGBA")
        logo_size = 200
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

        # 创建透明层，合成二维码和logo
        logo_layer = Image.new("RGBA", img.size)
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        logo_layer.paste(logo, pos)
        final = Image.alpha_composite(img.convert("RGBA"), logo_layer)

        # 保存到内存
        img_io = io.BytesIO()
        final.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        print(e)
        abort(400, 'Could not generate QR code.')


if __name__ == '__main__':
    app.run(debug=True)
