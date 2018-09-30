<template>
    <div class="w3-container w3-center">
        <h2><b>Movies</b></h2>
        <table class="w3-table movie-table w3-striped w3-bordered w3-hoverable">
            <thead>
                <tr class="w3-light-grey">
                    <td class="w3-center"><b>Title</b></td>
                    <td class="w3-center"><b>Likes</b></td>
                    <td class="w3-center"><b>Actions</b></td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="movie in movies" :key="movie.pk">
                    <td class="w3-center">{{ movie.fields.title }}</td>
                    <td class="w3-center">{{ movie.fields.likes }}</td>
                    <td class="w3-center">
                        <button class="w3-button w3-round-large w3-green" @click="likeMovie(movie.pk)">Like</button>
                        <button class="w3-button w3-round-large w3-blue">Edit</button>
                        <button class="w3-button w3-round-large w3-red" @click="deleteMovie(movie.pk)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'MovieTable',
    data() {
        return {
            movies: [],
        }
    },
    methods: {
        async getMovies() {
            const response = await axios.get('http://127.0.0.1:8000/movielist/movies');
            this.movies = response.data;
        },
        async likeMovie(id) {
            const response = await axios.get('http://127.0.0.1:8000/movielist/movies/'+id+'/like');
            this.getMovies();
        },
        async deleteMovie(id) {
            const response = await axios.delete('http://127.0.0.1:8000/movielist/movies/'+id);
            this.getMovies();
        }
    },
    mounted() {
        this.getMovies();
    }
}
</script>

<style>
.movie-table {
    margin-left: auto;
    margin-right: auto;
}
</style>
