var crudOperation = function () {

    var self = this;
    //Mandatory function to be implemented here
    var initialization = function () {

    }
    var registration = function () {
        $(document).on("click", "#btn_register", register);
        $(document).on("click", "#btn_login", login);
    }


var register = function(e){
 console.log("hello register");
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/register',
                data: $('#registration-form').serialize(),
                success: function(response) {
                debugger;
                    alert(response.data);
                    window.location.href = '/login';
                },
                error: function(response) {
                debugger;

                    var errors = response.responseJSON.errors;
                    for (var field in errors) {
                        alert(errors[field]);
                    }
                }
            });

        }

var login = function(e) {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/login',
                data: $('#login-form').serialize(),
                success: function(response) {
                    $(".toast-body").html(response.data);
//                    alert(response.data);
                    window.location.href = response.redirect_url;
                },
                error: function(response) {
                    var errors = response.responseJSON.errors;
                    for (var field in errors) {
                        alert(errors[field]);
                    }
                }
            });
        }

function toast1(){
    $('.toast-body').html("Hello test toast");
        $(".toast").toast('show');
    }

self.init = function () {
        initialization();
        registration();
    }
}