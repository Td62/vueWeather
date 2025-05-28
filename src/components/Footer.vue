<template>
    <div class="footer-container">
        <div class="footer-item-container">
            <div class="day">Mon</div>
            <img src="../assets/icons/02d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Tue</div>
            <img src="../assets/icons/03d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Wed</div>
            <img src="../assets/icons/04d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Thu</div>
            <img src="../assets/icons/09d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Fri</div>
            <img src="../assets/icons/10d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Sat</div>
            <img src="../assets/icons/11d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
        <div class="footer-item-container">
            <div class="day">Sun</div>
            <img src="../assets/icons/13d.png" alt="" class="min_icon">
            <div class="footer-text">12<span>/</span>16</div>
        </div>
    </div>
</template>

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