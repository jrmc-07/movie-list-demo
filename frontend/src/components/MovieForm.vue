<template>
    <div class="w3-card-4">
        <div class="w3-container w3-green">
            <h2 class="w3-left">{{ header }}</h2>
        </div>
        <form @submit.prevent="">
            <label class="w3-left">Title</label>
            <input class="w3-input w3-border" v-model="movie_title" type="text" placeholder="Enter title..." required>
            <button class="w3-button w3-round-large w3-blue w3-right" @click="onSubmit">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'MovieForm',
    props: [ 'type', 'title', 'id' ],
    data() {
        return {
            movie_title: '',
        }
    },
    computed: {
        header() {
            if (this.type == "create") { return "Add New Movie"; }
            else if (this.type == "update") { return "Update Movie"; }
        },
        link() {
            if (this.type == "create") { return "http://127.0.0.1:8000/movielist/movies"; }
            else if (this.type == "update") { return "http://127.0.0.1:8000/movielist/movies/"+this.id; }
        },
        http_req_method() {
            if (this.type == "create") { return "post"; }
            else if (this.type == "update") { return "put"; }
        }
    },
    methods: {
        async onSubmit() {
            const response = await axios({
                method: this.http_req_method,
                url: this.link,
                data: {
                    title: this.movie_title,
                }
            });
            this.$emit('success');
        }
    },
    watch: {
        title(val) {
            this.movie_title = val;
        }
    },
    mounted() {
        if (this.type == "update") {
            this.movie_title = this.title;
        }
    }
}
</script>

