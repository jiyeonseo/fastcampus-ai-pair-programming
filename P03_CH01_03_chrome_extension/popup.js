document.addEventListener('DOMContentLoaded', function() {
    updateDateTime();
    updateClock(); // 문서 로딩 시 시계 업데이트
    fetchLocation();
});

function updateDateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById('time').textContent = timeString;
    setTimeout(updateDateTime, 1000); // 매 1초마다 시간 업데이트
}

function fetchLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            document.getElementById('location').textContent = `위도: ${lat}, 경도: ${lon}`;
        }, function(error) {
            document.getElementById('location').textContent = "위치 정보를 가져올 수 없습니다.";
        });
    } else {
        document.getElementById('location').textContent = "Geolocation이 지원되지 않습니다.";
    }
}
function updateClock() {
    const now = new Date();

    // 각 도시의 시간대에 맞게 Date 객체 조정
    const sanFranciscoTime = new Date(now.toLocaleString("en-US", {timeZone: "America/Los_Angeles"}));
    const hanoiTime = new Date(now.toLocaleString("en-US", {timeZone: "Asia/Ho_Chi_Minh"}));
    const sydneyTime = new Date(now.toLocaleString("en-US", {timeZone: "Australia/Sydney"}));

    // 각 도시의 시간에 따라 시계 업데이트
    updateHandPositions(sanFranciscoTime, 'sanFrancisco');
    updateHandPositions(hanoiTime, 'hanoi');
    updateHandPositions(sydneyTime, 'sydney');

    setTimeout(updateClock, 1000); // 매 초마다 시계 업데이트
}

function updateHandPositions(time, cityPrefix) {
    const second = time.getSeconds();
    const minute = time.getMinutes();
    const hour = time.getHours();

    const secondAngle = second * 6;
    const minuteAngle = minute * 6 + second * 0.1;
    const hourAngle = hour * 30 + minute * 0.5;

    document.getElementById(`${cityPrefix}Hour`).style.transform = `rotate(${hourAngle}deg)`;
    document.getElementById(`${cityPrefix}Minute`).style.transform = `rotate(${minuteAngle}deg)`;
    document.getElementById(`${cityPrefix}Second`).style.transform = `rotate(${secondAngle}deg)`;
}
