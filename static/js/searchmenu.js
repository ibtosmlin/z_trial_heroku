$(function () {
  var sIcon = $('#searchicon');
  var Menu = $('#menu');
  //ボタン表示
  sIcon.click(function (){

  if(sIcon.text() == "search") {
    sIcon.text("close");
    Menu.removeClass("menu_shrink");
    Menu.addClass("menu_dropdown");
  }
  else {
    sIcon.text("search");
    Menu.removeClass("menu_dropdown");
    Menu.addClass("menu_shrink");
  }
})
});
