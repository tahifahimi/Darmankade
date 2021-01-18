<template>
  <div>
    <Nuxt />
  </div>
</template>

<script>
import feather from 'feather-icons'

export default {
  mounted: function(){
    feather.replace()
  }  
}
</script>

<style>
@import url('@/assets/common.css');
@import url('http://www.fontonline.ir/css/BYekan.css');
</style>
