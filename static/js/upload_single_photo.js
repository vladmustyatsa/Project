$(document).ready(function() {
	var avatar_input = document.getElementById('avatar_input');
	avatar_input.oninput = function() {
		var formdata = new FormData();
		file = $(this).prop('files')[0];
		console.log(file['file']);
		formdata.append("avatar_file", file);
		$.ajax({
			url: '/test',
			type: "POST",
			data: formdata,
			processData: false,
			contentType: false,
			success: function (result) {
				console.log(result);
				var avatar_view = $('#avatar_view');
				avatar_view.attr('src','/static/'+result['filename']) 
			}
		});

	};
});