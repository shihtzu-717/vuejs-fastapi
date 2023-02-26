<template>
  <div class="wrap" style="height: 180px">
    <!-- <h1>Header</h1>ß
      <router-link to="/">Home</router-link> / <router-link to="/bar">Go to Bar</router-link> -->
    <div id="model-bg">
      <br />
      <text class="menu">MODEL</text><br /><br />
      <div id="model">
        <span style="display: inline-block; width: 17%; text-align: justify">
          모델 선택 :
        </span>
        <input type="text" v-model="model_name" />
        <!-- <select v-model="selectedModel">
            <option >모델을 선택하세요.</option>
            <option :value="model.name" :key="model.name" v-for="model in modelList" >{{ model.name }}</option>
        </select> -->
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
        파일을 선택하세요. <br /><input type="file" multiple /><br />
      </div>
    </div>
  </div>
  <button id="inference_btn">추론 시작</button>
  <span>{{ msg }}</span>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      modelList: [
        { name: '220830' },
        { name: '220222' },
        { name: '000918' },
        { name: '210717' }
      ],
      model_name: '',
      iou_thresh: '0.5',
      thresh: '0.25',
      msg: ''
    }
  },
  methods: {
    getMessage() {
      axios
        .get('/')
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created() {
    this.getMessage()
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
