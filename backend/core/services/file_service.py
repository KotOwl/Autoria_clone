import os
from uuid import  uuid1

def upload_advertisement_photo(instance,filename:str)->str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.advertisement.model_of_car,f'{uuid1()}.{ext}')

def upload_dealership_advertisement_photo(instance,filename:str)->str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.dealership_advertisement.model_of_car,f'{uuid1()}.{ext}')