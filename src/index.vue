<template>
    <Header></Header>
    <Body></Body>
    <LineChart></LineChart>
    <Footer></Footer>
    
</template>

<script>
import Header from "./components/Header.vue";
import Body from "./components/Body.vue";
import LineChart from "./components/LineChart.vue";
import Footer from "./components/Footer.vue";
export default{
    components:{
        Header:Header,
        Body:Body,
        LineChart:LineChart,
        Footer:Footer
    }
}
</script>
<style>
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>