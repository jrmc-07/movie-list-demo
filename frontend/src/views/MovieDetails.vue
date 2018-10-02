<template>
    <div class="w3-container">
        <div class="w3-container w3-green">
            <h2>Movie Details</h2>
        </div>
        <div class="w3-container">
            <table class="w3-table">
                <tr>
                    <td>Id: </td>
                    <td>{{ movie.pk }}</td>
                </tr>
                <tr>
                    <td>Title: </td>
                    <td>{{ movie.fields.title }}</td>
                </tr>
                <tr>
                    <td>Likes: </td>
                    <td>{{ movie.fields.likes }}</td>
                </tr>
            </table>
        </div>
        <LikeButton :id=movie.pk @liked=getMovieDetails />
        <EditButton :id=movie.pk />
        <DeleteButton :id=movie.pk :title=movie.fields.title @deleted=onMovieDeleted />
    </div>
</template>

<script>
import axios from 'axios';
import LikeButton from '@/components/MovieLikeButton.vue';
import EditButton from '@/components/MovieEditButton.vue';
import DeleteButton from '@/components/MovieDeleteButton.vue';

export default {
    name: 'MovieDetails',
    components: {
        LikeButton,
        EditButton,
        DeleteButton,
    },
    data() {
        return {
            movie: {pk:0, fields:{title:'',likes:''}}
        }
    },
    methods: {
        async getMovieDetails() {
            const response = await axios.get('http://127.0.0.1:8000/movielist/movies/'+this.$route.params.id);
            this.movie = response.data[0];
        },
        onMovieDeleted() {
            this.$router.push('/');
        }
    },
    mounted() {
        this.getMovieDetails()
    }
}
</script>

