import pytesseract
from PIL import Image
import io
import re

async def extract_text_from_image(image_bytes: bytes) -> dict:
    """
    Extracts text from image bytes using Tesseract OCR and parses key fields.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # Simple extraction
        text = pytesseract.image_to_string(image)
        
        return parse_receipt_text(text)
    except Exception as e:
        print(f"OCR Error: {e}")
        return {"merchant_name": "Unknown", "total_amount": 0.0, "date_extracted": None}

def parse_receipt_text(text: str) -> dict:
    lines = text.split('\n')
    
    # Very basic parsing logic (Improve this with NLP later)
    merchant = lines[0].strip() if lines else "Unknown"
    
    # Regex for money (e.g., $12.34 or 12.34)
    amount_pattern = r'\$?\s?(\d+\.\d{2})'
    amounts = []
    
    for line in lines:
        match = re.search(amount_pattern, line)
        if match:
            try:
                amounts.append(float(match.group(1)))
            except:
                pass
                
    # Heuristic: The largest amount is likely the total
    total = max(amounts) if amounts else 0.0
    
    return {
        "merchant_name": merchant,
        "total_amount": total,
        "date_extracted": "2024-01-01" # Placeholder for date regex
    }
