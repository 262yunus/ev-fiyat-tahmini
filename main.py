from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd

app = FastAPI(title="Ev Fiyat Tahmin Uygulaması")

# Modeli Yükle
model = joblib.load('ev_fiyat_modeli.pkl')

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Ev Fiyatı Tahmin Et</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f7f6; margin: 50px; display: flex; justify-content: center; }}
        .card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 360px; }}
        h2 {{ color: #2c3e50; text-align: center; margin-top: 0; }}
        label {{ font-weight: bold; color: #555; display: block; margin-top: 15px; }}
        input {{ width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }}
        button {{ width: 100%; background-color: #27ae60; color: white; padding: 12px; border: none; border-radius: 6px; font-size: 16px; margin-top: 20px; cursor: pointer; }}
        button:hover {{ background-color: #219150; }}
        .result {{ margin-top: 20px; padding: 15px; background: #e8f8f5; border-left: 5px solid #27ae60; border-radius: 4px; }}
        .error {{ margin-top: 20px; padding: 15px; background: #fadbd8; border-left: 5px solid #e74c3c; border-radius: 4px; color: #78281f; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>🏠 Ev Fiyatı Tahmini</h2>
        <form action="/web-tahmin" method="post">
            <label>Metrekare (m²): [20 - 500]</label>
            <input type="number" name="metrekare" value="{metrekare_val}" min="20" max="500" required>
            
            <label>Oda Sayısı: [1 - 10]</label>
            <input type="number" name="oda_sayisi" value="{oda_val}" min="1" max="10" required>
            
            <label>Bina Yaşı: [0 - 50]</label>
            <input type="number" name="bina_yasi" value="{yasi_val}" min="0" max="50" required>
            
            <button type="submit">Tahmin Et 🚀</button>
        </form>
        {sonuc_alani}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html_template.format(
        metrekare_val=120,
        oda_val=3,
        yasi_val=5,
        sonuc_alani=""
    )

@app.post("/web-tahmin", response_class=HTMLResponse)
def web_tahmin(metrekare: float = Form(...), oda_sayisi: int = Form(...), bina_yasi: float = Form(...)):
    
    # Backend Kontrolü (Validation)
    if not (20 <= metrekare <= 500) or not (1 <= oda_sayisi <= 10) or not (0 <= bina_yasi <= 50):
        hata_html = """
        <div class="error">
            ⚠️ <strong>Geçersiz Değer!</strong><br>
            Lütfen değerleri belirlenen aralıklarda giriniz:
            <ul>
                <li>Metrekare: 20 - 500 m²</li>
                <li>Oda Sayısı: 1 - 10</li>
                <li>Bina Yaşı: 0 - 50 yıl</li>
            </ul>
        </div>
        """
        return html_template.format(
            metrekare_val=int(metrekare),
            oda_val=oda_sayisi,
            yasi_val=int(bina_yasi),
            sonuc_alani=hata_html
        )

    # Değerler mantıklıysa model tahmini yap
    yeni_data = pd.DataFrame([[metrekare, oda_sayisi, bina_yasi]], 
                             columns=['Metrekare', 'Oda_Sayisi', 'Bina_Yasi'])
    
    tahmin_tl = model.predict(yeni_data)[0]
    
    sonuc_html = f"""
    <div class="result">
        <p style="margin:0; font-size:14px; color:#555;">Tahmini Piyasa Değeri:</p>
        <h3 style="margin:5px 0 0 0; color:#27ae60;">{tahmin_tl:,.2f} TL</h3>
    </div>
    """
    
    return html_template.format(
        metrekare_val=int(metrekare),
        oda_val=oda_sayisi,
        yasi_val=int(bina_yasi),
        sonuc_alani=sonuc_html
    )