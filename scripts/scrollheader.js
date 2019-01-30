( function( window, $, undefined ) {

    'use strict';

    $(document).ready(function() {

      function is_scrolling() {

        var $element = $('.site-header'),
            $nav_height = $element.outerHeight( true );

        if ($(this).scrollTop() >= $nav_height ) {

          $element.addClass( 'is-scrolling');

        } else {

          $element.removeClass( 'is-scrolling');
        }

      }

    $( window ).scroll(_.throttle(is_scrolling, 200));

  });

})(this, jQuery);
