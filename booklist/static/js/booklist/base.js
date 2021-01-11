// ホバー→表示・非表示：カード作成
$(function () {
  $('.table-wrapper').hover(
    function () {
      $(this).find('.card-create').removeClass('hidden');
    },
    function () {
      $(this).find('.card-create').addClass('hidden');
    });
});

// ホバー→表示・非表示：カード編集、削除
$(function () {
  $('tr').hover(
    function () {
      $(this).find('.card-icon-btn').removeClass('hidden');
    },
    function () {
      $(this).find('.card-icon-btn').addClass('hidden');
    });
});


$('.dropdown').dropdown();
