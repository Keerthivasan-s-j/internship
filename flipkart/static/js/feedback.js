function validate() {
    var ratings = document.getElementById('ratings')
    var exp1 = document.getElementById('exp1').checked;
    var exp2 = document.getElementById('exp2').checked;
    var exp3 = document.getElementById('exp3').checked;
    var message = document.getElementById('message').value.trim();
    var error_ratings = document.querySelector('.error-ratings');
    var error_message = document.querySelector('.error-message');
    
    error_message.innerText = ''; // Clear previous error-messages
    error_ratings.innerText = ''; // Clear previous error-ratings
    
    var valid = true;
    
    if (!exp1 && !exp2 && !exp3) {
        error_ratings.innerText = 'Please rate your experience.';
        valid = false;
    }
    
    if (message === '' || message === undefined ) {
        error_message.innerText = 'Message is required.';
        valid = false;
    }
    
    // If all validations pass
    return valid;
}
