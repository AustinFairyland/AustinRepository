# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-04-02 16:59:44 UTC+08:00
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("二维码生成器")

        # 输入URL
        tk.Label(root, text="输入URL：").grid(row=0, column=0, padx=10, pady=10)
        self.entry_url = tk.Entry(root, width=40)
        self.entry_url.grid(row=0, column=1, padx=10, pady=10)

        # 输入Logo文件路径
        tk.Label(root, text="Logo路径：").grid(row=1, column=0, padx=10, pady=10)
        self.entry_logo = tk.Entry(root, width=35)
        self.entry_logo.grid(row=1, column=1, padx=10, pady=10)
        button_browse = tk.Button(root, text="浏览", command=self.browse_file)
        button_browse.grid(row=1, column=2, padx=10, pady=10)

        # 输入Logo尺寸
        tk.Label(root, text="Logo尺寸：").grid(row=2, column=0, padx=10, pady=10)
        self.entry_logo_size = tk.Entry(root, width=10)
        self.entry_logo_size.grid(row=2, column=1, padx=10, pady=10)
        self.entry_logo_size.insert(0, "200")  # 默认值为200

        # 生成按钮
        button_generate = tk.Button(root, text="生成二维码", command=self.generate_qr)
        button_generate.grid(row=3, column=1, padx=10, pady=10)

        # 保存按钮
        button_save = tk.Button(root, text="保存二维码", command=self.save_qr)
        button_save.grid(row=4, column=1, padx=10, pady=10)

        # 状态标签
        self.lbl_status = tk.Label(root, text="")
        self.lbl_status.grid(row=5, column=1, padx=10, pady=10)

        # 二维码显示标签
        self.lbl_qr = tk.Label(root)
        self.lbl_qr.grid(row=6, column=1, padx=10, pady=20)

        self.final_image = None

    def generate_qr(self):
        url = self.entry_url.get()
        logo_path = self.entry_logo.get()
        try:
            logo_size = int(self.entry_logo_size.get())
        except ValueError:
            self.lbl_status.config(text="Logo尺寸必须是一个整数！")
            return

        if not url or not logo_path:
            self.lbl_status.config(text="URL或Logo路径不能为空！")
            return

        try:
            qr = qrcode.QRCode(
                version=3,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            logo = Image.open(logo_path).convert("RGBA")
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

            logo_layer = Image.new("RGBA", img.size)
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            logo_layer.paste(logo, pos)
            final = Image.alpha_composite(img.convert("RGBA"), logo_layer)

            self.final_image = final.resize((200, 200), Image.Resampling.LANCZOS)
            tk_image = ImageTk.PhotoImage(self.final_image)
            self.lbl_qr.config(image=tk_image)
            self.lbl_qr.image = tk_image  # keep a reference!
            self.lbl_status.config(text="二维码生成成功！")

        except Exception as e:
            self.lbl_status.config(text="生成二维码出错：" + str(e))

    def save_qr(self):
        if self.final_image is None:
            self.lbl_status.config(text="请先生成二维码！")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if not file_path:
            return  # 用户取消了保存

        self.final_image.save(file_path)
        self.lbl_status.config(text="二维码已保存！")

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.entry_logo.delete(0, tk.END)
        self.entry_logo.insert(0, filename)


if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
