from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def generate_receipt(receipt_data):
    file_name = "receipt.pdf"
    document_title = "Payment Receipt"
    title = "Payment Receipt"
    sub_title = "Thank you for your purchase!"
    date = f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    company_name = "Your Company Name"
    company_address = "1234 Main Street, Anytown, USA"
    company_phone = "Phone: +1 (123) 456-7890"
    
    # Create a canvas object
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle(document_title)
    
    # Set the title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(300, 750, title)
    
    # Set the subtitle
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(300, 730, sub_title)
    
    # Draw a line
    pdf.line(30, 710, 580, 710)
    
    # Add company details
    pdf.setFont("Helvetica", 10)
    pdf.drawString(30, 690, company_name)
    pdf.drawString(30, 675, company_address)
    pdf.drawString(30, 660, company_phone)
    pdf.drawString(450, 690, date)
    
    # Draw another line
    pdf.line(30, 645, 580, 645)
    
    # Add receipt details
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(30, 625, "Customer Name:")
    pdf.drawString(150, 625, receipt_data["customer_name"])
    
    pdf.drawString(30, 610, "Transaction ID:")
    pdf.drawString(150, 610, receipt_data["transaction_id"])
    
    pdf.drawString(30, 595, "Payment Method:")
    pdf.drawString(150, 595, receipt_data["payment_method"])
    
    # Add table headers
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(30, 570, "Description")
    pdf.drawString(300, 570, "Quantity")
    pdf.drawString(400, 570, "Unit Price")
    pdf.drawString(500, 570, "Total")
    
    # Add table data
    pdf.setFont("Helvetica", 12)
    y = 550
    for item in receipt_data["items"]:
        pdf.drawString(30, y, item["description"])
        pdf.drawString(300, y, str(item["quantity"]))
        pdf.drawString(400, y, f"${item['unit_price']:.2f}")
        pdf.drawString(500, y, f"${item['total']:.2f}")
        y -= 20
    
    # Add total amount
    pdf.drawString(400, y-20, "Total Amount:")
    pdf.drawString(500, y-20, f"${receipt_data['total_amount']:.2f}")
    
    # Save the PDF
    pdf.save()
    print(f"Receipt generated: {file_name}")

# Example data
receipt_data = {
    "customer_name": "John Doe",
    "transaction_id": "123456789",
    "payment_method": "Credit Card",
    "items": [
        {"description": "Item 1", "quantity": 2, "unit_price": 10.00, "total": 20.00},
        {"description": "Item 2", "quantity": 1, "unit_price": 15.00, "total": 15.00},
        {"description": "Item 3", "quantity": 3, "unit_price": 7.50, "total": 22.50}
    ],
    "total_amount": 57.50
}

# Generate the receipt
generate_receipt(receipt_data)
