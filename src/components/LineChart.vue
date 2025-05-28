<template>
  <div ref="chartDom" style="width: 100%; height: 18rem"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
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

const chartDom = ref(null); // 通过 ref 绑定 DOM
let myChart = null;

// 配置项
const option = {
  xAxis: {
    type: 'category',
    data: ['8AM', '9AM', '10AM', '11AM', '12AM', '13PM', '14PM'],
    axisLabel: { // 新增 X 轴标签样式
      fontSize: 20,  // X 轴文字大小
      color: '#666' // 文字颜色
    }
  },
  yAxis: [
    {
      type: 'value', min: 0, max: 50, position: 'left',
      axisLabel: { // 左侧 Y 轴标签
        fontSize: 20,
        color: '#666'
      }
    },
    {
      type: 'value', min: 0, max: 100, position: 'right',
      axisLabel: { // 右侧 Y 轴标签
        fontSize: 20,
        color: '#666'
      }
    }
  ],
  series: [
    {
      data: [9, 11, 12, 14, 16, 20, 38],
      type: 'line',
      yAxisIndex: 0,
      label: {
        show: true, position: 'top',
        fontSize: 20,  // 数据标签字体
        color: '#FFA500'// 与线条颜色一致 
      },
      smooth: true,
      itemStyle: { color: '#FFA500' },
      lineStyle: { color: '#FFA500' }
    },
    {
      data: [70, 60, 80, 90, 20, 11, 30],
      type: 'line',
      yAxisIndex: 1,
      label: {
        show: true, position: 'top', fontSize: 20,  // 数据标签字体
        color: '#40A7DC'// 与线条颜色一致 
      },
      smooth: true,
      itemStyle: { color: '#40A7DC' },
      lineStyle: { color: '#40A7DC' }
    }
  ]
};

onMounted(() => {
  // 确保 DOM 已挂载后初始化
  myChart = echarts.init(chartDom.value);
  myChart.setOption(option);

  // 添加窗口响应式
  window.addEventListener('resize', handleResize);
});

// 组件卸载时销毁实例
onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  myChart?.dispose();
});

// 响应式调整
const handleResize = () => {
  myChart?.resize();
};
</script>