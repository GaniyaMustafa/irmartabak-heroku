import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import VueCarousel from "vue-carousel";
import VueAxios from '../components/plugins/axios';

Vue.use(VueCarousel);
Vue.use(VueRouter);
Vue.use(VueAxios);

const routes = [
  {
    path: "/",
    name: "Home",
    meta: { hideDesktop: false },
    component: Home
  },
  {
    path: "/social",
    name: "Social",
    meta: { hideDesktop: true },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Social.vue")
  },
  {
    path: "/contact",
    name: "Contact",
    meta: { hideDesktop: true },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Contact.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
