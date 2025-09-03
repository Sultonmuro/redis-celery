from .models import Transfer
from celery import shared_task
import random
import string
import re
import logging
from .utils import *
logger = logging.getLogger(__name__)
@shared_task
def transfer_view():
    read_list  = Transfer.objects.all().values()
    return {"success":True,"data":list(read_list)}

@shared_task
def transfer_create(ext_id:str,receiver_card_number:str,sender_card_number:str):
    valid_card = validate_card_numbers(sender_card_number)
    if not valid_card:
        return {"success":False,"status":"Invalid card number"}
    

    transfer = Transfer.objects.create(
        ext_id = ext_id,
        receiver_card_number = receiver_card_number,
        sender_card_number=valid_card,
    )
    return {
        "success": True,
        "status": "created(200)",
        "transfer_id": transfer.id,
    }
    
