require ('dotenv').config();
const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static('public'));

// Usar el index.html como página principal
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API endpoint para buscar películas
app.get('/api/movies', async (req, res) => {
  const query = req.query.q || ''; // Parámetro de búsqueda
  
  if (!query) {
    return res.json({ success: true, movies: [], total: 0 });
  }
  
  const url = `https://api.themoviedb.org/3/search/movie?query=${query}&include_adult=false&language=es-MX&page=1`;
  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${process.env.ANTHROPIC_API_KEY}`
    }
  };

  try {
    const response = await fetch(url, options);
    const data = await response.json();
    
    // Guardar en variable y enviar al cliente
    const movies = data.results || [];
    res.json({ success: true, movies: movies, total: data.total_results });
  } catch (error) {
    console.error('Error fetching movies:', error);
    res.status(500).json({ success: false, error: 'Error al obtener películas' });
  }
});

// Iniciar el servidors
const server = app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

server.on('error', (error) => {
  console.error('Error starting the server:', error);
});