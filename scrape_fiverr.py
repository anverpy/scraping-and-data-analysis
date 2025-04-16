import pyperclip
import tkinter as tk
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# Variables para almacenar los gigs
all_gigs = []
page_counter = 1  # Empezamos con la primera página

# Función para extraer gigs del HTML copiado
def extract_gigs_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    gigs = soup.select("div.basic-gig-card")
    print(f"🔍 Gigs encontrados en este lote: {len(gigs)}")
    data = []

    for gig in gigs:
        title = gig.select_one("p[role='heading']")
        seller = gig.select_one("a.text-bold")
        rating = gig.select_one("strong.rating-score")
        reviews = gig.select_one("span.rating-count-number")
        price_tag = gig.select_one("span.text-bold.co-grey-1200")
        level_tag = gig.select_one("p.z58z872")

        has_video_consult = "video consultation" in gig.text.lower()

        raw_price = price_tag.text if price_tag else None
        price_cleaned = None
        if raw_price:
            match = re.search(r'[\d.,]+', raw_price)
            price_cleaned = match.group() if match else raw_price

        data.append({
            "title": title.text.strip() if title else None,
            "seller": seller.text.strip() if seller else None,
            "rating": rating.text.strip() if rating else None,
            "reviews": reviews.text.strip() if reviews else None,
            "price": price_cleaned,
            "seller_level": level_tag.text.strip() if level_tag else None,
            "video_consultation": has_video_consult
        })
    return data

# Función para capturar los datos del portapapeles cuando presionas el botón
def capture_data():
    global page_counter
    print(f"\n💾 Capturando datos de la página {page_counter}...")
    html = pyperclip.paste()
    lote = extract_gigs_from_html(html)

    # Eliminar duplicados SOLO dentro del lote actual
    df_lote = pd.DataFrame(lote)
    lote_filtrado = df_lote.drop_duplicates().to_dict(orient="records")

    all_gigs.extend(lote_filtrado)
    print(f"✅ Guardados {len(lote_filtrado)} gigs en esta iteración. Total acumulado: {len(all_gigs)}")
    print(f"📄 Página {page_counter} almacenada.")

    page_counter += 1  # Incrementa el contador de páginas
    capture_button.config(text=f"💾 Página {page_counter}")  # Cambiar texto del botón dinámicamente

# Función para terminar y guardar el CSV
def save_and_quit():
    if not all_gigs:
        print("❌ No hay datos para guardar.")
        return
    
    # Guardar los datos en el CSV
    file_name = file_name_entry.get()
    if not file_name:
        file_name = "fiverr_gigs"  # Nombre predeterminado si no se ingresa
    df = pd.DataFrame(all_gigs)
    df.to_csv(f"{file_name}.csv", index=False)
    print(f"✅ Archivo guardado como {file_name}.csv")
    root.quit()  # Cierra la interfaz gráfica

# Crear la ventana principal
root = tk.Tk()
root.title("Capturar Gigs de Fiverr")

# Hacer que la ventana siempre esté por encima
root.attributes("-topmost", 1)
root.lift()

# Cambiar el color de fondo y el color del texto
root.configure(bg='#000000')  # Fondo negro
root.geometry("400x400")  # Tamaño ajustado para la interfaz

# Pedir nombre del archivo al principio
file_name_label = tk.Label(root, text="Name CSV:", font=("Consolas", 16), fg="#00FFFF", bg="#000000")
file_name_label.pack(pady=5)

file_name_entry = tk.Entry(root, width=40, font=("Consolas", 16), fg="#00FFFF", bg="#000000", insertbackground="white")
file_name_entry.pack(pady=5)

# Crear los botones con separación y fuente Consolas
capture_button = tk.Button(root, text="💾 Save P1", command=capture_data, height=2, width=20, font=("Consolas", 16), fg="#00FFFF", bg="#000000")
capture_button.pack(pady=10, fill='both', expand=True)  # El botón ahora se adapta dinámicamente

finish_button = tk.Button(root, text="🚪", command=save_and_quit, height=2, width=20, font=("Consolas", 16), fg="#00FFFF", bg="#000000")
finish_button.pack(pady=10)

# Iniciar la ventana
root.mainloop()