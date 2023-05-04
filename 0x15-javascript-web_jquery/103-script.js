$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';

  function translateHello() {
    const langCode = $('INPUT#language_code').val();
    if (langCode !== '') {
      $.get(url, { lang: langCode }, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  }

  $('INPUT#btn_translate').click(translateHello);

  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
