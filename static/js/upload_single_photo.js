function upload_single_photo(url) {
	var avatar_input = document.getElementById('avatar_input');
	avatar_input.oninput = function() {
		var formdata = new FormData();
		file = $(this).prop('files')[0];
		console.log(file['file']);
		formdata.append("avatar_file", file);
		formdata.append("status", "for_avatar");
		$.ajax({
			url: url,
			type: "POST",
			data: formdata,
			processData: false,
			contentType: false,
			success: function (result) {
				console.log(result);
				var avatar_view = $('#avatar_view');
				avatar_view.attr('src','/static/'+result['filename']);
				$('#navbar_avatar').attr('src','/static/'+result['filename']);
			}
		});

	};
}