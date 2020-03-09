<template>
  <div class="contact" style="padding-top: 10rem">
    <h1>This is Contact page</h1>
    <ul>
      <li>Email: {{ email }}</li>
      <li>Phone Number: {{ nohp }}</li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Contact",
  data() {
    return {
      email: "shaddam.a.h@gmail.com",
      nohp: "085156386948"
    };
  }
};
</script>
