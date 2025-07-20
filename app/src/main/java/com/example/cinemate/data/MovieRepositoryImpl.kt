package com.example.cinemate.data

import com.example.cinemate.model.Movie

class MovieRepositoryImpl(private val api: MovieApiService): MovieRepository {
    override suspend fun getMovies(): List<Movie> = api.getMovies()
}