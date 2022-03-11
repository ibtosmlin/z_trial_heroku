$(function () {
  var $sibox = $('#sicheckbox');
  var $Menu = $('#menu');
  var $Menu_c = $('#menu_child');
  var $rbox = $("#resultbox");

  $sibox.change(function(){
  if($sibox.prop("checked") == true) {
    // Menu 表示; rbox 非表示
    $rbox.removeClass("rbox_visible");
    $rbox.addClass("rbox_shrink");
    $Menu.removeClass("menu_shrink");
    $Menu.addClass("menu_dropdown");
    $Menu_c.removeClass("menu_child_shrink");
    $("#menu").toggleClass('panelactive');//ナビゲーションにpanelactiveクラスを付与
    $(".circle-bg").toggleClass('circleactive');//丸背景にcircleactiveクラスを付与
  }
  else {
    // Menu 非表示; rbox 表示
    $Menu_c.addClass("menu_child_shrink");
    $Menu.removeClass("menu_dropdown");
    $Menu.addClass("menu_shrink");
    $rbox.removeClass("rbox_shrink");
    $rbox.addClass("rbox_visible");
  }})
});
