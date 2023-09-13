
function sendMail (contactForm) {
    emailjs.send("service_g7iucrk","template_89y5wtg", {
        'from_name': contactForm.name.value, 
        'contact_email': contactForm.contact_email.value, 
        'message': contactForm.message.value,
    })
    .then (
        function (response) {
            console.log('Success', response) 
        },
        function (error) {
            console.log('Failed', error) 
        });
    return false;
}

let emailSuccess = document.getElementById('email-success');
let resetForm = document.getElementById('contactForm');

resetForm.addEventListener('submit', (e) => {
    e.preventDefault();
    resetForm.reset();
    emailSuccess.innerHTML += 'Email submitted successfully! <br> We will reply as soon as we can.';
});