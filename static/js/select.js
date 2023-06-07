const selectElement = document.querySelector('.chapter');

selectElement.addEventListener('change', (event) => {
location.href ="/getchapter"+event.target.value
});