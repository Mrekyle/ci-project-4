/**
 * Alert messages function to close the alert after the time has passed
 */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alerts = new bootstrap.Alert(messages);
    alerts.close();
}, 4000);