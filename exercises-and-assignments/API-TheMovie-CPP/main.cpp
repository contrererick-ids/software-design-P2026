/**
*   Tarea: Consumir API - TheMovieDB
*   Equipo: Isaac Vazquez,
*           Erick Contreras
*
*   DEPENDENCIAS:
* - libcurl (sudo apt-get install libcurl4-openssl-dev)
* - nlohmann json (sudo apt-get install nlohmann-json3-dev)
*
*   COMPILAR:
*   g++ main.cpp -o movie_search -lcurl
*/
#include <iostream>
#include <string>
#include <vector>
#include <curl/curl.h>
#include <curl/easy.h>
#include <nlohmann/json.hpp>

// JSON Facilitator
using json = nlohmann::json;
using namespace std;

// Data Structure for Movies
struct Movie {
    std::string title;
    std::string release_date;
    std::string overview;
    double vote_average;
};

// API Class
class TMDBCLient {
private:
    std::string apiKey;
    std::string baseURL =  "https://api.themoviedb.org/3/search/movie";

    // Callback for libcurl to return string
    static std::size_t WriteCallBack(void* contents, std::size_t size, std::size_t nmemb, void* userp) {
        ((std::string*)userp)->append((char*)contents, size * nmemb);
        return size * nmemb;
    }

    // Auxiliar function for adding spaces on url -> %20
    std::string urlEncode(CURL* curl, std::string value){
        char* output = curl_easy_escape(curl, value.c_str(), value.length());
        std::string result(output);
        curl_free(output);
        return result;
    }

public:
    TMDBCLient(string key) : apiKey(key) {}

    vector<Movie> search(string query){
        vector<Movie> movies;
        CURL* curl;
        CURLcode res;
        string readBuffer;

        curl = curl_easy_init();
        if(curl){
            // 1. Build URL
            std::string encodeQuery = urlEncode(curl, query);
            std::string url = baseURL + "?query=" + encodeQuery + "&include_adult=false&language=en-US&page=1";

            // 2. Configure headers
            struct curl_slist *headers = NULL;
            std::string authHeader = "Authorization: Bearer " + apiKey;
            headers = curl_slist_append(headers, authHeader.c_str());
            headers = curl_slist_append(headers, "accept: application/json");

            // 3. Configure CURL
            curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallBack);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

            // 4. Send Request
            res = curl_easy_perform(curl);

            if(res != CURLE_OK){
                std::cerr << "Error in the request:" <<curl_easy_strerror(res) << std::endl;
            } else {
                try{
                    // 5. Parse JSON
                    auto jsonResponse = json::parse(readBuffer);

                    for(const auto& item : jsonResponse["results"]){
                        Movie m;
                        m.title = item.value("title", "No title");
                        m.release_date = item.value("release_date", "Unknown");
                        m.overview = item.value("overview", " No description");
                        m.vote_average = item.value("vote_average", 0.0);
                        movies.push_back(m);
                    }
                } catch (json::parse_error& e){
                    std::cerr << "Error parsing Json: " << e.what() << std::endl;
                }
            }
        // Clean URL and headers
        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);
    }
    return movies;
  }
};

// User Interface
int main() {
    std::string TOKEN = "";

    TMDBCLient client(TOKEN);
    std::string inputTitle;

    while(true){
        std::cout << "-----------------------------------------" << std::endl;
        std::cout << "|            Search a Movie             |" << std::endl;
        std::cout << "-----------------------------------------" << std::endl;
        std::cout << "Enter the Movie name or type 'exit': ";
        getline(cin, inputTitle);

        if (inputTitle == "exit") break;

        std::cout << "Searching '" << inputTitle << "'..." << std::endl;

        std::vector<Movie> res = client.search(inputTitle);

        if(res.empty()){
            std::cout << "No movies found" << std::endl;\
        } else {
            std::cout << "\n--- Results:" << res.size() << "---\n";
            for (const auto& m : res){
                std::cout << "[" << m.release_date << "] " << m.title
                          << " (Rating: " << m.vote_average << "/10" << std::endl;
                std::cout << "Overview: " << m.overview.substr(0, 100) << "..." << std::endl;
                std::cout << "-----------------------------------------" << std::endl;
            }
        }
        std::cout << "\n";
    }

    return 0;
}