$(function () {
  var topBtn = $('#topBtn');
  topBtn.hide();
  //スクロールが100に達したらボタン表示
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      topBtn.fadeIn();
    } else {
      topBtn.fadeOut();
    }
  });
  //スルスルっとスクロールでトップへもどる
  topBtn.click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 800);
    return false;
  });
});
