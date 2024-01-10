import qrcode
import requests
import secrets
from ..variables import ROOT, DATA_DIRECTORY, NOW, CURRENT_DAY
import os

# from PIL import Image
from io import BytesIO


class QrCode:
    def generate_qrcode(
        self,
        company: str,
        product: str,
        qrcode_settings: dict,
    ):
        version = qrcode_settings.get("version", 1) #"version"] if qrcode_settings["version"] else 1
        box_size = qrcode_settings.get("box_size", 5) 
        border = qrcode_settings.get("border", 10)
        fill_color = qrcode_settings.get("fill_color", "black")
        back_color = qrcode_settings.get("back_color", "white")

        token = secrets.token_urlsafe(22)

        company = str(company).replace(" ", "-").lower()
        product = str(product).replace(" ", "-").lower()
        url = f"http://localhost/{company}/{product}/{token}"

        qr_obj = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )

        qr_obj.add_data(url)
        qr_obj.make(fit=True)

        # Gerar a imagem
        qr_image = qr_obj.make_image(fill_color=fill_color, back_color=back_color)

        # Convertendo a imagem para bytes
        image_bytes = self.get_image_bytes(qr_image)

        # Salvar a imagem no diretório
        # TODO: não será necessário no futuro
        data_directory = f"{DATA_DIRECTORY}"
        os.makedirs(data_directory, exist_ok=True)
        image_url = f"{product}{token}"
        # qr_image.save(os.path.join(data_directory, f"{image_url}.png"))

        return qr_obj, token, url, image_bytes

    def get_image_bytes(self, image):
        image_bytes = BytesIO()
        image.save(image_bytes)
        image_bytes.seek(0)
        return image_bytes.getvalue()
