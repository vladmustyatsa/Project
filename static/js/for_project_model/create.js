$(document).ready(function() {
	
	var tags = [];
	var select = document.getElementById('tags');
	
	for (var option of select.selectedOptions){
		var tag = option.text;
		tags.push(tag);
		var tag_link = tag.replace('#','');
		var html = `<a href="/tags/${tag_link}"" id="${tag_link}" class="link">${tag} </a>`;
		$('#tag_list').append(html);
	}
	$('#tags').on('changed.bs.select', function(event, clickedIndex, isSelected, previousValue){
		var tag = select[clickedIndex].text;
		if (isSelected){
			
			tags.push(tag);
			var tag_link = tag.replace('#','');
			var html = `<a href="/tags/${tag_link}"" id="${tag_link}" class="link">${tag} </a>`;
			$('#tag_list').append(html);
		}
		else{
			tags.pop(tag);
			$(tag).remove();
		}

	});	

});