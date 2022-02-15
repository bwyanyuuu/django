/*
	ZeroFour by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Dropdowns.
		$('#nav > ul').dropotron({
// 			offsetY: -22,
            // offsetX: 500,
            alignment: 'right',
			expandMode: 'click',
			mode: 'fade',
			noOpenerFade: true,
			speed: 'fast',
			detach: false
		});

	// Nav.

		// Title Bar.
			$(
				'<div id="titleBar">' +
					'<a href="#navPanel" class="toggle"></a>' +
					'<span class="title">' + $('#logo').html() + '</span>' +
				'</div>'
			)
				.appendTo($body);

		// Panel.
			$(
				'<div id="navPanel">' +
					'<nav>' +
						$('#nav').navList() +
						'<a class="link depth-0" href="/accounts/logout/"><span class="indent-0"></span>Log Out</a>' +
					'</nav>' +
				'</div>'
			)
				.appendTo($body)
				.panel({
					delay: 500,
					hideOnClick: true,
					hideOnSwipe: true,
					resetScroll: true,
					resetForms: true,
					side: 'left',
					target: $body,
					visibleClass: 'navPanel-visible'
				});

})(jQuery);
$(function(){
    var $li = $('ul.tab-title li').not('.date-tab');
        $($li. eq(0) .addClass('active').find('a').attr('href')).siblings('.tab-inner').hide();
        
        $li.click(function(){
            if ($(this).hasClass('extra'))
                return;
            $($(this).find('a'). attr ('href')).show().siblings ('.tab-inner').hide();
            $(this).addClass('active'). siblings ('.active').removeClass('active');
        });
    });
    
    var $lid = $('ul.tab-title li.date-tab');
        $($lid. eq(3) .addClass('active').find('a').attr('href')).siblings('.tab-inner').hide();
        
        $lid.click(function(){
            if ($(this).hasClass('extra'))
                return;
            $($(this).find('a'). attr ('href')).show().siblings ('.tab-inner').hide();
            $(this).addClass('active'). siblings ('.active').removeClass('active');
        });


$(function(){
	$('.sd-time').click(function(){
			console.log($(this).hasClass('hidden'))
			if($(this).hasClass('hidden')){
				$(this).next().slideDown()
				$(this).removeClass('hidden')
			}
			else{
				$(this).next().slideUp()
				$(this).addClass('hidden')
			}
		});
	});