<template>
    <div class="w3-container w3-center">
        <h2><b>Movies</b></h2>
        <table class="w3-table movie-table w3-striped w3-bordered w3-hoverable">
            <thead>
                <tr class="w3-light-grey">
                    <td class="w3-center"><b>Title</b></td>
                    <td class="w3-center"><b>Likes</b></td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="movie in movies" :key="movie.pk">
                    <td class="w3-center">{{ movie.fields.title }}</td>
                    <td class="w3-center">{{ movie.fields.likes }}</td>
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
