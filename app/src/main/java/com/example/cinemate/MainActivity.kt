package com.example.cinemate

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.cinemate.data.MovieRepositoryImpl
import com.example.cinemate.data.remote.RetrofitInstance
import com.example.cinemate.screens.MovieListScreen
import com.example.cinemate.ui.theme.CinemateTheme
import com.example.cinemate.viewmodel.MovieListViewModel
import com.example.cinemate.viewmodel.MovieListViewModelFactory

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val repository = MovieRepositoryImpl(RetrofitInstance.api)
        val factory = MovieListViewModelFactory(repository)
        setContent {
            val viewModel: MovieListViewModel = viewModel(factory = factory)
            MovieListScreen(viewModel)
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    CinemateTheme {
        Greeting("Android")
    }
}