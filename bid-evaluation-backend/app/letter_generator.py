from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from io import BytesIO
from fastapi.responses import StreamingResponse

def generate_letter_of_acceptance_pdf(bidder_name: str, tender_title: str, contract_value: float):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 50, "Letter of Acceptance")

    c.setFont("Helvetica", 12)
    text = f"""
Dear {bidder_name},

We are pleased to inform you that your bid for the tender titled '{tender_title}'
has been accepted. The contract value is LKR {contract_value:,.2f}.

Please consider this letter as formal Notification of Award.

Regards,
Procurement Committee
"""

    y = height - 150
    for line in text.strip().splitlines():
        c.drawString(70, y, line.strip())
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

def letter_response(bidder_name, tender_title, contract_value):
    pdf_stream = generate_letter_of_acceptance_pdf(bidder_name, tender_title, contract_value)
    headers = {
        'Content-Disposition': f'attachment; filename="LetterOfAcceptance_{bidder_name}.pdf"'
    }
    return StreamingResponse(pdf_stream, media_type='application/pdf', headers=headers)
