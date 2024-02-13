from modelos.cardapio.item_cardapio import ItemCardapio



class Prato(ItemCardapio):
    def __init__(self,nom,preco,descricao):
        super().__init__(nom,preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)