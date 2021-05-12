from ..db.documents import Product

def create_product(**kwargs):
    return Product(**kwargs).save()

def get_all_products():
    return Product.objects()

def get_one_product(id):
    return Product.objects(id=id).first()
