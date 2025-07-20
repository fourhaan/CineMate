package com.example.cinemate.data.remote

import com.example.cinemate.data.MovieApiService
import com.google.gson.Gson
import com.google.gson.GsonBuilder
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance {
    val api: MovieApiService by lazy {
        Retrofit.Builder()
            .baseUrl("https://k3k0j11z-8000.inc1.devtunnels.ms/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(MovieApiService::class.java)
    }
}