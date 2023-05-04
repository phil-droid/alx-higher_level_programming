$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + langCode;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
