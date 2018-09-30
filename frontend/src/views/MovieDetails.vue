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
        <LikeButton />
        <DeleteButton />
    </div>
</template>

<script>
import axios from 'axios';
import LikeButton from '@/components/MovieLikeButton.vue';
import DeleteButton from '@/components/MovieDeleteButton.vue';

export default {
    name: 'MovieDetails',
    components: {
        LikeButton,
        DeleteButton,
    },
    data() {
        return {
            movie: {pk:0, fields:{title:'',likes:''}}
        }
    },
    async mounted() {
        const response = await axios.get('http://127.0.0.1:8000/movielist/movies/'+this.$route.params.id);
        this.movie = response.data[0];
    }
}
</script>

