(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{69:function(a,t,i){"use strict";i.r(t);var e={name:"menuslider",data:function(){return{martabakmenu:[],ratingdata:[],errored:!1,loading:!0}},components:{menucard:function(){return i.e(1).then(i.bind(null,72))}},created:function(){var a=this;this.$axios.get("/api/rating/").then((function(t){a.ratingdata=t.data})),this.$axios.get("/api/martabak/").then((function(t){a.martabakmenu=t.data})).catch((function(t){console.log(t),a.errored=!0})).finally((function(){return a.loading=!1}))},props:{currentMartabak:Number}},n=i(1),s=Object(n.a)(e,(function(){var a=this,t=a.$createElement,i=a._self._c||t;return i("section",{attrs:{id:"favorite"}},[a._m(0),a._v(" "),i("div",{staticClass:"container-fluid row p-0 m-0 mx-auto"},[i("div",{staticClass:"col-9 p-0 mx-auto mb-2 pb-5"},[i("carousel",{staticClass:"mdi",attrs:{autoplay:!0,scrollPerPage:!1,perPage:1,perPageCustom:[[480,1],[768,2],[992,3]],navigationEnabled:!0,navigationNextLabel:"",navigationPrevLabel:"",paginationEnabled:!1,loop:!0}},[a.loading?i("slide",[i("div",{staticClass:"card card--menu card--disable mx-2"},[i("div",{staticClass:"image-card"},[i("img",{staticClass:"card-img-top img-fluid fit-cover"})]),a._v(" "),i("div",{staticClass:"card-img-overlay skeleton-card-overlay"})])]):a._e(),a._v(" "),a.loading?i("slide",[i("div",{staticClass:"card card--menu card--disable mx-2"},[i("div",{staticClass:"image-card"},[i("img",{staticClass:"card-img-top img-fluid fit-cover"})]),a._v(" "),i("div",{staticClass:"card-img-overlay skeleton-card-overlay"})])]):a._e(),a._v(" "),a.loading?i("slide",[i("div",{staticClass:"card card--menu card--disable mx-2"},[i("div",{staticClass:"image-card"},[i("img",{staticClass:"card-img-top img-fluid fit-cover"})]),a._v(" "),i("div",{staticClass:"card-img-overlay skeleton-card-overlay"})])]):a._e(),a._v(" "),a._l(a.martabakmenu,(function(t){return t.id!=a.currentMartabak?i("slide",{key:t},a._l(a.ratingdata,(function(e){return i("div",{key:e.object_id},[e.object_id==t.id?i("div",[i("menucard",{attrs:{price:t.price,name:t.name,rating:parseFloat(e.average),img:t.image,slug:t.slug}})],1):a._e()])})),0):a._e()}))],2)],1)]),a._v(" "),i("div",{staticClass:"container-fluid row p-0 m-0 mx-auto mb-5"},[a.loading?i("div",{staticClass:"col mx-auto p-0 text-center"},[i("button",{staticClass:"mx-auto btn btn-skeleton btn-lg px-5 py-3",attrs:{type:"button"}},[a._v("\n              Menu Lainnya\n            ")])]):a._e(),a._v(" "),a.loading?a._e():i("div",{staticClass:"col mx-auto p-0 text-center"},[i("router-link",{staticClass:"mx-auto btn btn-primary btn-lg px-5 py-3",attrs:{to:"/menu",tag:"button",type:"button"}},[a._v("\n              Menu Lainnya\n            ")])],1)])])}),[function(){var a=this.$createElement,t=this._self._c||a;return t("div",{staticClass:"container-fluid row p-0 m-0 mx-auto"},[t("div",{staticClass:"col-md-12 p-0"},[t("h1",{staticClass:"text-center display-4 my-5"},[this._v("Menu Paling Populer")])])])}],!1,null,null,null);t.default=s.exports}}]);