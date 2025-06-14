<template>
    <Header :location="location"></Header>

    <Body v-if="current_weather" :current_weather="current_weather"></Body>
    <LineChart :lineChartData="lineChartData"></LineChart>
    <Footer :forecast7days="forecast7days"></Footer>
</template>

<script>
import Header from "./components/Header.vue";
import Body from "./components/Body.vue";
import LineChart from "./components/LineChart.vue";
import Footer from "./components/Footer.vue";
import { getWeatherData } from "../src/services/indexApi"

export default {
    components: {
        Header,
        Body,
        LineChart,
        Footer
    },
    data() {
        return {
            location: "ShenZhen,LongHua",
            current_weather: null,
            nextSevenDaysData: [],
            forecast7days: {
                nextSevenDaysData: [],
                data:{}
            },
            lineChartData:{
                nextSevenDaysData: [],
                data:{}
            },
            updateInterval: null
        };
    },
    methods: {
        getNextSevenDays() {
            // 定义星期几的缩写
            const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

            // 创建当前日期对象
            const today = new Date();

            // 存储结果的数组
            const nextDays = [];

            // 计算未来七天的日期
            for (let i = 1; i <= 7; i++) {
                // 创建新的日期对象，避免修改原始日期
                const nextDay = new Date(today);

                // 设置为未来第i天
                nextDay.setDate(today.getDate() + i);

                // 获取星期几的缩写
                const dayName = weekdays[nextDay.getDay()];

                // 获取日期（月份中的天数）
                const dayDate = nextDay.getDate();

                // 获取月份
                const month = nextDay.getMonth() + 1; // 月份从0开始，所以加1

                // 格式化为 "月/日"
                const formattedDate = `${month}/${dayDate}`;

                // 添加到结果数组
                nextDays.push({
                    day: dayName,
                    date: formattedDate
                });
            }

            return nextDays;
        },
        async fetchWeatherData() {
            try {
                const response = await getWeatherData();
                this.current_weather = response.current_weather;
                this.forecast7days.data = response.forecast_7days;
                this.lineChartData.data = response.forecast_7days;
               // console.log(this.current_weather)
               // console.log(this.forecast7days)
            } catch (error) {
                console.error('获取天气数据失败:', error);
            }
        }
    },
    mounted() {
        // 初始加载数据
        this.fetchWeatherData();
        this.nextSevenDaysData = this.getNextSevenDays();
        // 每半小时更新一次（1800000毫秒 = 30分钟）
        this.updateInterval = setInterval(() => {
            this.fetchWeatherData();
            this.nextSevenDaysData = this.getNextSevenDays();
        }, 900000);
    },
    watch: {
        // 监听nextSevenDaysData的变化
        nextSevenDaysData: {
            handler(newValue, oldValue) {
                // 当nextSevenDaysData变化时，将其赋值给forecast7days中的对应属性
                this.forecast7days.nextSevenDaysData = newValue;
                this.lineChartData.nextSevenDaysData = newValue;
               // console.log('nextSevenDaysData 已更新:', this.forecast7days);
            },
            deep: true, // 深度监听数组内部变化
            immediate: true // 初始渲染时立即执行一次
        }
    },
    beforeUnmount() {
        // 清除定时器
        clearInterval(this.updateInterval);
    }
}
</script>