$(function () {
  var $Sistatus = true;
  var $Sisearch = $('#search');
  var $Siclose = $('#close');
  var $Si = $('#searchicon');
  var $Menu = $('#menu');
  var $Circle = $("#circle-bg");


  $Si.click(function(){
    if($Sistatus) {
      // si: close Menu: 表示; rbox: 非表示
      $Sisearch.css('display','none');
      $Sisearch.css('opacity',0);
      $Siclose.css('display','block');
      $Siclose.animate({opacity: 1}, 1000);

      $Circle.css('z-index', 80);
      $Circle.css( { transform: "scale(50)" } );
      $Menu.css('z-index', 100);
      $Menu.animate({opacity:1}, 1000);

      $Sistatus = false;
  }
    else {
      // si: serch Menu: 非表示; rbox: 表示
      $Siclose.css('display','none');
      $Siclose.css('opacity',0);
      $Sisearch.css('display','block');
      $Sisearch.animate({opacity: 1}, 1000);

      $Menu.animate({opacity:0}, 100);
      $Circle.css( { transform: "scale(0)" } );
      $Menu.css('z-index', 10);
      $Circle.css('z-index', 10);

      $Sistatus = true;
    }
  })
});
