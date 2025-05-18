<template>
    <div class="baseB">
        组件B(发布方)
        <button @click="sendBus">发布信息</button>
    </div>
</template>

<script>
import Bus from '@/utils/EventBus';
export default{
    methods:{
        sendBus(){
            Bus.emit('sendMessage','BaseBMessage')
        }
    }
}
</script>

<style scoped>
.baseB{
    width: 200px;
    height: 150px;
    padding: 10px;
    margin-top: 10px;
    border: 3px solid #000;
    border-radius: 5px;
    font-size: 20px;
}
button{
    display: block;
}
</style>