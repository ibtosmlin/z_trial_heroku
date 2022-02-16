$(function() {
    $("#searchicon").on("click", function() {
      if($(this).text() == "search") {
        $(this).text("close");
        $("#menu").removeClass("dropdown");
      } else {
        $(this).text("search");
        $("#menu").addClass("dropdown");
      }
    });
  });
