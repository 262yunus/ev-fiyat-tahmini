# 🏠 House Price Prediction Application (Ev Fiyatı Tahmini Uygulaması)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### 📌 Overview
An end-to-end Machine Learning web application that predicts house prices based on features such as square meters, number of rooms, and building age. Built with **FastAPI** on the backend, **Scikit-learn** for machine learning, and a clean modern UI (HTML5/CSS3) on the frontend.

### ✨ Key Features
- **End-to-End Pipeline:** ML model integrated directly with a REST API.
- **Real-Time Predictions:** Instant house value estimation based on user input.
- **User-Friendly UI:** Modern, responsive HTML/CSS interface with input bounds validation and formatted output.
- **Input Validation:** Input limits pre-defined (`20 - 500 m²`, `1 - 10 rooms`, `0 - 50 age`) for optimal model performance.

### 🛠️ Tech Stack
- **Machine Learning:** Python, Scikit-learn, Pandas, NumPy
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Version Control:** Git & GitHub

### 🚀 Getting Started

#### Prerequisites
- Python 3.10+

#### Installation & Run
1. **Clone the repository:**
   git clone https://github.com/262yunus/ev-fiyat-tahmini.git
   cd ev-fiyat-tahmini

2. **Run the server:**
   python -m uvicorn main:app --reload

3. **Open in browser:**
   Go to `http://127.0.0.1:8000`

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### 📌 Genel Bakış
Metrekare, oda sayısı ve bina yaşı gibi değişkenleri kullanarak ev fiyatlarını tahmin eden uçtan uca (end-to-end) Makine Öğrenmesi web uygulaması. Backend tarafında **FastAPI**, makine öğrenmesinde **Scikit-learn** ve frontend tarafında modern HTML/CSS kullanılarak geliştirilmiştir.

### ✨ Öne Çıkan Özellikler
- **Uçtan Uca Mimari:** Makine öğrenmesi modelinin REST API ile doğrudan entegrasyonu.
- **Gerçek Zamanlı Tahmin:** Kullanıcı girdilerine dayalı anlık piyasa değeri tahmini.
- **Modern Arayüz:** Kullanıcı dostu, girdi sınırlandırmaları olan ve çıktıları biçimlendirilmiş şık tasarım.
- **Girdi Doğrulama:** Model kararlılığı için sınırlandırılmış veri aralıkları.

### 🛠️ Kullanılan Teknolojiler
- **Makine Öğrenmesi:** Python, Scikit-learn, Pandas, NumPy
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML5, CSS3, JavaScript
- **Versiyon Kontrolü:** Git & GitHub

---

## 📸 Application Screenshot / Uygulama Ekran Görüntüsü

![Application Screenshot](ekran_goruntusu.png)