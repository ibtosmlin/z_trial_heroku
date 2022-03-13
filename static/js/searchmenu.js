$(function () {
  var $Si = $('#searchicon');
  var $Menu = $('#menu');
  var $Circle = $("#circle-bg");
//  var $Menu_c = $('#menu_child');

  $Si.click(function(){
    if($Si.text() == 'search') {
    // si: close Menu: 表示; rbox: 非表示
      $Si.toggleClass('siactive');//ナビゲーションにpanelactiveクラスを付与
      $Si.text('close')
      $Menu.toggleClass('siactive');//ナビゲーションにpanelactiveクラスを付与
      $Circle.toggleClass('siactive');//丸背景にcircleactiveクラスを付与
    }
    else {
    // si: serch Menu: 非表示; rbox: 表示
    $Si.removeClass('siactive');//ナビゲーションのpanelactiveクラスを除去
    $Si.text('search')
      $Menu.removeClass('siactive');//ナビゲーションのpanelactiveクラスを除去
      $Circle.removeClass('siactive');//丸背景のcircleactiveクラスを除去
    }
  })
});
