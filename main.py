import webview
import os
import json
import pandas as pd

class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def get_data(self):
        """Wczytuje dane z CSV i zwraca je jako postać JSON do JS"""
        csv_path = os.path.join(os.path.dirname(__file__), 'misc', 'data.csv')
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            # Agresywna zamiana NaN na None, aby zapobiec błędom SyntaxError w JS
            data = df.astype(object).where(pd.notnull(df), None).to_dict(orient='records')
            return data
        return []

def main():
    # Pobieranie ścieżki do pliku HTML
    html_path = os.path.join(os.path.dirname(__file__), 'tree.html')
    
    api = Api()
    
    # Tworzenie okna
    window = webview.create_window(
        'System Struktury Organizacyjnej', 
        html_path, 
        js_api=api,
        width=1200,
        height=800
    )
    
    api.set_window(window)
    
    # Uruchomienie aplikacji
    webview.start()

if __name__ == '__main__':
    main()
