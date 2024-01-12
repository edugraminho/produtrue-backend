import jwt
import secrets


class JwtToken:
    def __init__(self, owner, item) -> None:
        self.payload = {
            "owner": owner,
            "item": item,
        }

    def generate(self):
        # Defina as informações adicionais que você deseja incluir no token
        token = jwt.encode(self.payload, "sua_chave_secreta", algorithm="HS256")

        return token



class Token:
    def token_generator(self, company, product):
        token = secrets.token_urlsafe(22)

        company = str(company).replace(" ", "-").lower()
        product = str(product).replace(" ", "-").lower()
        url = f"http://localhost/{company}/{product}/{token}"


        return token, url