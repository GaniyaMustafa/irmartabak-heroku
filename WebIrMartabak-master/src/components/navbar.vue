<template>
  <nav class="navbar navbar-expand-md navbar-light bg-white py-4 pl-5">
    <a class="navbar-brand pb-sm-3 pb-md-0" href="#">
      <img height="60" src="@/assets/img/logo.png" />
    </a>
    <button
      class="navbar-toggler float-left"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link exact to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            Menu
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="#">Asin</a>
            <a class="dropdown-item" href="#">Manis</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#"> Top Seller</a>
          </div>
        </li>
        <li class="nav-item">
          <router-link to="/Social" class="nav-link">Social</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/Contact" class="nav-link">Contact</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "navbar",
  props: {
    msg: String
  }
};
</script>
