# Tokopedia-Shopee Sold Quantity Monitor

## 🎯 Motivasi

Proyek ini dibuat untuk membantu seller dan analis e-commerce dalam memantau dan membandingkan kuantitas produk yang terjual di dua marketplace terbesar di Indonesia: Tokopedia dan Shopee. Dengan otomatisasi monitoring ini, Anda dapat:

- Mengidentifikasi tren penjualan produk kompetitor
- Membuat strategi pricing yang lebih efektif
- Memantau performa produk secara real-time
- Mengoptimalkan inventory management

## ✨ Fitur Utama

### 🔍 Web Scraping
- **Multi-platform scraping**: Mengambil data dari Tokopedia dan Shopee secara bersamaan
- **Product tracking**: Monitor sold quantity, harga, rating, dan review count
- **Keyword monitoring**: Track produk berdasarkan kata kunci tertentu

### 📊 Analisis Tren Penjualan
- **Historical tracking**: Menyimpan data penjualan dalam rentang waktu tertentu
- **Growth analysis**: Analisis pertumbuhan penjualan harian/mingguan/bulanan
- **Performance comparison**: Bandingkan performa produk antar platform

### 💰 Analisis Harga
- **Price monitoring**: Track perubahan harga produk over time
- **Competitor pricing**: Analisis strategi harga kompetitor
- **Price-to-sales correlation**: Korelasi antara harga dan volume penjualan

### 🎉 Event & Promo Detection
- **Sale event tracking**: Deteksi otomatis event sale besar (11.11, 12.12, dll)
- **Discount analysis**: Analisis efektivitas diskon terhadap penjualan
- **Flash sale monitoring**: Monitor produk yang masuk flash sale

### 🏪 Perbandingan Seller
- **Seller performance**: Bandingkan performa seller di kedua platform
- **Market share analysis**: Analisis pangsa pasar per kategori produk
- **Competitive positioning**: Posisi kompetitif produk di market

## 🚀 Panduan Penggunaan

### Prerequisites
- Python 3.8+
- Chrome browser
- Stable internet connection

### Instalasi
```bash
# Clone repository
git clone https://github.com/dewarakaks/tokopedia-shopee-sold-qty-monitor.git
cd tokopedia-shopee-sold-qty-monitor

# Install dependencies
pip install -r requirements.txt

# Setup ChromeDriver
# Download dari https://chromedriver.chromium.org/
# Letakkan di folder src/drivers/
```

### Konfigurasi
```python
# Edit config.py
CONFIG = {
    'tokopedia': {
        'base_url': 'https://www.tokopedia.com',
        'search_delay': 2,
        'max_products': 100
    },
    'shopee': {
        'base_url': 'https://shopee.co.id',
        'search_delay': 3,
        'max_products': 100
    },
    'keywords': ['laptop gaming', 'smartphone 5G', 'tas ransel'],
    'schedule': '0 */6 * * *'  # Every 6 hours
}
```

### Menjalankan Monitor
```bash
# Single run
python src/main.py

# Scheduled monitoring
python src/scheduler.py

# Generate report
python src/generate_report.py --period 7d
```

## 📈 Contoh Output

### Tabel Perbandingan Sold Quantity

| Produk | Tokopedia (Sold) | Shopee (Sold) | Price Diff | Growth 7d |
|--------|------------------|---------------|------------|----------|
| iPhone 14 Pro | 1,234 | 2,156 | -5.2% | +15.3% |
| Samsung Galaxy S23 | 987 | 1,543 | +2.1% | +8.7% |
| MacBook Air M2 | 456 | 321 | +12.5% | +22.1% |
| Xiaomi 13 Pro | 2,134 | 3,421 | -8.9% | +31.4% |

### Grafik Tren Penjualan (7 Hari)

```
Tokopedia vs Shopee - Sold Quantity Trend

   3500 |                                        
        |                               ◆        
   3000 |                        ◆     /        
        |                 ◆     /     /         
   2500 |          ◆     /     /     /          
        |   ◆     /     /     /     /           
   2000 |  /     /     /     /     /            
        | /     /     /     /     /             
   1500 |/     /     /     /     /              
        +----+----+----+----+----+----+--------
        Mon  Tue  Wed  Thu  Fri  Sat  Sun
        
   ◆ Shopee    ○ Tokopedia
```

