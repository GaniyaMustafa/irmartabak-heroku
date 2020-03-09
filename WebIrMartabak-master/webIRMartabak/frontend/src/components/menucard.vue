<template>
  <div class="card mx-2">
    <img
      class="card-img-top img-fluid fit-cover"
      src="static/img/martabak.jpg"
      alt="Card image cap"
    />
    <div class="card-img-overlay">
      <div class="rating h4 text-dark">
        <i class="mdi mdi-star" v-bind:key="i" v-for="i in rating"></i>
      </div>
      <p class="lead2">{{ nama }}</p>
      <h1 class="display-4">{{ harga }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "menucard",
  props: {
    rating: Number,
    nama: String,
    harga: String
  }
};
</script>
