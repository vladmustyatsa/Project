$(document).ready(function() {
	$('#sub_btn').on('click', function() {
		$.post(document.location,
		{
			'status':'sub'
		},
		function(result){
			if (result.status == 'must_login'){
				/*let url = new URL(window.location.origin+'/signin');
				url.searchParams.append('next','/projects/'+result.team_name)
				window.location.assign(url);*/
				let url = new URL(window.location.origin+'/api/unauthorized');
				url.searchParams.append('next','/projects/'+result.team_name);
				url.searchParams.append('message','Please sign in to subscribe');
				window.location.assign(url);
			}
			if (result.status == 'ok'){
				$('#sub_btn').removeClass('my-button');
				$('#sub_btn').addClass('btn-secondary');
				$('#sub_btn').addClass('casual-button');
				$('#sub_btn').css({'border':'none'});
				$('#sub_btn').attr('disabled','');
				$('#sub_counter').text(parseInt($('#sub_counter').text()) + 1);

			}
		}
		);
	});
	$('#join_btn').on('click', function() {
		$.post(document.location,
		{
			'status':'join'
		},
		function(result){
			if (result.status == 'must_login'){
				let url = new URL(window.location.origin+'/api/unauthorized');
				url.searchParams.append('next','/projects/'+result.team_name);
				url.searchParams.append('message','Please sign in to join');
				window.location.assign(url);
			}
		}
		);
	});
});