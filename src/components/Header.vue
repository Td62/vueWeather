<template>
  <div class="container">
    <div class="simple-clock">
      <div v-for="(timePart, index) in timeParts" :key="index" class="time-part">
        <div class="digit-container">
          <transition name="slide">
            <div :key="timePart" class="digit">{{ timePart }}</div>
          </transition>
        </div>
        <div class="separator" v-if="index < 2"></div>
      </div>
    </div>
    <div class="location">ShenZhen,LongHua</div>
    <div class="date">{{ currentDate }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentTime: '00:00:00',
      currentDate: '',
      timeInterval: null,
      dateUpdateTimer: null
    }
  },
  computed: {
    timeParts() {
      return this.currentTime.split(':')
    }
  },
  methods: {
    getPreciseTime() {
      const now = new Date()
      return now.toLocaleTimeString('en-US', { hour12: false })
    },
    
    updateTime() {
      // 立即更新当前时间（不等待动画）
      this.currentTime = this.getPreciseTime()
      
      // 计算到下一秒的精确时间
      const now = new Date()
      const nextSecond = new Date(now)
      nextSecond.setMilliseconds(0)
      nextSecond.setSeconds(now.getSeconds() + 1)
      const delay = nextSecond - now
      
      // 清除旧定时器并设置新定时器
      clearTimeout(this.timeInterval)
      this.timeInterval = setTimeout(() => {
        this.updateTime()
      }, delay)
    },
    
    updateDate() {
      const now = new Date()
      this.currentDate = now.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
      
      // 设置午夜自动更新
      const nextMidnight = new Date(
        now.getFullYear(),
        now.getMonth(),
        now.getDate() + 1
      )
      const timeUntilMidnight = nextMidnight - now
      
      clearTimeout(this.dateUpdateTimer)
      this.dateUpdateTimer = setTimeout(() => {
        this.updateDate()
        this.updateTime() // 确保午夜立即更新时间
      }, timeUntilMidnight)
    },
    
    async syncWithServerTime() {
      try {
        const response = await fetch('https://worldtimeapi.org/api/ip')
        const data = await response.json()
        const serverTime = new Date(data.datetime)
        this.currentTime = serverTime.toLocaleTimeString('en-US', { hour12: false })
        this.currentDate = serverTime.toLocaleDateString('en-US', {
          weekday: 'long',
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        })
      } catch (e) {
        console.log('使用本地时间', e)
      }
    }
  },
  mounted() {
    // 初始同步时间
    this.syncWithServerTime()
    // 启动精确计时器
    this.updateTime()
    this.updateDate()
  },
  beforeUnmount() {
    clearTimeout(this.timeInterval)
    clearTimeout(this.dateUpdateTimer)
  }
}
</script>

<style scoped>
.container {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
}

.location {
  font-size: 42px;
  margin-bottom: 8px;
  color: #333;
}

.date {
  font-size: 28px;
  color: #666;
}

.simple-clock {
  display: flex;
  font-size: 50px;
  font-weight: bold;
}

.time-part {
  display: flex;
  align-items: center;
}

.digit-container {
  position: relative;
  width: 60px;
  height: 60px;
  overflow: hidden;
}

.digit {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  will-change: transform, opacity;
}

.separator {
  position: relative;
  width: 10px;
  height: 60px;
  margin: 0 10px;
}

.separator::before,
.separator::after {
  content: '';
  position: absolute;
  left: 50%;
  width: 6px;
  height: 6px;
  background: #333;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}

.separator::before {
  top: 40%;
}

.separator::after {
  top: 60%;
}

/* 优化后的动画时间 */
.slide-enter-active {
  transition: all 0.2s ease;
  transform: translateY(0);
}

.slide-leave-active {
  transition: all 0.3s ease;
  position: absolute;
}

.slide-enter-from {
  transform: translateY(-100%);
  opacity: 0;
}

.slide-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>