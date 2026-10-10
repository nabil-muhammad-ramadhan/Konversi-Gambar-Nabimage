import os
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def halaman_utama():
    return render_template('index.html')

@app.route('/konversi', methods=['POST'])
def konversi():
    file = request.files['file_gambar']
    format_tujuan = request.form.get('format_tujuan')
    
    if file.filename == '':
        return "Kamu belum memilih file gambar!"
    
    if file:
        
        if format_tujuan == 'jpg':
            format_tujuan = 'jpeg'

        img = Image.open(file)
            
        if format_tujuan == 'jpeg' and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        nama_file_asli = file.filename.rsplit('.', 1)[0]
        nama_file_baru = f"{nama_file_asli}.{format_tujuan}"
        
        jalur_simpan = os.path.join(app.config['UPLOAD_FOLDER'], nama_file_baru)
        
        img.save(jalur_simpan, format=format_tujuan.upper())
        return send_file(jalur_simpan, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)





