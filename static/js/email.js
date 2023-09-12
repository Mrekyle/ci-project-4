function sendMail (contactForm) {
    emailjs.send("service_6tepuq5","template_89y5wtg", {
        'from_name': contactForm.name.value, 
        'contact_email': contactForm.email.value, 
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