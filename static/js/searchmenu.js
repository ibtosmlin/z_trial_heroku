const _sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));


$(function () {
  var $Sistatus = true;
  var $Sisearch = $('#search');
  var $Siclose = $('#close');
  var $Si = $('#searchicon');
  var $Menu = $('#menu');
  var $Bs = $('button[type="submit"]');

  $Si.click(function(){
    if($Sistatus) {
      // si: close Menu: 表示; rbox: 非表示
      $Sisearch.css('display','none');
      $Sisearch.css('opacity',0);
      $Siclose.css('display','block');
      $Siclose.animate({opacity: 1}, 1000);
      $Menu.addClass("sitrue")
      await _sleep(1000);
      $Bs.css('display','block');

      $Sistatus = false;
  }
    else {
      // si: serch Menu: 非表示; rbox: 表示
      $Siclose.css('display','none');
      $Siclose.css('opacity',0);
      $Sisearch.css('display','block');
      $Sisearch.animate({opacity: 1}, 1000);
      $Menu.removeClass("sitrue")
      await _sleep(1000);
      $Bs.css('display','none');

      $Sistatus = true;
    }
  })
});
