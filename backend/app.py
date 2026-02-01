from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pypdf import PdfReader, PdfWriter
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route('/unlock', methods=['POST'])
def unlock_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    password = request.form.get('password', '')
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_in:
        file.save(temp_in.name)
        temp_in.flush()
        reader = PdfReader(temp_in.name)
        if reader.is_encrypted:
            result = reader.decrypt(password)
            if result == 0:
                os.unlink(temp_in.name)
                return jsonify({'error': 'Wrong password or decryption failed'}), 400
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_out:
            writer.write(temp_out)
            temp_out.flush()
            temp_out.seek(0)
            response = send_file(temp_out.name, as_attachment=True, download_name='unlocked.pdf')
        os.unlink(temp_in.name)
        os.unlink(temp_out.name)
        return response

@app.route('/')
def home():
    return 'PDF Unlocker Backend is running!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
