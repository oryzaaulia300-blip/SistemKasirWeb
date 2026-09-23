from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Konfigurasi Database PostgreSQL
DB_HOST = "localhost"
DB_NAME = "SistemKasir"
DB_USER = "postgres"
DB_PASS = "Admin123" # Ganti dengan password asli Anda

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def index():
    # Membuka koneksi ke database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Mengambil semua data dari tabel barang
    cur.execute('SELECT nama, harga FROM barang ORDER BY id ASC;')
    daftar_barang = cur.fetchall()
    
    # Menutup koneksi
    cur.close()
    conn.close()
    
    # Mengirim data 'daftar_barang' ke file HTML
    return render_template('index.html', menu_barang=daftar_barang)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
