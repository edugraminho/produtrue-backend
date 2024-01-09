import qrcode
import requests
import secrets


from pathlib import Path, PurePath
import os
from datetime import datetime, timedelta
from enum import Enum


# ====================== DIRETÓRIOS LOCAIS e DATAS ======================
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIRECTORY = os.path.join(ROOT, "data")
NOW = datetime.now().strftime("%d/%m/%y %H:%M:%S")
CURRENT_DAY = datetime.now().strftime("%d/%m")


class QrCode:
    def generate_qrcode(
        self,
        company: str,
        product: str,
        version: int = 1,
        box_size: int = 5,
        border: int = 10,
    ):
        """Cria um objeto QRCode
        Args:
            version (int): versoes de 1 a 40
            box_size (_type_):
            border (_type_):
            data (dict): Dados a serem codificados no QRCode
        """

        # Gerar um token aleatório
        token = secrets.token_urlsafe(16)

        url = f"http://localhost/{company}/{product}/{token}"

        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )

        qr.add_data(url)
        qr.make(fit=True)

        return qr, token, url

    def save_qr_image(
        self, list_qrcodes: list, fill_color: str = "black", back_color: str = "white"
    ):
        """Cria uma imagem PIL (Python Imaging Library) do QRCode e
            salva a imagem em um arquivo
        Args:
            list_qrcodes (list): _description_
            fill_color (str): _description_
            back_color (str): _description_
        """

        for qrc in list_qrcodes:
            imagem_qrcode = qrc.make_image(fill_color=fill_color, back_color=back_color)

            # Salva a imagem em um arquivo
            imagem_qrcode.save(f"{DATA_DIRECTORY}/qrcode.png")


# qr = QrCode()
# listqr = qr.generate(1, 5, 10, 4)

# listlink = qr.add_link(listqr, "blabla.com")

# qr.save_qr_image(
#     listlink,
# )
