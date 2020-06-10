$(document).ready(function() {
	$('button').on('click', function() {
		if ($(this).attr('id') !== undefined) {
			if ($(this).attr('id').indexOf('unsend_') !== -1){
				var project = $(this).attr('id').split('');
				project = project.splice(7, project.length - 7);
				project = project.join('')
				console.log(project)
				$.post(document.location,{
					status : 'unsend',
					project : project
				},
				function(result){
					if (result.status == "req_deleted"){
						$(`#${project}`).remove();
						if ($('#reqs').html().trim() === ''){
							$('#reqs').append(`<div class="text-center">
					<span class="text-muted">You haven't sent any request</span>
				</div>`)
						}
					}
				})
			}
		}
	});
});