package com.example.cinemate.data
import com.example.cinemate.model.Movie
import retrofit2.http.GET

interface MovieApiService {
    @GET("movies")
    suspend fun getMovies() : List<Movie>
}