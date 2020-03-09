<template>
  <div class="card p-0 border-none">
    <img
      class="card-img-top img-fluid fit-cover"
      src="static/img/stand.jpg"
      alt="Card image cap"
    />
    <div class="card-img-overlay2 row m-0 my-auto">
      <div class="my-auto m-3">
      <img src="static/img/profile.png" class="round" srcset="">
      </div>
      <div class="col my-auto">
      <p>{{ comment }} <b>#insinyur_martabak #ir_martabak_moment</b></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "comment",
  props: {
    comment: String,
  }
};
</script>
