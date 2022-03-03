$(function () {
  var sIcon = $('#searchicon');
  var Menu = $('#menu');
  //ボタン表示
  sIcon.click(function (){

  if(sIcon.text() == "search") {
    sIcon.text("close");
    Menu.removeClass("shrink");
    Menu.addClass("dropdown");
  }
  else {
    sIcon.text("search");
    Menu.removeClass("dropdown");
    Menu.addClass("shrink");
  }
})
});
