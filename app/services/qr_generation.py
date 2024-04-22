import qrcode
import requests
import secrets
from ..variables import ROOT, DATA_DIRECTORY, NOW, CURRENT_DAY
import os
import json
import io

# from PIL import Image
from io import BytesIO


class QrCode:
    def generate_qrcode(
        self,
        company: str,
        product: str,
        qrcode_settings: dict,
        token
    ):
        version = qrcode_settings.get("version", 1)
        box_size = qrcode_settings.get("box_size", 5)
        border = qrcode_settings.get("border", 10)
        fill_color = qrcode_settings.get("fill_color", "black")
        back_color = qrcode_settings.get("back_color", "white")


        company = str(company).replace(" ", "-").lower()
        product = str(product).replace(" ", "-").lower()
        url = f"http://192.168.15.5:5173/{company}/{product}/{token}"
        # url = f"http://produtrue.com/{company}/{product}/{token}"

        qr_obj = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )

        qr_obj.add_data(url)
        qr_obj.make(fit=True)

        # f = io.StringIO()
        # qr_obj.print_ascii(out=f)
        # f.seek(0)
        # print(f.read())

        # Gerar a imagem
        qr_image = qr_obj.make_image(fill_color=fill_color, back_color=back_color)

        # Convertendo a imagem para bytes
        image_bytes = self.get_image_bytes(qr_image)

        # Salvar a imagem no diretório
        # TODO: não será necessário no futuro
        data_directory = f"{DATA_DIRECTORY}"
        os.makedirs(data_directory, exist_ok=True)
        image_url = f"{company}{product}{token}"
        qr_image.save(os.path.join(data_directory, f"{image_url}.png"))

        return qr_obj, token, url, image_bytes

    def get_image_bytes(self, image):
        image_bytes = BytesIO()
        image.save(image_bytes)
        image_bytes.seek(0)
        return image_bytes.getvalue()
