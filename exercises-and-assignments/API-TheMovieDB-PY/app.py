from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Ruta principal - servir el HTML
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint para buscar películas
@app.route('/api/movies')
def search_movies():
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({'success': True, 'movies': [], 'total': 0})
    
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=es-MX&page=1"
    headers = {
        'accept': 'application/json',
        'Authorization': f"Bearer {os.getenv('TMDB_API_KEY')}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        movies = data.get('results', [])
        return jsonify({
            'success': True, 
            'movies': movies, 
            'total': data.get('total_results', 0)
        })
    except Exception as error:
        print(f'Error fetching movies: {error}')
        return jsonify({'success': False, 'error': 'Error al obtener películas'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
