package com.example.cinemate.screens

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.cinemate.model.Movie
import androidx.lifecycle.viewmodel.compose.viewModel
import coil.compose.AsyncImage
import com.example.cinemate.viewmodel.MovieListViewModel

@Composable
fun MovieListScreen(viewModel: MovieListViewModel = viewModel()) {
    val movies by viewModel.movies.collectAsState()
    LazyColumn(
        contentPadding = PaddingValues(16.dp)
    ) {
        items(movies) { movie: Movie ->
            Column(modifier = Modifier.padding(vertical = 8.dp)) {
                Text(movie.title)
                AsyncImage(
                    model = movie.posterUrl,
                    contentDescription = "${movie.title} poster",
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(220.dp)
                )
            }
        }
    }
}