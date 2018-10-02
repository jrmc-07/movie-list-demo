<template>
    <button class="w3-button w3-round-large w3-orange" @click=routeToEdit>Edit</button>
</template>

<script>

export default {
    name: 'MovieEditButton',
    props: ['id'],
    methods: {
        routeToEdit() {
            this.$router.push('/movie/'+this.id+'/edit');
        }
    },
}
</script>
