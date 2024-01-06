import qrcode
import requests


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
    def __init__(self) -> None:
        pass

    def generate(self, version: int, quantity: int, box_size: int, border: int):
        """Cria um objeto QRCode
        Args:
            version (int): versoes de 1 a 40
            quantity (int): _description_
            box_size (_type_): _description_
            border (_type_): _description_
        """

        result: list = []
        for _ in range(quantity):
            qrcode_obj = qrcode.QRCode(
                version=version,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=box_size,
                border=border,
            )

            result.append(qrcode_obj)

        return result

    def add_link(self, list_qrcodes: list, url: str):
        """Adiciona o link ao QRCode
        Args:
            list_qrcodes (list): _description_
        """
        # TODO cada qrcode deve ter uma rota diferente com seu token
        result: list = []

        for qrc in list_qrcodes:
            qrc.add_data(url)
            qrc.make(fit=True)

            result.append(qrc)

        return result

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


qr = QrCode()
listqr = qr.generate(1, 5, 10, 4)

listlink = qr.add_link(listqr, "blabla.com")

qr.save_qr_image(
    listlink,
)