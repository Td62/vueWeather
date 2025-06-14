<template>
    <div class="footer-container">

        <div class="footer-item-container" v-for="(day, index) in forecast7days.data" :key="index">
            <div class="day">{{forecast7days.nextSevenDaysData[index].day}}</div>
            <img :src="getWeatherIcon(day.weather_icon)" class="min_icon">
            <div class="footer-text">{{day.min_temp}}<span>/</span>{{day.max_temp}}</div>
        </div>
    </div>
</template>
<script>
export default {
    props: ['forecast7days'],
    methods:{
        getWeatherIcon(weather_icon) {
            if (weather_icon) {
                return `/src/assets/icons/${weather_icon}`;
            }
        },
    }
}   

    </script>

<style scoped>
.footer-container{
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    gap: 1.8rem;

}
.footer-item-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 2px solid;
    border-radius: 12px;
    padding: 3px 24px 3px 24px;
}
.min_icon {
    width: 8rem;
    height: 8rem;
}
.day{
    font-size: 1.6rem;
    font-weight: bold;
}
.footer-text{
    font-size: 1.4rem;
}
</style>