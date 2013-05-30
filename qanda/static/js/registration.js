// add remove secondary classes		
$(document).ready(function() {
	$('#btnAdd').click(function() {
		var num     = $('.classInputs').length;
		var newNum  = new Number(num + 1);
		var newElem = $('#input' + num).clone().attr('id', 'input' + newNum);

		newElem.children(':first').attr('id', 'name' + newNum).attr('name', 'name' + newNum);
		$('#input' + num).after(newElem);
		$('#btnDel').attr('disabled','');

		if (newNum == 6)
			$('#btnAdd').attr('disabled','disabled');
	
	});

	$('#btnDel').click(function() {
		var num = $('.classInputs').length;

		$('#input' + num).remove();
		$('#btnAdd').attr('disabled','');

		if (num-1 == 1)
			$('#btnDel').attr('disabled','disabled');

	});

	$('#btnDel').attr('disabled','disabled');
});


// Dropdowns to select course/class/prof
$(document).ready(function(){

	$('#courseSelection').hide();
	$('#profSelection').hide();

	$("#course_title").change(function(){
	   correspondingID = $(this).find(":selected").val()
	   $("#" + correspondingID).show();
	})	
	$("#class_title").change(function(){
	   correspondingID = $(this).find(":selected").val()
	   $("#profSelection").show();
	})
})



