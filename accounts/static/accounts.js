/**
 * Created by yangjun on 16/8/14.
 */

var initialize = function(navigator, user, token, urls){
    $('#id_login').on('click', function(){
        console.log("id_login click");
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function(assertion){
            console.log("onlogin called");
            $.post(
                urls.login,
                {assertion:assertion, csrfmiddlewaretoken:token}
            )
                .done(function() {console.log("reload windows"); window.location.reload();})
                .fail(function() {navigator.id.logout();})
        },
        onlogout: function() {}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
