class BancoDeDadosSimulado:
    def __init__(self):
        self.usuarios = {}

    def add_usuario(self, id_usuario, nome):
        self.usuarios[id_usuario] = nome

    def buscar_usuario(self, id_usuario):
        return self.usuarios.get(id_usuario)

    def remover_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]


