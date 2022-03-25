$(function () {
  var $Sistatus = true;
  var $Sisearch = $('#search');
  var $Siclose = $('#close');
  var $Si = $('#searchicon');
  var $Menu = $('#menu');

  $Si.click(function(){
    if($Sistatus) {
      // si: close Menu: 表示; rbox: 非表示
      $Sisearch.css('display','none');
      $Sisearch.css('opacity',0);
      $Siclose.css('display','block');
      $Siclose.animate({opacity: 1}, 1000);
      $Menu.addClass("sitrue")
      $Sistatus = false;
  }
    else {
      // si: serch Menu: 非表示; rbox: 表示
      $Siclose.css('display','none');
      $Siclose.css('opacity',0);
      $Sisearch.css('display','block');
      $Sisearch.animate({opacity: 1}, 1000);
      $Menu.removeClass("sitrue")
      $Sistatus = true;
    }
  })
});


$(function () {
  var $Cfstatus = true;
  var $Ci = $('#contacticon');
  var $Cf = $('#contactform');

  $Ci.click(function(){
    if($Cfstatus) {
      // si: close Menu: 表示; rbox: 非表示
      $Cf.addClass("cftrue")
      $Cfstatus = false;
  }
    else {
      // si: serch Menu: 非表示; rbox: 表示
      $Cf.removeClass("cftrue")
      $Cfstatus = true;
    }
  })
});
