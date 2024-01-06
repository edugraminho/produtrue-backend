import jwt


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
