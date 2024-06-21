class Cliente:
    def __init__(self, nombre, documento, compra, codigoCompra):
        self.nombre = nombre        
        self.documento = documento
        self.compra = compra
        self.codigoCompra = codigoCompra
    def __str__(self):
        return f'Cliente: {self.nombre} Documento: {self.documento}'
    def detalleCompra(self):
        print(f'Compra: {self.compra}\t Código de compra: {self.codigoCompra}')