<template>
  <div class="home">
    <section id="landing">
      <carousel
        :autoplay="true"
        :autoplayTimeout="3000"
        :scrollPerPage="false"
        :perPage="1"
        :paginationEnabled="false"
        :navigationEnabled="false"
        :loop="true"
      >
        <slide v-bind:key="i" v-for="martabak in martabakhome">
          <div class="container-fluid row p-0 m-0">
            <div class="col-md-6 p-0 my-auto">
              <div
                class="jumbotron-fluid bg-white m-3 m-md-5 pr-0 pr-md-5 m-md-0 ml-0 ml-md-5 pl-0 pl-md-5"
              >
                <p class="lead">{{martabak.name}}</p>
                <div class="rating h4">
                  <i class="mdi mdi-star" v-bind:key="i" v-for="i in martabak.rating"></i>
                </div>
                <h1 class="display-3 mb-5 price">{{martabak.price}}</h1>
                <p class="lead">
                  <a
                    class="btn btn-primary btn-lg px-5 py-3 mt-3 mb-5"
                    href="#"
                    role="button"
                    >Pesan Sekarang</a
                  >
                </p>
              </div>
            </div>
            <div class="col-md-6 col-sm-12 p-0">
              <img
                class="img-fluid fit-cover h-auto"
                :src=martabak.image
              />
            </div>
          </div>
        </slide>
      </carousel>
    </section>
    <section id="aboutus">
      <div
        class="container-fluid row align-items-center p-0 m-0 position-relative"
      >
        <div class="col-md-5 col-sm-12 p-0 ">
          <img class="w-100 martabak" src="static/img/stand.jpg" alt="" />
        </div>
        <div class="col-md-8 p-0 my-auto aboutus">
          <h1 class="text-center display-4 my-5">Tentang Kami</h1>
          <div class="jumbotron-fluid bg-primary px-5 pt-5 pb-0">
            <h1 class="display-5 mb-5 mt-5">The Professional Martabak Maker</h1>
            <p class="lead2">
              Insinyur martabak adalah sebuah Restoran berkonsep open kitchen
              yang menyajikan martabak dengan menu yang lengkap mulai dari
              martabak yang umum seperti martabak telor dan martabak coklat,
              sampai yang sedang trending saat ini seperti Red Velvet dan
              Matcha.
            </p>
            <p class="lead">
              <button
                data-toggle="modal" data-target="#exampleModalCenter"
                class="btn btn-dark btn-lg px-5 py-3 mt-5"  
                role="button"
                >Baca Selengkapnya</button
              >
            </p>
            <!-- Modal -->
            <div class="modal fade bd-example-modal-lg" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
              <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
                <div class="modal-content bg-primary pt-3 px-3 pb-0">
                  <div class="modal-header">
                    <h5 class="display-5 modal-title" id="exampleModalLongTitle">The Professional Martabak Maker</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body border-none">
                    <p class="lead2">
                    Insinyur martabak adalah sebuah brand martabak yang didirikan oleh para ahli dalam bidangnya. Dengan konsep proyek open kitchen yang menyajikan berbagai varian martabak  manis dan martabak telur. Berdiri sejak tahun 2017  hingga kini telah melebarkan sayap hingga empat cabang yang tersebar di Kota Bandung. Insinyur Martabak menyediakan  menu yang lengkap mulai dari martabak klasik hingga martabak dengan inovasi yang modern dan kekinian. Dengan konsep yang unik dan rasa produk yang spesial serta selalu terjaga kualitasnya, Insinyur Martabak selalu digemari oleh para pecinta martabak yang pastinya telah mendapat tempat spesial  di hati para pelanggannya. 
                    </p>
                  </div>
                  <div class="modal-footer p-0 pr-5">
                    <button type="button" class="btn btn-dark btn-lg px-5 py-3 mt-5" data-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-3 py-md-5" id="favorite">
      <div class="container-fluid row p-0 m-0 mx-auto">
        <div class="col-md-12 p-0">
          <h1 class="text-center display-4 my-5">Menu Paling Populer</h1>
        </div>
      </div>
      <div class="container-fluid row p-0 m-0 mx-auto">
        <div class="col-md-8 col-sm-12 p-0 mx-auto mb-5 pb-5">
          <carousel
            :autoplay="true"
            :scrollPerPage="false"
            :perPageCustom="[
              [968, 2],
              [1080, 3]
            ]"
            :navigationEnabled="true"
            :paginationEnabled="false"
            :loop="true"
          >
            <slide v-bind:key="i" v-for="i in 9">
              <menucard
                harga="Rp 60.000"
                nama="Martabak Sapi Super Mozarella"
                v-bind:rating="4"
              />
            </slide>
          </carousel>
        </div>
      </div>
    </section>
    <section id="map">
      <div class="container-fluid row p-0 m-0">
        <div class="col-md-6 col-sm-12 p-0">
          <h1 class="text-center display-4 my-3">Temukan Kami Di</h1>
          <div class="col-md-10 col-sm-12 float-right p-0">
            <div class="map-point">
              <div class="container bg-light"
                @click="src_cabang = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126744.20115044081!2d107.50106452753097!3d-6.919712449868398!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e68e9c9deb18173%3A0xa322ce9752833d6e!2sINSINYUR%20MARTABAK%20(Cab.%20Cibaduyut)Tci!5e0!3m2!1sid!2sid!4v1583329833260!5m2!1sid!2sid';
                active1=true;
                active2=false;
                active3=false;
                active4=false;"
                v-bind:class="{ active: active1 }">
                
                <p class="lead3">Kiaracondong</p>
                <p>Jl. Babakan Sari no 115 Kiaracondong, Bandung</p>
                <p class="lead3 float-right bg-white px-3 py-2">
                  Buka 14.00 - 23.00
                </p>
              </div>
              <div class="container bg-light"
                @click="src_cabang = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126744.20115044081!2d107.50106452753097!3d-6.919712449868398!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e68e9c9deb18173%3A0xa322ce9752833d6e!2sINSINYUR%20MARTABAK%20(Cab.%20Cibaduyut)Tci!5e0!3m2!1sid!2sid!4v1583329833260!5m2!1sid!2sid';
                active2=true;
                active1=false;
                active3=false;
                active4=false;"
                v-bind:class="{ active: active2 }">

                <p class="lead3">Kiaracondong</p>
                <p>Jl. Babakan Sari no 115 Kiaracondong, Bandung</p>
                <p class="lead3 float-right bg-white px-3 py-2">
                  Buka 14.00 - 23.00
                </p>
              </div>
              <div class="container bg-light"
                @click="src_cabang = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126744.20115044081!2d107.50106452753097!3d-6.919712449868398!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e68e9c9deb18173%3A0xa322ce9752833d6e!2sINSINYUR%20MARTABAK%20(Cab.%20Cibaduyut)Tci!5e0!3m2!1sid!2sid!4v1583329833260!5m2!1sid!2sid';
                active3=true;
                active1=false;
                active2=false;
                active4=false;"
                v-bind:class="{ active: active3 }">
                <p class="lead3">Kiaracondong</p>
                <p>Jl. Babakan Sari no 115 Kiaracondong, Bandung</p>
                <p class="lead3 float-right bg-white px-3 py-2">
                  Buka 14.00 - 23.00
                </p>
              </div>
              <div class="container bg-light"
                @click="src_cabang = '';
                active4=true;
                active1=false;
                active3=false;
                active2=false;">
                <p class="lead3">Kiaracondong</p>
                <p>Jl. Babakan Sari no 115 Kiaracondong, Bandung</p>
                <p class="lead3 float-right bg-white px-3 py-2">
                  Buka 14.00 - 23.00
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6 p-0">
          <div class="embed-responsive embed-responsive-1by1">
            <iframe
              class="embed-responsive-item"
              :src="src_cabang"
              frameborder="0"
              style="border:0;"
              allowfullscreen=""
            ></iframe>
          </div>
        </div>
      </div>
    </section>
    <section id="comment">
      <div class="container-fluid row p-0 m-0 mx-auto">
        <div class="text-center col-md-12 p-0">
          <h1 class="display-4 mt-5 pt-4">Tanggapan Pembeli</h1>
          <p class="mb-5 pb-4">
            Mention kami dengan hashtag <b>#irmartabak_moment</b>
          </p>
        </div>
      </div>
      <div class="container-fluid row p-0 m-0 mx-auto">
        <div class="col-md-12 col-sm-12 p-0 mx-auto">
          <carousel
            :autoplay="true"
            :scrollPerPage="false"
            :perPage="1"
            :perPageCustom="[
              [480, 1],
              [960, 3]
            ]"
            :navigationEnabled="true"
            :paginationEnabled="false"
            :loop="true"
          >
            <slide v-bind:key="i" v-for="i in 6">
              <comment
                comment="Wow, martabaknya enak buanget, de best pokonya! selalu jadi reccomend buat beli martabak apapun kesukaan kalian <3"
              />
            </slide>
          </carousel>
        </div>
      </div>
    </section>
    <section class="py-5" id="available">
      <div class="container-fluid row p-0 m-0 mx-auto">
        <div class="col-md-12 p-0">
          <h1 class="text-center display-4 my-5">Tersedia Juga di</h1>
        </div>
      </div>
      <div class="container-fluid row mt-5 p-0 m-0 mx-auto">
        <div class="col-md-6 p-0 text-center my-5">
          <img src="static/img/gofood.png" class="w-50" srcset="">
        </div>
        <div class="col-md-6 p-0 text-center my-5">
          <img src="static/img/grabfood.png" class="w-50" srcset="">
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import menucard from "../components/menucard.vue";
import comment from "../components/comment.vue";

export default {
  name: "Home",
  data() {
    return {
      martabakhome: [],
      active1: true,
      active2: false,
      active3: false,
      active4: false,
      loading: true,
      errored: false,
      src_cabang: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15842.932382044912!2d107.64236086977539!3d-6.922476099999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e68e7e12f13b5c7%3A0x345f76036dfa4d45!2sIr.%20Martabak(Insinyur%20Martabak)!5e0!3m2!1sid!2sid!4v1583127885422!5m2!1sid!2sid"
    };
  },

  mounted () {
    this.$axios
      .get('http://127.0.0.1:8000/api/database/')
      .then(response => {
        this.martabakhome = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
  },

  components: {
    menucard,
    comment
  },
  methods: {
  }
};
</script>
