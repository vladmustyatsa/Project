function delete_model(url) {
	$('#delete_button').on('click',function() {

		$.post(url,
		{
			'status':'delete'
		},
		function(){

			window.location = '/'
		}

		);

	});
}


