<template>
  <div class="w3-container">
    <MovieTable></MovieTable>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieTable from '@/components/MovieTable.vue'

export default {
  name: 'home',
  components: {
    MovieTable,
  }
}
</script>
