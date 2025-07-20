package com.example.cinemate.data

import com.example.cinemate.model.Movie

interface MovieRepository {
    suspend fun getMovies(): List<Movie>
}