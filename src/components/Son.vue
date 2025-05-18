<template>
    <div>son{{ title }}</div>
    <button @click="changeFn">edit</button>
</template>
<script>
export default {
    props: {
        title:{
            type:String,
            required:true,
            default:'',
            validator(value){
                console.log(value)
                if (value) {
                return true
                }
                return false
            }
        }
    },
    emits: ['changeTitle'],//显式声明组件会触发哪些自定义事件不需要修改模板结构，
                         // 保持原有的多个根节点
    methods:{
        changeFn(){
            //$emit 子传父
            this.$emit('changeTitle','sonValue')
        }
    }
}
</script>