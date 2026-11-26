from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from email.message import EmailMessage
import smtplib, ssl, time

pdf_path = "/home/ecghealth/ecg_report.pdf"

def generate_report(ecg_value):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.setFont("Helvetica", 14)
    c.drawString(50, 800, "ECG Monitoring Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 740, f"Sample ECG Value: {ecg_value}")
    c.drawString(50, 710, "Note: Auto-generated report.")
    c.showPage()
    c.save()

def send_email(recipient, ecg_value):
    generate_report(ecg_value)
    sender = "your.email@gmail.com"
    password = "YOUR_APP_PASSWORD"

    msg = EmailMessage()
    msg["Subject"] = "Your ECG Report"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("Hello,\n\nPlease find attached your ECG report.\n\nRegards,\nECG Monitoring System")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="ECG_Report.pdf")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("✅ Email sent to", recipient)
