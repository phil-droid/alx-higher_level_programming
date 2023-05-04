$(document).ready(function() {
  $('DIV#toggle_header').click(function() {
    const $headerElem = $('header');
    if ($headerElem.hasClass('red')) {
      $headerElem.removeClass('red');
      $headerElem.addClass('green');
    } else {
      $headerElem.removeClass('green');
      $headerElem.addClass('red');
    }
  });
});
