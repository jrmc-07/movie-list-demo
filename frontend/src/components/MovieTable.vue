<template>
    <div class="w3-container w3-center">
        <h3>Movies</h3>
        <table class="w3-table movie-table">
            <thead>
                <td class="w3-center"><b>Title</b></td>
                <td class="w3-center"><b>Actions</b></td>
            </thead>
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
    width: 50%;
    margin-left: auto;
    margin-right: auto;
}
</style>
