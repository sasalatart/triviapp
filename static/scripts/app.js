$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .remove();
  });

$('.ui.answer.card')
  .on('click', function() {
    $('#answer').val($(this).data('answer'));
    $('.ui.answer.card').css('background-color', 'white');
    $(this).css('background-color', 'green');
  });