### Dashboard Insights
- **Top Performer**: Shopee menunjukkan volume penjualan 23% lebih tinggi
- **Price Advantage**: Tokopedia rata-rata 3.2% lebih murah
- **Growth Rate**: Kategori smartphone tumbuh 28% minggu ini
- **Opportunity**: 15 produk menunjukkan gap signifikan antar platform

## 📦 Dependensi Python

```txt
# Web Scraping & Browser Automation
selenium==4.15.2
beautifulsoup4==4.12.2
requests==2.31.0

# Data Processing & Analysis
pandas==2.1.3
numpy==1.25.2
scipy==1.11.4

# Database & Storage
sqlite3  # Built-in
openpyxl==3.1.2

# Visualization & Reporting
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.17.0

# Task Scheduling
schedule==1.2.0
apscheduler==3.10.4

# Configuration & Logging
pyaml==6.0.1
loguru==0.7.2

# Notifications
telebot==4.15.1
twilio==8.10.3

# Performance & Monitoring
tqdm==4.66.1
psutil==5.9.6
```

## 📁 Struktur Folder

```
tokopedia-shopee-sold-qty-monitor/
│
├── src/                          # Source code utama
│   ├── scrapers/                # Web scraping modules
│   │   ├── tokopedia_scraper.py
│   │   ├── shopee_scraper.py
│   │   └── base_scraper.py
│   │
│   ├── analyzers/               # Data analysis modules
│   │   ├── trend_analyzer.py
│   │   ├── price_analyzer.py
│   │   └── competitor_analyzer.py
│   │
│   ├── exporters/               # Export & reporting
│   │   ├── excel_exporter.py
│   │   ├── csv_exporter.py
│   │   └── dashboard_generator.py
│   │
│   ├── utils/                   # Utility functions
│   │   ├── config_loader.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   ├── drivers/                 # WebDriver files
│   │   └── chromedriver.exe
│   │
│   ├── main.py                  # Entry point utama
│   ├── scheduler.py             # Automated scheduling
│   ├── config.py                # Configuration settings
│   └── requirements.txt         # Python dependencies
│
├── data/                        # Data storage
│   ├── raw/                     # Raw scraped data
│   │   ├── tokopedia/
│   │   └── shopee/
│   │
│   ├── processed/               # Cleaned & processed data
│   │   ├── daily_summary/
│   │   ├── weekly_trends/
│   │   └── competitor_analysis/
│   │
│   └── database/                # Database files
│       └── products.db
│
├── output/                      # Generated reports & exports
│   ├── reports/                 # Automated reports
│   │   ├── daily/
│   │   ├── weekly/
│   │   └── monthly/
│   │
│   ├── charts/                  # Generated visualizations
│   │   ├── trends/
│   │   ├── comparisons/
│   │   └── dashboards/
│   │
│   └── exports/                 # Excel/CSV exports
│       ├── sold_qty_comparison.xlsx
│       ├── price_analysis.xlsx
│       └── competitor_report.xlsx
│
├── tests/                       # Unit tests
│   ├── test_scrapers.py
│   ├── test_analyzers.py
│   └── test_exporters.py
│
├── docs/                        # Documentation
│   ├── API.md
│   ├── SETUP.md
│   └── EXAMPLES.md
│
├── .gitignore
├── README.md
├── LICENSE
└── requirements.txt
```

## 🔧 Konfigurasi Lanjutan

### Environment Variables
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
export TWILIO_SID="your_twilio_sid"
export TWILIO_TOKEN="your_twilio_token"
```

### Cron Job Setup (Linux/Mac)
```bash
# Edit crontab
crontab -e

# Jalankan setiap 6 jam
0 */6 * * * /path/to/python /path/to/project/src/scheduler.py
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lengkap.

## ⚠️ Disclaimer

Proyek ini dibuat untuk tujuan edukasi dan penelitian. Pastikan untuk mematuhi ToS (Terms of Service) dari masing-masing platform. Gunakan dengan bijak dan bertanggung jawab.

---

**Happy Monitoring! 🚀📊**
