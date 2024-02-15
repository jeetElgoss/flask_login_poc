var crudOperation = function () {

    var self = this;
    //Mandatory function to be implemented here
    var initialization = function () {

    }
    var registration = function () {
        $(document).on("click", "#btn_register", btn_check);
//        $(document).on("click", "#btn_register", register);
        $(document).on("click", "#login", login);
    }

    var btn_check = function(e){
            e.preventDefault();

    console.log("Btn -registration");
    }

 var register = function(e){
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/register',
                data: $('#registration-form').serialize(),
                success: function(response) {
                debugger;
                    console.log(response.data);
//                    window.location.href = '/login';
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

var login = $('#login-form').submit(function(e) {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/register',
                data: $('#registration-form').serialize(),
                success: function(response) {
                    console.log(response.data);
//                    window.location.href = '/login';
                },
                error: function(response) {
                    var errors = response.responseJSON.errors;
                    for (var field in errors) {
                        alert(errors[field]);
                    }
                }
            });
        });
self.init = function () {
        initialization();
        registration();
    }
}