<template>
  <div class="w3-container" style="height: 100%">
    <div class="w3-container">
      <h2 class="w3-left">{{ welcomeMessage }}</h2>
    </div>
    <MovieTable class="mtable"></MovieTable>
    <button class="w3-button w3-round-large w3-border w3-right w3-blue" @click="addClicked">Add a Movie</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import MovieTable from '@/components/MovieTable.vue'

export default {
  name: 'home',
  components: {
    MovieTable,
  },
  data() {
    return {
      last_access_time: '0',
    }
  },
  methods: {
    addClicked() {
      this.$router.push('/movie/add');
    },
    async sessionGet() {
      const response = await axios.get('http://127.0.0.1:8000/movielist/last_session', {withCredentials:true});
      this.last_access_time = response.data;
    }
  },
  computed: {
    welcomeMessage() {
      return this.last_access_time == '0' ? "Welcome to our site!" : "Welcome back! You've visited this page last " + this.last_access_time;
    }
  },
  mounted() {
    this.sessionGet();
  }
}
</script>

<style>
.mtable {
  height: 50%;
  overflow-y: auto;
}
</style>
