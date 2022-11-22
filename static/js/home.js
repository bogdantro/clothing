const cookieStorage = {
    getItem: (key) => {
        const cookies = document.cookie
            .split(';')
            .map(cookie => cookie.split('='))
            .reduce((acc, [key, value]) => ({ ...acc, [key.trim()]: value }), {});
        return cookies[key];
    },
    setItem: (key, value) => {
        document.cookie = `${key}=${value}`;
    },
};

const storageType = cookieStorage;
const consentPropertyName = 'stellcare';

const shouldShowPopup = () => !storageType.getItem(consentPropertyName);
const saveToStorage = () => storageType.setItem(consentPropertyName, true);

window.onload = () => {
    const consentPopup = document.getElementById('popup');
    const acceptBtn = document.getElementById('accept');


    const acceptFn = event => {
        saveToStorage(storageType);
        consentPopup.classList.add('hidden')
    };
    
    acceptBtn.addEventListener('click', acceptFn);
    
    if (shouldShowPopup(storageType)) {
        setTimeout(() => {
            consentPopup.classList.remove('hidden')
        }, 3000);
    }
};


window.onload = function(){ 
    setTimeout(() => {
        document.getElementById('coverText').classList.add('active');
    }, 350);
    setTimeout(() => {
        document.getElementById('coverImage').classList.add('active');
    }, 350);
    setTimeout(() => {
        document.getElementById('coverActions').classList.add('active');
    }, 350);
}



function addToCartOverlay(){
    const spinnerDiv = document.getElementById('spinnerOverlay');
    const spinnerFirst = document.getElementById('spinnerFirst');
    const spinnerToCart = document.getElementById('spinnerGoToCart');
    spinnerDiv.classList.add('active')
    setTimeout(function(){
        spinnerFirst.classList.add('hidden')
    },600); 
    setTimeout(function(){
        spinnerToCart.classList.add('active')
    },600); 
}
function RefreshPageHome(){
    location.reload();
}

