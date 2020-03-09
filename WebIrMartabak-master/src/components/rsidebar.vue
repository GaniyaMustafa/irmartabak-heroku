<template>
  <div class="sidebar text-center p-0 bg-primary">
      <ul class="list-group">
          <a href="#" class="mdi mdi-instagram"></a>
          <a href="#" class="mdi mdi-facebook-box"></a>
          <a href="#" class="mdi mdi-youtube"></a>
          <a href="#" class="mdi mdi-twitter"></a>
      </ul>
      <a href="#aboutus">
        <div class="arrow container-fluid m-0 p-0">
          <i class="mdi mdi-arrow-down"></i>
        </div>
      </a>
    </div>
</template>

<script>
export default {
  name: "rsidebar",
  props: {
    msg: String
  }
};