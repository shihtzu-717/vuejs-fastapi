<template>
  <form @submit.prevent="postInputData()" method="post" enctype="multipary/form-data" >
  <div class="wrap" style="height: 180px">
    <div id="model-bg">
      <br />
      <text class="menu">MODEL</text><br /><br />
      <div id="model">
        <span style="display: inline-block; width: 17%; text-align: justify">
          모델 선택 :
        </span>
        <input type="text" v-model="model_name" />
        <br />
        <span style="display: inline-block; width: 17%; text-align: justify">
          iou_thresh :
        </span>
        <input type="text" v-model="iou_thresh" />
        <br />
        <span style="display: inline-block; width: 17%; text-align: justify">
          thresh :
        </span>
        <input type="text" v-model="thresh" />
      </div>
    </div>
    <div id="data-bg">
      <br />
      <text class="menu">DATA</text><br /><br />
      <div id="data">
        파일을 선택하세요. <br />
        <input type="file" multiple @change="uploadImage($event.target.files)" ref="files"><br/>
      </div>
    </div>
  </div>
  <input type="submit" id="inference_btn" value="추론 시작"/>
  </form>
  <span>{{ msg }} </span>
  <span> {{ model_name }} {{ iou_thresh}} {{thresh }} {{ image_list }}</span>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      model_name: '',
      iou_thresh: '0.5',
      thresh: '0.25',
      image_list: [],
      uploadImageIndex: 0,
      msg: ''
    }
  },
  methods: {
    postInputData() {
      const formData = new FormData()
      formData.append('model_name', this.model_name)
      formData.append('iou_thresh', this.iou_thresh)
      formData.append('thresh', this.thresh)

      for (const f of this.image_list) {
        formData.append('image_list', f)
      }

      axios
        .post('/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((res) => {
          console.log(res)
        })
        .catch((res) => {
          console.log('error', res)
        })
    },
    uploadImage(files) {
      console.log('THAP')
      this.image_list = files
      console.log(this.image_list)
    },

    created() {
      this.getMessage()
    }
  }
}
</script>

<style scoped>
.wrap {
  display: flex;
  position: sticky;
  margin-bottom: 10px;
}
.menu {
  font-size: 20px;
  font-weight: bold;
}
#model-bg {
  flex: 1;
  background-color: pink;
  padding-left: 30px;
}
#model {
  padding-left: 10px;
}

#data-bg {
  flex: 1;
  background-color: lightgray;
  padding-left: 30px;
}

#data {
  padding-left: 10px;
}

#inference_btn {
  background-color: whitesmoke;
  margin: auto;
  display: block;
  width: 100px;
  font-size: large;
}
</style>
