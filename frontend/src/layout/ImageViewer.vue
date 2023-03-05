<template>
  <div class="hello">
    <!-- img tag를 이용한 일반적인 Image 생성. -->
    <header class="logo"></header>
    <!-- v-viewer를 이용한 Image 생성. -->
    <viewer :images="this.images">
      <img
        style="width: 300px"
        class="gallary_image"
        v-for="image in this.images"
        :src="image"
        :key="image"
      />
    </viewer>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      images: []
      // images: [require('@/img/1.jpg'), require('@/img/2.jpg'), require('@/img/3.jpg'), require('@/img/lacuna-1.jpg'), require('@/img/lacuna-2.jpg'),
      //   require('@/img/lacuna-3.jpg'), require('@/img/lacuna-4.jpg'), require('@/img/thornapple-1.jpeg'), require('@/img/thornapple-2.png'), require('@/img/blackstar.png')]
    }
  },
  inited(viewer) {
    this.$viewer = viewer
  },
  methods: {
    getResult() {
      axios.get('/').then((res) => {
        console.log('infernece')
        console.log(res.data)
        this.images = res.data
      })
    }
  }
}
</script>
