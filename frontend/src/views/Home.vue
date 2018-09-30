<template>
  <div class="w3-container" style="height: 100%">
    <MovieTable class="mtable"></MovieTable>
    <button class="w3-button w3-round-large w3-border w3-right w3-blue" @click="addClicked">Add a Movie</button>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieTable from '@/components/MovieTable.vue'

export default {
  name: 'home',
  components: {
    MovieTable,
  },
  methods: {
    addClicked() {
      this.$router.push('/movie/add');
    }
  }
}
</script>

<style>
.mtable {
  height: 50%;
  overflow-y: auto;
}
</style>
