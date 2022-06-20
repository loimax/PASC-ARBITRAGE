from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
pdf = canvas.Canvas('test.pdf')
pdf.drawString(3*cm, 25*cm, u'Bonjour')
pdf.line(3*cm,24.5*cm,18*cm,24.5*cm)
pdf.drawString(3*cm, 23*cm, u'Un texte')
pdf.save()