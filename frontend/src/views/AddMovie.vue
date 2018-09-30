<template>
  <div class="w3-container" style="height: 100%">
    <MovieForm type="create" @success="onCreate" />
  </div>
</template>

<script>
import MovieForm from '@/components/MovieForm.vue'

export default {
    name: 'AddMovie',
    methods: {
        onCreate() {
            alert('created');
            this.$router.push('/');
        }
    },
    components: {
        MovieForm,
    },
}
</script>
