
$(document).ready(function() {
	$('#demo-slidebottom input').click(function() {
		$('#inner').animate({width: '200px'});
		$('#demo-slidebottom input').hide('fast');
		$('#image-settings').css('display', 'block');
		$('#image-settings-1').css('display', 'block');
		$('#image-settings-2').css('display', 'block');
		$('#ig1').css('display', 'block');
		$('#ig2').css('display', 'block');
		$('#ig3').css('display', 'block');
		$('#so-image').css('display', 'block');
		$('#so-image-1').css('display', 'block');
		$('#so-image-2').css('display', 'block');
		$('#p-setting').css('display', 'block');
		$('#p-setting1').css('display', 'block');
		$('#p-setting2').css('display', 'block');
	});
});

$(document).ready(function() {
	$(".logo").click(function() {
		$('#inner').animate({width: '0%'});
		$('#demo-slidebottom input').show('fast');
		$('#submit-changes').css('display', 'none');
		$('#image-settings').css('display', 'none');
		$('#image-settings-1').css('display', 'none');
		$('#image-settings-2').css('display', 'none');
		$('#ig1').css('display', 'none');
		$('#ig2').css('display', 'none');
		$('#ig3').css('display', 'none');
		$('#so-image').css('display', 'none');
		$('#so-image-1').css('display', 'none');
		$('#so-image-2').css('display', 'none');
		$('#p-setting').css('display', 'none');
		$('#p-setting1').css('display', 'none');
		$('#p-setting2').css('display', 'none');
	});
});

$(document).ready(function () {
    $('#list > li').click(function (event) {
        $(this).children("ul").slideToggle();
        event.stopPropagation();
    });
});

$(document).ready(function () {
	$('#change-input').click(function (event)  {
		$(this).attr('type','text');
		$('#submit-changes').css('display', 'block');
	});
});

// function getCookie(name){
//     var cookieValue = null;
//     if(document.cookie && document.cookie != '' ){
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++){
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name wewant?
//             if ( cookie.substring(0, name.length + 1 ) == (name + '=') ){
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');
// function csrfSafeMethod(method){
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings){
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain){
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

$(document).ready(function () {
	$('#like').click(function (event)  {
		$.ajax({
			url: "/post_liked/",
			type: "GET",
			data: $("#form-like").serialize(),
			success: function (data) {
				console.log('ok')
				print("ok")
			}
		});
	});
});