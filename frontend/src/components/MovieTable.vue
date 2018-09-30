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
                        <LikeButton :id=movie.pk @liked="getMovies"/>
                        <button class="w3-button w3-round-large w3-blue" @click="viewClicked(movie.pk)">View</button>
                        <button class="w3-button w3-round-large w3-orange" @click=editClicked(movie.pk)>Edit</button>
                        <DeleteButton :id=movie.pk :title=movie.fields.title @deleted="getMovies" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import LikeButton from '@/components/MovieLikeButton.vue';
import DeleteButton from '@/components/MovieDeleteButton.vue';

export default {
    name: 'MovieTable',
    components: {
        LikeButton,
        DeleteButton,
    },
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
        editClicked(id) {
        },
        viewClicked(id) {
            this.$router.push('/movie/'+id);
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
