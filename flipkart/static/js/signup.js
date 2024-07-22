function validate(){

    var uname = document.getElementById('uname').value;
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var con_password = document.getElementById('con_password').value;
    var uname_error = document.querySelector('.uname-error');
    var fname_error = document.querySelector('.fname-error');
    var lname_error = document.querySelector('.lname-error');
    var email_error = document.querySelector('.email-error');
    var password_error = document.querySelector('.password-error');
    var con_password_error = document.querySelector('.con-password-error');
    var password_match_error = document.querySelector('.password-match-error');

    uname_error.innerText = '';
    fname_error.innerText = '';
    lname_error.innerText = '';
    email_error.innerText = '';
    password_error.innerText = '';
    con_password_error.innerText = '';
    password_match_error.innerText = '';

    var valid = true;

    if (uname.trim() === ''){
        uname_error.innerText = 'User name is required';
        valid = false;
    }
    if (fname.trim() === ''){
        fname_error.innerText = 'First name is required';
        valid = false;
    }
    if (lname.trim() === ''){
        lname_error.innerText = 'Last name is required';
        valid = false;
    }
    if (email.trim() === ''){
        email_error.innerText = 'Email is required';
        valid = false;
    }
    if (password.trim() === ''){
        password_error.innerText = 'Password is required';
        valid = false;
    }
    if (con_password.trim() === ''){
        con_password_error.innerText = 'Conform Password is required';
        valid = false;
    }
    else if (password.trim() != con_password.trim()){
        password_match_error.innerText = 'Conform Password mismatch with the Password';
        valid = false;
    }

    return valid;
}