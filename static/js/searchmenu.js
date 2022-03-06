$(function () {
  var $sibox = $('#sicheckbox');
  var $Menu = $('#Menu');
  var $Menu_c = $('#Menu_child');
  var $rbox = $("#resultbox");

  $sibox.change(function(){
  if($sibox.prop("checked") == true) {
    // 表示
    $rbox.addClass("rbox_shrink");
    $Menu_c.removeClass("Menu_child_shrink");
    $Menu.removeClass("Menu_shrink");
    $Menu.addClass("Menu_dropdown");

  }
  else {
    // 非表示
    $Menu_c.addClass("Menu_child_shrink");
    $Menu.removeClass("Menu_dropdown");
    $Menu.addClass("Menu_shrink");
    $rbox.removeClass("rbox_shrink");
  }})
});
