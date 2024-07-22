function validate(){

    var uname_or_email = document.getElementById('uname_or_email').value;
    var password = document.getElementById('pwd').value;
    var uname_error = document.querySelector('.uname-error');
    var password_error = document.querySelector('.password-error');
    var invalid_error = document.querySelector('.invalid-error');

    uname_error.innerText = '';
    password_error.innerText = '';
    invalid_error.innerText = '';

    var valid;

    if (uname_or_email.trim() === ''){
        uname_error.innerText = 'User name or Email is required';
        valid = false;
    }
    if (password.trim() === ''){
        password_error.innerText = 'Password is required';
        valid = false;
    }

    return valid;
}