
/*registration lightbox
$(document).ready(function(){
	$('#sign_up').hide();

	$('#registerButton').click(function(){
		var popMargTop = ($(window).height() -300) / 2;
		var popMargLeft = ($(window).width() -400) / 2;
		
		$('#sign_up').css({
			'margin-top' : popMargTop,
			'margin-left': popMargLeft
		});
			
		$('#sign_up').fadeIn(300);
		
		$('body').append('<div id="mask"></div>')
		$('#mask').fadeIn(300);
		return false;
	});
	
	$('a.close, #mask, #cancel').live('click', function(){
		$('#mask, #sign_up').fadeOut(300, function() {
			$('#mask').remove()
		});
	});
}); */


