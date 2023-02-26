<template>
  <div>
    <MenuHeader></MenuHeader>
    <ImageViewer></ImageViewer>
  </div>
</template>

<script>
import MenuHeader from './layout/MenuHeader'
import ImageViewer from './layout/ImageViewer.vue'

export default {
  name: 'App',
  components: {
    MenuHeader,
    ImageViewer
  }
}
</script>
