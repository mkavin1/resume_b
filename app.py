from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    # Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    experience = request.form.get('experience')
    education = request.form.get('education')
    skills = request.form.get('skills')

    # Choose the template type from form data
    template_type = request.form.get('template')

    # Create PDF in memory
    pdf = BytesIO()
    c = canvas.Canvas(pdf, pagesize=letter)
    width, height = letter

    # Template-based content
    if template_type == 'template1':
        # Basic layout for template 1
        c.drawString(100, height - 50, f"Name: {name}")
        c.drawString(100, height - 70, f"Email: {email}")
        c.drawString(100, height - 90, f"Phone: {phone}")
        c.drawString(100, height - 110, f"Address: {address}")
        c.drawString(100, height - 130, "Experience:")
        c.drawString(100, height - 150, experience)
        c.drawString(100, height - 190, "Education:")
        c.drawString(100, height - 210, education)
        c.drawString(100, height - 250, "Skills:")
        c.drawString(100, height - 270, skills)
    else:
        # Basic layout for template 2
        c.drawString(100, height - 50, f"RESUME OF {name.upper()}")
        c.drawString(100, height - 90, f"Contact: {email}, {phone}")
        c.drawString(100, height - 130, f"Address: {address}")
        c.drawString(100, height - 180, "Experience:")
        c.drawString(100, height - 200, experience)
        c.drawString(100, height - 250, "Education:")
        c.drawString(100, height - 270, education)
        c.drawString(100, height - 320, "Skills:")
        c.drawString(100, height - 340, skills)

    # Finalize the PDF
    c.showPage()
    c.save()

    # Return the generated PDF as a file to download
    pdf.seek(0)
    return send_file(pdf, as_attachment=True, download_name='resume.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
