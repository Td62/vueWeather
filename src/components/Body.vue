<template>
    <div class="container">
        <div class="left">
            <img src="../assets/icons/01d.png" alt="" class="icon">
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
    font-size: 9rem;
    line-height: 1;
}

.temperature-unit {
    font-size: 2rem;
    margin-left: 4px; 
}

.feels-like {
    font-size: 1.9rem;
    margin-top: 8px;
}

.icon {
    width: 18rem;
    height: 18rem;
}
</style>