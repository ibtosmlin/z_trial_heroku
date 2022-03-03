$(function () {
  var sIcon = $('#searchicon');
  var Menu = $('#menu');
  var Menu_c = $('#menu_child');
  //ボタン表示
  sIcon.click(function (){

  if(sIcon.text() == "search") {
    sIcon.text("close");
    // 表示
    Menu_c.removeClass("menu_child_shrink");
    Menu.removeClass("menu_shrink");
    Menu.addClass("menu_dropdown");
  }
  else {
    sIcon.text("search");
    // 非表示
    Menu_c.addClass("menu_child_shrink");
    Menu.removeClass("menu_dropdown");
    Menu.addClass("menu_shrink");
  }
})
});
