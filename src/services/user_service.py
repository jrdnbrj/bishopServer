from ..db.documents import User

def create_user(**kwargs):
    return User(**kwargs).save()

def get_all_users():
    return User.objects()

def get_one_user(id):
    return User.objects(id=id).first()
