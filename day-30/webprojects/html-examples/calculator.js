// Simple enhancement: animate the result
document.addEventListener('DOMContentLoaded', function () {
    const resultEl = document.getElementById('result');
    if (resultEl) {
        resultEl.classList.add('scale-up');
        setTimeout(() => {
            resultEl.classList.remove('scale-up');
        }, 1000);
    }
});
