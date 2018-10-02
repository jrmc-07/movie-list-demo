import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import EditMovie from './views/EditMovie.vue'
import AddMovie from './views/AddMovie.vue'
import MovieDetails from './views/MovieDetails.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/movie/add',
      name: 'AddMovie',
      component: AddMovie,
    },
    {
      path: '/movie/:id',
      name: 'MovieDetails',
      component: MovieDetails,
      props: true
    },
    {
      path: '/movie/:id/edit',
      name: 'EditMovie',
      component: EditMovie,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
