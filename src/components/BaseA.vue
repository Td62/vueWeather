<template>
    <div class="baseA">
        组件A(接收方)
        <p>{{message}}</p>
    </div>
</template>

<script>
import Bus from '@/utils/EventBus';
export default{
    data(){
        return{
            message:''
        }
    },
    created(){
        Bus.on('sendMessage',(Message)=>{
            this.message = Message;
        })
    }
}
</script>

<style scoped>
.baseA{
    width: 200px;
    height: 150px;
    padding: 10px;
    margin-top: 10px;
    border: 3px solid #000;
    border-radius: 5px;
    font-size: 20px;
}
</style>