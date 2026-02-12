// Variables globales para almacenar las películas
let moviesData = [];

// Elementos del DOM
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const moviesContainer = document.getElementById('movies-container');
const loadingElement = document.getElementById('loading');
const resultsCount = document.getElementById('results-count');

// Función para buscar películas
async function searchMovies(query) {
  if (!query || query.trim() === '') {
    showWelcome();
    return;
  }

  // Mostrar loading
  loadingElement.classList.add('active');
  moviesContainer.innerHTML = '';
  resultsCount.textContent = '';

  try {
    const response = await fetch(`/api/movies?q=${encodeURIComponent(query)}`);
    const data = await response.json();

    if (data.success) {
      // Guardar en la variable global
      moviesData = data.movies;
      
      // Mostrar resultados
      if (moviesData.length > 0) {
        displayMovies(moviesData);
        resultsCount.textContent = `✨ Se encontraron ${data.total} resultados para "${query}"`;
      } else {
        showNoResults(query);
      }
      
      // También puedes imprimir en consola
      console.log('Películas encontradas:', moviesData);
    } else {
      showNoResults(query);
    }
  } catch (error) {
    console.error('Error:', error);
    showError();
  } finally {
    loadingElement.classList.remove('active');
  }
}

// Función para mostrar las películas en el HTML
function displayMovies(movies) {
  moviesContainer.innerHTML = movies.map((movie, index) => {
    const posterUrl = movie.poster_path 
      ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
      : 'https://placehold.co/600x400?text=test';
    
    const rating = movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A';
    const releaseYear = movie.release_date ? movie.release_date.split('-')[0] : 'N/A';

    return `
      <div class="movie-card" data-id="${movie.id}" style="animation-delay: ${index * 0.05}s">
        <img src="${posterUrl}" alt="${movie.title}" class="movie-poster" loading="lazy">
        <div class="movie-info">
          <h3 class="movie-title">${movie.title}</h3>
          <div class="movie-meta">
            <span class="movie-rating">⭐ ${rating}</span>
            <span class="movie-date">${releaseYear}</span>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Función para mostrar mensaje de bienvenida
function showWelcome() {
  moviesContainer.innerHTML = `
    <div class="welcome-message">
      <div class="welcome-icon">🍿</div>
      <h2>¡Bienvenido!</h2>
      <p>Escribe el nombre de una película en el buscador para comenzar</p>
    </div>
  `;
  resultsCount.textContent = '';
}

// Función para mostrar mensaje de sin resultados
function showNoResults(query) {
  moviesContainer.innerHTML = `
    <div class="no-results">
      <p>No se encontraron películas para "<strong>${query}</strong>"</p>
      <p style="font-size: 1rem; margin-top: 15px; opacity: 0.9;">Intenta con otro término de búsqueda</p>
    </div>
  `;
  resultsCount.textContent = '';
}

// Función para mostrar error
function showError() {
  moviesContainer.innerHTML = `
    <div class="no-results">
      <p>Error al cargar las películas</p>
      <p style="font-size: 1rem; margin-top: 15px; opacity: 0.9;">Por favor, intenta de nuevo más tarde</p>
    </div>
  `;
  resultsCount.textContent = '';
}

// Event listener para el botón de búsqueda
searchBtn.addEventListener('click', () => {
  const query = searchInput.value.trim();
  searchMovies(query);
});

// Event listener para presionar Enter en el input
searchInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    const query = searchInput.value.trim();
    searchMovies(query);
  }
});

// Mostrar mensaje de bienvenida al cargar
showWelcome();