package com.example.cinemate.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cinemate.data.MovieRepository
import com.example.cinemate.model.Movie
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class MovieListViewModel(private val repository: MovieRepository) : ViewModel() {
    private val _movies = MutableStateFlow<List<Movie>>(emptyList())
    val movies: StateFlow<List<Movie>> = _movies
    init {
        fetchMovies()
    }
    private fun fetchMovies(){
        viewModelScope.launch {
            _movies.value = repository.getMovies()
        }
    }
}