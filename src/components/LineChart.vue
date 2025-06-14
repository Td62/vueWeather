<template>
  <div ref="chartDom" style="width: 100%; height: 18rem"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, defineProps } from 'vue';
import * as echarts from 'echarts/core';
import { GridComponent } from 'echarts/components';
import { LineChart } from 'echarts/charts';
import { UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';

// 按需注册组件
echarts.use([
  GridComponent,
  LineChart,
  CanvasRenderer,
  UniversalTransition
]);

const props = defineProps({
  lineChartData: {
    type: Object,
    required: true,
    default: () => ({ data: [], nextSevenDaysData: [] })
  }
});

const chartDom = ref(null);
let myChart = null;

// 处理温度数据
const processTempData = (tempStr) => {
  if (!tempStr) return 0;
  return parseInt(tempStr.toString().replace('°', ''), 10) || 0;
};

// 天气类型到降雨概率的映射
const weatherToRainfall = (weather) => {
  const map = {
    '小雨': 30,
    '中雨': 60,
    '大雨': 80,
    '暴雨': 95,
    '雷阵雨': 70,
    '阵雨': 50,
    '多云': 10,
    '晴': 0,
    '阴': 5
  };
  return map[weather] || 0;
};

// 计算温度轴范围
const calculateTempRange = (temps) => {
  if (temps.length === 0) return { min: 0, max: 40 };
  
  const maxTemp = Math.max(...temps);
  const minTemp = Math.min(...temps);
  
  // 确定最小值和最大值（5的倍数）
  const min = Math.floor(minTemp / 5) * 5;
  const max = Math.ceil(maxTemp / 5) * 5;
  
  // 确保至少有20度的范围
  return { 
    min: Math.max(0, min - 5), 
    max: max < 20 ? 25 : max + 5 
  };
};

// 生成图表配置
const generateOption = () => {
  const data = Array.isArray(props.lineChartData.data) 
    ? props.lineChartData.data 
    : [];
  
  const dates = data.map(item => item.date || '');
  const maxTemps = data.map(item => processTempData(item.max_temp));
  
  // 降雨概率数据
  const rainfallData = data.map(item => ({
    value: weatherToRainfall(item.weather),
    weather: item.weather
  }));
  
  // 计算温度范围
  const tempRange = calculateTempRange(maxTemps);
  
  return {
    grid: {
      top: '22%',    // 增加顶部空间
      right: '10%',
      bottom: '22%', // 增加底部空间
      left: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: dates,
      axisLabel: {
        fontSize: 12,
        color: '#666',
        interval: 0
      },
      axisLine: {
        show: true,
        lineStyle: {
          color: '#e0e0e0'
        }
      },
      axisTick: {
        show: false
      }
    },
    yAxis: [
      {
        type: 'value',
        min: tempRange.min,
        max: tempRange.max,
        interval: 5, // 固定每5度一个刻度
        name: 'Temperature(℃)',
        nameTextStyle: {
          fontSize: 12,
          padding: [0, 0, 0, 20]
        },
        axisLabel: {
          fontSize: 12,
          color: '#666',
          formatter: '{value}°'
        },
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        splitLine: {
          show: true,
          lineStyle: {
            type: 'dashed',
            color: '#f0f0f0',
            opacity: 0.5
          }
        }
      },
      {
        type: 'value',
        min: 0,
        max: 100,
        interval: 20,
        position: 'right',
        name: 'POP(%)',
        nameTextStyle: {
          fontSize: 12,
          padding: [0, 20, 0, 0]
        },
        axisLabel: {
          fontSize: 12,
          color: '#666',
          formatter: '{value}%'
        },
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        splitLine: {
          show: false
        }
      }
    ],
    tooltip: {
      trigger: 'axis',
      backgroundColor: 'rgba(255, 255, 255, 0.9)',
      borderWidth: 0,
      padding: 10,
      textStyle: {
        color: '#333'
      },
      formatter: function(params) {
        const index = params[0].dataIndex;
        const weatherInfo = data[index] || {};
        const rainfallInfo = rainfallData[index] || { value: 0 };
        
        return `
          <div style="font-weight:bold;margin-bottom:5px;color:#333;">${weatherInfo.date || ''}</div>
          <div>天气: ${weatherInfo.weather || '未知'}</div>
          <div>最高温: ${weatherInfo.max_temp || '0°'}</div>
          <div>降雨概率: ${rainfallInfo.value}%</div>
        `;
      }
    },
    series: [
      {
        name: '最高温度',
        data: maxTemps,
        type: 'line',
        symbol: 'circle',
        symbolSize: 8,
        label: {
          show: true,
          position: 'top',
          fontSize: 11, // 减小字体大小避免重叠
          color: '#FFA500',
          formatter: '{c}°',
          borderRadius: 4,
          textBorderColor: 'rgba(0,0,0,0.1)', // 添加文字描边
          textBorderWidth: 1
        },
        smooth: true,
        itemStyle: { 
          color: '#FFA500',
          borderWidth: 2,
          borderColor: '#fff'
        },
        lineStyle: { 
          color: '#FFA500',
          width: 3
        },
        emphasis: {
          itemStyle: {
            color: '#FF8C00',
            borderColor: '#fff',
            borderWidth: 2
          }
        }
      },
      {
        name: '降雨概率',
        data: rainfallData.map(item => item.value),
        type: 'line',
        yAxisIndex: 1,
        symbol: 'circle',
        symbolSize: 8,
        label: {
          show: true,
          position: 'top',
          fontSize: 11, // 减小字体大小避免重叠
          color: '#40A7DC',
          formatter: '{c}%',
          textBorderColor: 'rgba(0,0,0,0.1)', // 添加文字描边
          textBorderWidth: 1
        },
        smooth: true,
        itemStyle: { 
          color: '#40A7DC',
          borderWidth: 2,
          borderColor: '#fff'
        },
        lineStyle: { 
          color: '#40A7DC',
          width: 3
        },
        emphasis: {
          itemStyle: {
            color: '#1E88E5',
            borderColor: '#fff',
            borderWidth: 2
          }
        }
      }
    ]
  };
};

onMounted(() => {
  if (!chartDom.value) return;
  
  myChart = echarts.init(chartDom.value);
  window.addEventListener('resize', handleResize);
  
  try {
    const option = generateOption();
    myChart.setOption(option);
  } catch (error) {
    console.error('ECharts初始化失败:', error);
  }
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  myChart?.dispose();
});

const handleResize = () => {
  myChart?.resize();
};

// 监听数据变化
watch(() => props.lineChartData, (newData) => {
  if (newData && myChart) {
    try {
      const option = generateOption();
      myChart.setOption(option);
    } catch (error) {
      console.error('ECharts更新失败:', error);
    }
  }
}, { deep: true });
</script>