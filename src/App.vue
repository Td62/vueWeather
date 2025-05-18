<template>
  <div>father
    <!-- 父传子 添加属性值方式 -->
    <Son :title="myTitle"  @changeTitle="handleChange"></Son>
  </div>
  <HelloWorld></HelloWorld>
  <div class="main">main</div>
  <BaseA></BaseA>
  <BaseB></BaseB>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import Son from './components/Son.vue';
import BaseA from './components/BaseA.vue';
import BaseB from './components/BaseB.vue';
export default {
  components: {
    HelloWorld: HelloWorld,
    Son: Son,
    BaseA:BaseA,
    BaseB:BaseB
  },
  data() {
    return {
      myTitle: 'father_title'
    }
  },
  methods:{
    handleChange(sonValue){
      this.myTitle = sonValue;
    }
  }
}
</script>
<style scoped>
.main {
  height: 100px;
  background-color: coral;
}
</style>
