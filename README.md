# 🏠 House Price Prediction Application (Ev Fiyatı Tahmini Uygulaması)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### 📌 Overview

This project is an end-to-end web application that estimates house market values based on property features (Square Meters, Number of Rooms, Building Age) using a machine learning model.

Designed using an AI-Assisted Development approach; model training, API architecture, input validation, and frontend integration processes were executed via pair programming.

---

## 🛠️ Tech Stack & Libraries

* Python 3.12
* Scikit-learn (Linear Regression Model)
* Pandas & NumPy (Data Processing & Preparation)
* FastAPI (Web API & Frontend Server)
* Uvicorn (ASGI Server)
* Joblib (Model Serialization / Saving)

---

## 🚀 Key Features

* High Model Performance: High accuracy achieved on the dataset using a Linear Regression model (R² ≈ 97%).
* User-Friendly Web Interface: Clean, fast, and user-centric HTML/CSS interface instead of complex raw API outputs.
* Input Validation: Security and consistency rules preventing invalid or extreme out-of-bound values at both the HTML5 and FastAPI backend levels.
* Technical Documentation: Interactive Swagger API documentation automatically available via the `/docs` route.

---

## 💻 Installation & Usage

To run and test the project on your local machine, you can follow these steps:

1. Clone the Repository:
git clone https://github.com/262yunus/ev-fiyat-tahmini.git
cd ev-fiyat-tahmini

2. Install Required Dependencies:
pip install -r requirements.txt

3. Run the Application:
uvicorn main:app --reload

4. Open http://127.0.0.1:8000 in your browser to use the application directly!

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### 📌 Genel Bakış

Bu proje, makine öğrenmesi modeli kullanarak ev özelliklerine (Metrekare, Oda Sayısı, Bina Yaşı) göre tahmini piyasa değerini hesaplayan uçtan uca bir web uygulamasıdır.

AI-Assisted Development (Yapay Zeka Destekli Geliştirme) yaklaşımıyla tasarlanmış; model eğitimi, API mimarisi, girdi doğrulama (validation) ve arayüz entegrasyonu süreçleri eşli kodlama (pair programming) ile yürütülmüştür.

---

## 🛠️ Teknolojiler ve Kütüphaneler

* Python 3.12
* Scikit-learn (Linear Regression Modeli)
* Pandas & NumPy (Veri İşleme ve Hazırlık)
* FastAPI (Web API & Arayüz Sunucusu)
* Uvicorn (ASGI Server)
* Joblib (Model Serileştirme / Kaydetme)

---

## 🚀 Öne Çıkan Özellikler

* Yüksek Model Başarısı: Veri seti üzerinde eğitilen Lineer Regresyon modeli ile yüksek başarım (R2 ≈ %97).
* Kullanıcı Dostu Web Arayüzü: Karmaşık API çıktıları yerine sade, hızlı ve kullanıcı odaklı HTML/CSS arayüzü.
* Girdi Doğrulama (Validation): Hatalı veya aşırı uç değerlerin girilmesini hem HTML5 hem de FastAPI arka planında engelleyen güvenlik kuralı.
* Teknik Dokümantasyon: /docs adresi üzerinden erişilebilen otomatik Swagger API dokümantasyonu.

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırıp denemek için şu adımları izleyebilirsiniz:

1. Repoyu Klonlayın:
git clone https://github.com/262yunus/ev-fiyat-tahmini.git
cd ev-fiyat-tahmini

2. Gerekli Kütüphaneleri Yükleyin:
pip install -r requirements.txt

3. Uygulamayı Başlatın:
uvicorn main:app --reload

4. Tarayıcınızda http://127.0.0.1:8000 adresine giderek uygulamayı doğrudan kullanabilirsiniz!

---

## 📸 Application Screenshot // Uygulama Ekran görüntüsü

![Application Screenshot](ekran_goruntusu.png)