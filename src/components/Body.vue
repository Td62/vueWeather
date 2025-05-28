<template>
    <div class="container">
        <div class="left">
            <img src="../assets/icons/01d.png" alt="" class="icon">
            <div class="temperature">
                <div class="temperature-wrapper">
                    <span class="temperature-value">26</span>
                    <span class="temperature-unit">℃</span>
                </div>
                <span class="feels-like">Feels Like 25°</span>
            </div>
        </div>
        <div class="right">
            <div class="right-container">
                <img src="../assets/icons/sunrise.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Sunrise</div>
                    <div class="text-suffix">
                        <div class="text-bold">9.16</div>
                        <div class="min-text">AM</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/sunset.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Sunset</div>
                    <div class="text-suffix">
                        <div class="text-bold">5.25</div>
                        <div class="min-text">PM</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/wind.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Wind</div>
                    <div class="text-suffix">
                        <div class="text-bold">3.44</div>
                        <div class="min-text">mph</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/humidity.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Humidity</div>
                    <div class="text-suffix">
                        <div class="text-bold">83</div>
                        <div class="min-text">%</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/pressure.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Pressure</div>
                    <div class="text-suffix">
                        <div class="text-bold">1015</div>
                        <div class="min-text">kPa</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/uvi.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">UV Index</div>
                    <div class="text-suffix">
                        <div class="text-bold">1.26</div>
                        <div class="min-text"></div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/visibility.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Visibility</div>
                    <div class="text-suffix">
                        <div class="text-bold">>10</div>
                        <div class="min-text">km</div>
                    </div>
                </div>
            </div>
            <div class="right-container">
                <img src="../assets/icons/aqi.png" alt="" class="min_icon">
                <div class="text-group">
                    <div class="base-text">Air Quality</div>
                    <div class="text-suffix">
                        <div class="text-bold">5</div>
                        <div class="min-text">Very Poor</div>
                    </div>
                </div>
            </div>


            
        </div>
    </div>
</template>

<style scoped>
.container {
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    flex-wrap: wrap;
}

.left {
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
    font-size: 10rem;
    line-height: 1;
}

.temperature-unit {
    font-size: 3rem;
    margin-left: 4px;
}

.feels-like {
    font-size: 2rem;
    margin-top: 8px;
}

.icon {
    width: 18rem;
    height: 18rem;
}

.min_icon {
    width: 4rem;
    height: 4rem;
}

.right {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    flex: 1;

}

.right>div {
    flex: 0 0 50%;
    box-sizing: border-box;
}

.right-container {
    display: flex;
    align-items: center;
    gap: 4rem;
}

.text-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: 1.2;
}

.text-suffix {
    display: flex;
    align-items: baseline;
    gap: 4px;
}
.text-bold{
    font-weight: bold;
    font-size: 2rem;
}
.base-text{
    font-size: 1.4rem;
}
.min-text{
    font-size: 1.2rem;
}
</style>