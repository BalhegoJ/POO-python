class Item:
    def __init__(self, nomeDoItem):
        self.nomeDoItem = nomeDoItem


class GerenciadorDeEstoque:
    def __init__(self):
        self.estoque = {}

    def cadastrar_item(self, id_item, nomeDoItem):
        if id_item in self.estoque:
            raise ValueError("Item com esta ID já existe")
        self.estoque[id_item] = Item(nomeDoItem)

    def listar_itens(self):
        return {id_item: item.nomeDoItem for id_item, item in self.estoque.items()}

    def editar_item(self, id_item, novo_nomeDoItem):
        if id_item not in self.estoque:
            raise ValueError("Item não cadastrado no estoque")
        self.estoque[id_item].nomeDoItem = novo_nomeDoItem

    def excluir_item(self, id_item):
        if id_item not in self.estoque:
            raise ValueError("Item não cadastrado no estoque")
        del self.estoque[id_item]