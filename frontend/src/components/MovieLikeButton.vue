<template>
    <button class="w3-button w3-round-large w3-green" @click="likeMovie">Like</button>
</template>

<script>
import axios from 'axios';

export default {
    name: 'MovieLikeButton',
    props: ['id'],
    methods: {
        async likeMovie() {
            const response = await axios.get('http://127.0.0.1:8000/movielist/movies/'+this.id+'/like');
            this.$emit('liked');
        },
    },
}
</script>
