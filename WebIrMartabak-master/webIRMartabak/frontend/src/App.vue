<template>
  <div id="app">
    <rsidebar
      v-bind:class="{ hidedesktop: $route.meta.hideDesktop }"
    ></rsidebar>
    <div class="navigation">
      <navbar></navbar>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
  @import "./assets/css/main.css";
</style>

<script>
// @ is an alias to /src
import navbar from "./components/navbar.vue";
import rsidebar from "./components/rsidebar.vue";

export default {
  name: "Home",
  components: {
    navbar,
    rsidebar
  }
};
</script>
