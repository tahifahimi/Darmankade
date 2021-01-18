<template>
  <div>
    <Header />
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/header.vue'
import Footer from '../components/footer.vue'
import feather from 'feather-icons'

export default {
  components: {
    Header,
    Footer
  },
  mounted: function(){
    feather.replace()
  }
}
</script>

<style>
@import url('@/assets/bootstrap/css/bootstrap.css');
@import url('@/assets/common.css');
@import url('http://www.fontonline.ir/css/BYekan.css');
</style>
