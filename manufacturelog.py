#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def validate_and_extract_log(s):
    
    batches = []
    i = 0
    
    while i < len(s):
        #batch_prefix
        batch = {}
        if s[i] != 'B':
            return 'invalid'
        i = i+1
        
        #batch_id
        batch_id = s[i:i+4]
        if not batch_id.isdigit():
            return 'invalid'
        i = i+4
        
        #product_code
        if s[i] != 'P':
            return 'invalid'
        i = i+1
        product_code = s[i:i+2]
        if not (product_code.isalpha() and product_code.isupper()):
            return 'invalid'
        i = i+2
        
        #quantity
        if s[i] != 'Q':
            return 'invalid'
        i = i+1
        quantity = ''
        while i < len(s) and s[i].isdigit():
            quantity = quantity + s[i]
            i = i+1
            
        #This section stumped me for a while, landed up having to watch youtube for help
        if quantity.lstrip('0') == '':
            quantity = 0
        else:
            quantity = int(quantity.lstrip('0'))
        
        #date
        if s[i] != 'D':
            return 'invalid'
        i = i+1
        date = s[i:i+8]
    
        if not date.isdigit() or len(date) != 8: 
            return 'invalid'
        
        year_str, month_str, day_str = date[:4], date[4:6], date[6:]
        
        if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
            return 'invalid'
        
        try:
            year, month, day = int(year_str), int(month_str), int(day_str)
        except ValueError:
            return 'invalid'
        
        if not (2000 <= year <= 2099 and 1 <= month <= 12 and 1 <= day <= 31):
                return 'invalid'
        
        
        #return_dictionaries
        batches.append({
            'BatchID' : batch_id, 
            'ProductCode' : product_code, 
            'Quantity' : quantity, 
            'Date' : date
        })
        
        i = i+8
   


    return batches or 'invalid'

