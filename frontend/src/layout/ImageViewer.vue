<template>
    <div class="hello">
    <!-- img tag를 이용한 일반적인 Image 생성. -->
    <header class="logo">
    </header>
    <!-- v-viewer를 이용한 Image 생성. -->
    <viewer :images="this.images">
        <img style="width: 300px;" class="gallary_image" v-for="image in this.images" :src="image" :key="image" />

    </viewer>
    </div>
</template>

<script>
export default {
  data() {
    return {
      images: ['https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        'https://images.pexels.com/photos/93684/pexels-photo-93684.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        'https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        'https://images.pexels.com/photos/1073567/pexels-photo-1073567.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        'https://images.pexels.com/photos/35884/amazing-beautiful-beauty-blue.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260']
    }
  },
  inited(viewer) {
    this.$viewer = viewer
  }
}
</script>
