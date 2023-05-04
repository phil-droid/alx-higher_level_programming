$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('uL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('uL.my_list').empty();
  });
});
