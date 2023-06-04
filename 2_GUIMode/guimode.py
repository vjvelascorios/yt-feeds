# GUI mode
import tkinter as tk
from tkinter import ttk
import requests
import re
import pandas as pd
from tkinter import filedialog

def obtener_info_canales_youtube():
    urls = entrada_urls.get("1.0", tk.END).splitlines()
    data = []
    
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            original_url = url
            match = re.search(r'type="application/rss\+xml" title="RSS" href="(.+?)"', response.text)
            if match:
                rss_url = match.group(1)
                data.append({'originalUrl': original_url, 'rssUrl': rss_url})
            else:
                data.append({'originalUrl': original_url, 'rssUrl': ''})
        else:
            data.append({'originalUrl': url, 'rssUrl': ''})
    
    dataframe = pd.DataFrame(data)
    resultado_text.configure(state="normal")
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, dataframe.to_string(index=False))
    resultado_text.configure(state="disabled")
    
    return dataframe

def exportar_completo():
    dataframe = obtener_info_canales_youtube()
    
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt")])
    if archivo:
        if archivo.endswith(".csv"):
            dataframe.to_csv(archivo, index=False)
        elif archivo.endswith(".txt"):
            dataframe.to_csv(archivo, index=False, sep="\t")
        else:
            tk.messagebox.showerror("Error", "Formato de archivo no válido.")
    else:
        tk.messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def exportar_rss():
    dataframe = obtener_info_canales_youtube()
    rss_urls = dataframe['rssUrl']
    
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if archivo:
        with open(archivo, "w") as f:
            for url in rss_urls:
                f.write(url + "\n")
        tk.messagebox.showinfo("Éxito", "Exportación de RSS completada.")
    else:
        tk.messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

def importar_canales():
    archivo = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if archivo:
        with open(archivo, "r") as f:
            urls = f.readlines()
        entrada_urls.delete("1.0", tk.END)
        entrada_urls.insert(tk.END, "\n".join(urls))

def limpiar_resultado():
    resultado_text.configure(state="normal")
    resultado_text.delete("1.0", tk.END)
    resultado_text.configure(state="disabled")

    
# GUI
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Get RSS feeds from YT channels")
ventana.geometry("400x400")
ventana.configure(bg="white")

# Estilos
style = ttk.Style()
style.configure("TButton", background="gray", foreground="white")
style.configure("TLabel", background="gray", foreground="white")

# Marco de importación
importar_frame = ttk.Frame(ventana)
importar_frame.pack(pady=10)

importar_btn = ttk.Button(importar_frame, text="Import txt file", command=importar_canales)
importar_btn.pack(side="left", padx=5)

# Marco de entrada de URLs
url_frame = ttk.Frame(ventana)
url_frame.pack(pady=10)

url_label = ttk.Label(url_frame, text="URLs of YT channels:")
url_label.pack(side="left")

entrada_urls = tk.Text(url_frame, height=10, width=40)
entrada_urls.pack(side="left")

# Botón para obtener la información
obtener_btn = ttk.Button(ventana, text="Get links", command=obtener_info_canales_youtube)
obtener_btn.pack(pady=10)

# Marco de resultado
resultado_frame = ttk.Frame(ventana)
resultado_frame.pack()

resultado_label = ttk.Label(resultado_frame, text="Results:")
resultado_label.pack(pady=5)

resultado_text = tk.Text(resultado_frame, height=10, width=40, state="disabled")
resultado_text.pack()

# Marco de botones
botones_frame = ttk.Frame(ventana)
botones_frame.pack(pady=10)

# Botón para exportar completo
exportar_completo_btn = ttk.Button(botones_frame, text="Export all data", command=exportar_completo)
exportar_completo_btn.pack(side="left", padx=5)

# Botón para exportar RSS
exportar_rss_btn = ttk.Button(botones_frame, text="Export RSS links", command=exportar_rss)
exportar_rss_btn.pack(side="left", padx=5)

# Botón para limpiar resultado
limpiar_btn = ttk.Button(botones_frame, text="Clean", command=limpiar_resultado)
limpiar_btn.pack(side="left", padx=5)

# Ejecutar ventana
ventana.mainloop()

