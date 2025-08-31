import random
import string
import re
import logging

logger = logging.getLogger(__name__)







def generate_otp(length=6):
    otp = ""
    for i in range(length):
        otp+=random.choice(string.digits)
def validate_card_numbers(row:str):
    CARD_PREFIXES = {
        "8600":"HUMO",
        "6262": "UZCARD",
         "4": "VISA",         
        "5": "MASTERCARD",
    }
    cleaned_card_number = re.sub(r'\D','',row)
    sorted_prefixes = sorted(CARD_PREFIXES.keys(),key=len,reverse=True)
   

    digits = list()
    
    detected_card_type = "UNKNOWN"
    

    for prefix in sorted_prefixes:
        if cleaned_card_number.startswith(prefix):
            detected_card_type = CARD_PREFIXES[prefix]
            break
    
    if detected_card_type == "UNKNOWN":
        logger.error(f"ERROR: We could not detect any card number. {cleaned_card_number}")
    
    for digit in row:
        if not digit.isdigit():
            logger.error(f"ERROR: Invalid digit:'{digit}' in card number {cleaned_card_number}")
        digits.append(int(digit))
#luhn algorithm
    total_sum = 0
    for i,num in enumerate(digits):
        if i%2==1:
            doubled = num *2
            if doubled>9:
                doubled -=9
            total_sum +=doubled
        else:
            total_sum+=num
        if total_sum % 10 != 0:
            logger.error("ERROR: Invalid checksum for card number.")
            return False
    match detected_card_type:
         case "HUMO":
            logger.info(f"DEBUG: This is a Humo card. from prefix {prefix}")
         case 'UZCARD':
            logger.info(f"DEBUG: THIS IS UZCARD (from prefix: {prefix})")
            
         case 'VISA':
            logger.info(f"DEBUG: THIS IS VISA CARD (from prefix: {prefix})")
            
         case 'MASTERCARD':
            logger.info(f"DEBUG: THIS IS MASTERCARD (from prefix: {prefix})")
            
         case _:
            logger.info(f"ERROR: Unexpected card type: {detected_card_type}. This should have been caught.")
            return False
    if len(cleaned_card_number) ==16:
        return cleaned_card_number
    else:
        logger.error("Invalid length of card number.")    