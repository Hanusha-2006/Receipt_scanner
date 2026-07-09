import re

def parse_receipt(lines):
    receipt_data = {
        "store_name": None,
        "date":None,
        "time":None,
        "subtotal":None,
        "total":None,
        "tax":None,
        "items":[]
    }
    
    num = []
    m = []
    full_text = " ".join(lines)
    print("Full text: ", full_text)
    
    SKIP_KEYWORDS = ['total','subtotal','store_name','date','time','tax','items']
    # Extract store name
    receipt_data["store_name"] = lines[0]
    

    # Date
    date_match = re.search(r'\b(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}/\d{2}/\d{4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}.\s+\d{4})\b', full_text, re.IGNORECASE)
    if date_match:
        receipt_data["date"] = date_match.group()

    # Extract time 

    time_match = re.search(r'\b(\d{1,2}:\d{2})(?:\d{2})?\s*(AM|PM|am|pm)?|\d{2}:\d{2}\b',full_text)
    if time_match:
        receipt_data["time"] = time_match.group()
        # receipt_data['time'] = time_match.group(1) | time_match.group(0)

    # Extract total
    total_match = re.search(r'(?:total amount|grand total|amount due|total)\s*[:\s]*\$?\s*(\d+[\.,]\d{2})', full_text, re.IGNORECASE)
    if total_match is not None:
        receipt_data["total"] = "$" + total_match.group(1)
    else:
        m = []
        num = re.finditer(r'\$\s*(\d+[\.,]\d{2})', full_text)
        for n in num:
            m.append(n.group(1))
         
        if len(m) > 0:    
            m.sort(key=lambda x:float(x.replace(',','')))
            total = max(m, key=lambda x: float(x.replace(',', '')))
            receipt_data["total"] = "$" + total
            print("total numbers found:", len(m))
        
        else:
            num2 = re.finditer(r'\b(\d+)\b', full_text)
            plain = []
            for n in num2:
                plain.append(n.group(1))
            if len(plain) > 0:
                total = max(plain, key=lambda x:float(x))
                receipt_data["total"] = "$" + total

    # Extract subtotal
    subtotal_match = re.search(r'(?:subtotal|sub total)\s*[:\s]*\$?\s*(\d+[\.,]\d{2})', full_text, re.IGNORECASE)
    if subtotal_match:
        receipt_data["subtotal"] = "$" + subtotal_match.group(1)

    # Extract tax
    tax_match = re.search(
    r'(?:tax|gst|cgst|sgst)\s*(?:[:\s]|\d+(?:\.\d+)?%)?\s*'
    r'(?:rs\.?|₹)?\s*'
    r'(\d+(?:,\d{3})*(?:[\.,]\d{1,2})?)', full_text, re.IGNORECASE)
    if tax_match:
        receipt_data["tax"] = "$" + tax_match.group(1)
        

    # Extract items (format: item name follwoed by price)
    item_matches = re.findall(r'(\d+x\s+[A-Za-z][^\$\d]+?)\s*\$\s*(\d+[\.,]\d{2})', full_text, re.IGNORECASE)
    for name, price in item_matches:
        name = name.strip()
        if not any(kw in name.lower() for kw in SKIP_KEYWORDS):
            receipt_data["items"].append({
                "name":  name,
                "price": "$" + price
                
            })

    # m = []
    # num = re.finditer(r'\$\s*(\d+[\.,]\d{2})', full_text)
    # for n in num:
    #     m.append(n.group(1))
        
    # m.sort(key=lambda x:float(x.replace(',','')))
    # print("total numbers found:", len(m))
    
    # total = max(m, key=lambda x: float(x.replace(',', '')))
    # print("Total numbers found:", total)
        

    return receipt_data
    
    