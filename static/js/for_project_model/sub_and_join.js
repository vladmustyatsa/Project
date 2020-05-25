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
			if (result.status == 'ok_subed'){
				$('#sub_btn').removeClass('my-button');
				$('#sub_btn').addClass('btn-secondary');
				$('#sub_btn').addClass('casual-button');
				$('#sub_btn').css({'border':'none'});
				
				$('#sub_counter').text(parseInt($('#sub_counter').text()) + 1);
			}
			if (result.status == 'ok_unsubed'){
				$('#sub_btn').addClass('my-button');
				$('#sub_btn').removeClass('btn-secondary');
				$('#sub_btn').removeClass('casual-button');
				$('#sub_btn').css({'border':'none'});
				$('#sub_counter').text(parseInt($('#sub_counter').text()) - 1);
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
			console.log(result)
			if (result.status == 'must_login'){
				let url = new URL(window.location.origin+'/api/unauthorized');
				url.searchParams.append('next','/projects/'+result.team_name);
				url.searchParams.append('message','Please sign in to join');
				window.location.assign(url);
			}
			if (result.status == 'ok'){
				/*$('#join_btn').removeClass('my-button');
				$('#join_btn').removeClass('ts-warn-button');
				$('#join_btn').addClass('btn-secondary');
				$('#join_btn').addClass('casual-button');*/
				$('#join_btn').addClass('ts-warn');
				$('#join_btn').css({'border':'none', 'color':'grey'});
				$('#join_text').text('Request was sent');
				$('#delete_req').css({'display':'inline'});
				$('#join_btn').attr('disabled','');
			}
		}
		);
	});
	$('#delete_req').on('click', function() {
		$.post(document.location,
		{
			'status':'delete_req'
		},
		function(result){
			console.log(result);
			$('#join_text').text('Join');
			$('#delete_req').css({'display':'none'});
			$('#join_btn').removeClass('ts-warn');
			$('#join_btn').css({'border':'none', 'color':'white'});
			$('#join_btn').attr('disabled',null);
		}
		);
	});
});