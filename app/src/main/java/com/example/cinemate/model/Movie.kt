package com.example.cinemate.model

data class Movie(
    val id: String,
    val title: String,
    val posterUrl: String,
    val synopsis: String,
    val genres: List<String>,
    val rating: Double
)
