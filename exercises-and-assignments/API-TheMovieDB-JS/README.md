# 🎬 Movie Search Web App -- TMDB Integration

A full-stack movie search application built with **Node.js** and
**Vanilla JavaScript**, powered by The Movie Database (TMDB) API.

This project demonstrates backend API proxying, secure environment
variable handling, asynchronous frontend rendering, and clean
client--server architecture.

------------------------------------------------------------------------

## 🌟 Overview

This web application allows users to search for movies dynamically and
display results including:

-   🎥 Movie Poster\
-   ⭐ Rating\
-   📅 Release Year

The frontend communicates with a custom backend endpoint
(`/api/movies`), which securely integrates with the TMDB API using
environment variables.

The backend acts as a **proxy layer**, preventing exposure of the API
key in the frontend.

------------------------------------------------------------------------

## 🏗 Architecture

Client (Browser)\
⬇\
Node.js Server (`/api/movies`)\
⬇\
TMDB External API

------------------------------------------------------------------------

## 🚀 Features

-   🔎 Search movies by title
-   🎬 Dynamic movie cards rendering
-   ⚡ Real-time search interaction
-   🔐 API key secured with `dotenv`
-   ⌨️ Search via button or Enter key
-   🎨 Loading state animation
-   ❌ Graceful error handling
-   📱 Responsive layout

------------------------------------------------------------------------

## 🛠 Tech Stack

### Backend

-   Node.js
-   CommonJS
-   dotenv

### Frontend

-   HTML5
-   CSS3
-   Vanilla JavaScript (ES6+)
-   Fetch API
-   DOM Manipulation

### External API

-   The Movie Database (TMDB)

------------------------------------------------------------------------

## 📦 Installation

``` bash
git clone https://github.com/your-username/api-themoviedb.git
cd api-themoviedb
npm install
```

------------------------------------------------------------------------

## 🔐 Environment Configuration

Create a `.env` file in the root directory:

    TMDB_API_KEY=your_api_key_here

You can obtain an API key from: https://www.themoviedb.org/settings/api

------------------------------------------------------------------------

## ▶️ Run the Project

``` bash
npm start
```

This executes:

    node server.js

Then open:

    http://localhost:PORT

*(Replace PORT with your configured server port.)*

------------------------------------------------------------------------

## 📁 Project Structure

    api-themoviedb/
    │
    ├── server.js          # Backend server
    ├── package.json
    ├── .env
    │
    ├── public/
    │   ├── index.html     # Main UI
    │   ├── styles.css
    │   └── app.js         # Frontend logic

------------------------------------------------------------------------

## 🔍 Example Backend Response

``` json
{
  "success": true,
  "total": 3,
  "movies": [
    {
      "id": 27205,
      "title": "Inception",
      "poster_path": "/poster.jpg",
      "vote_average": 8.8,
      "release_date": "2010-07-16"
    }
  ]
}
```

------------------------------------------------------------------------

## 💡 What This Project Demonstrates

-   REST API consumption
-   Backend proxy pattern
-   Environment variable security
-   Asynchronous programming (`async/await`)
-   Dynamic DOM rendering
-   Clean separation of concerns

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Implement Express.js routing
-   Add pagination
-   Add movie detail page
-   Add genre filters
-   Deploy to cloud (Render / Railway)
-   Add caching
-   Add unit testing

------------------------------------------------------------------------

## 👨‍💻 Author

Developed as a personal portfolio project to showcase full-stack
development skills and API integration expertise.
