<template>
  <div class="w3-container" style="height: 100%">
    <MovieForm type="update" :id="$route.params.id" :title=title @success="onUpdate" />
  </div>
</template>

<script>
import MovieForm from '@/components/MovieForm.vue'
import axios from 'axios';

export default {
    name: 'EditMovie',
    data() {
        return {
            title: ''
        }
    },
    methods: {
        onUpdate() {
            alert('Updated');
            this.$router.push('/');
        }
    },
    components: {
        MovieForm,
    },
    async mounted() {
        const response = await axios.get('http://127.0.0.1:8000/movielist/movies/'+this.$route.params.id);
        console.log(response.data);
        this.title = response.data[0].fields.title;
    }
}
</script>
