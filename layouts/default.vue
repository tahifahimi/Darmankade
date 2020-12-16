<template>
  <div>
    <Header />
    <Nuxt />
  </div>
</template>

<script>
import Header from '../components/header.vue'
import feather from 'feather-icons'

export default {
  components: {
    Header,
  },
  mounted: function(){
    feather.replace()
  }
}
</script>

<style>
@import url('http://www.fontonline.ir/css/BYekan.css');
</style>
