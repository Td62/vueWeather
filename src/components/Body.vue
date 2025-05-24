<template>
    <div class="container">
        <div class="left">
            <div class="svg">
                <svg class="icon" aria-hidden="true">
                    <use xlink:href="#icon-tianqi-qing"></use>
                </svg>
            </div>
            <div class="temperature">
                <div class="temperature-wrapper">
                    <span class="temperature-value">26</span>
                    <span class="temperature-unit">℃</span>
                </div>
                <span class="feels-like">Feels Like 55°</span>
            </div>
        </div>
        <div class="right">
            <div>222</div>
            <div>111</div>
        </div>
    </div>
</template>

<style scoped>
.container {
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.left,
.right {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex: 1;
}

.temperature {
    display: flex;
    flex-direction: column;
    
}

.temperature-wrapper {
    display: flex;
    align-items: flex-start; 
}

.temperature-value {
    font-size: 6em;
    line-height: 1;
}

.temperature-unit {
    font-size: 2em;
    margin-left: 4px; 
}

.feels-like {
    font-size: 1.4em;
    margin-top: 8px;
}

.icon {
    width: 12em;
    height: 12em;
}
</style>