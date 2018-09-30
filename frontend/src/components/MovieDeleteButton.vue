<template>
    <button class="w3-button w3-round-large w3-red" @click="deleteMovie">Delete</button>
</template>

<script>
import axios from 'axios';

export default {
    name: 'MovieLikeButton',
    props: ['id', 'title'],
    methods: {
        async deleteMovie(id, title) {
            if (confirm("Are you sure you want to delete this movie - " + this.title + "?")) {
                const response = await axios.delete('http://127.0.0.1:8000/movielist/movies/'+this.id);
                this.$emit('deleted');
            }
        }
    },
}
</script>
