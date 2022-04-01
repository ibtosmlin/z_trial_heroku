// topBtn
$(function () {
  var topBtn = $('#topBtn');
  topBtn.hide();
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      topBtn.fadeIn();
    } else {
      topBtn.fadeOut();
    }
  });
  topBtn.click(function () {
    $('body, html').animate({
        scrollTop: 0
    }, 800);
    return false;
  });
});

// cardsの端数処理
$(function () {
  var $rbox = $("#cards");
  var $card = $(".card");
// cardの配列が端数を持つ場合に左詰めにする
  let emptyCells = [];//空の配列を作っておく
  let parentWidth = $rbox.width();//rbox(sectionの親要素)の幅を取得
  let childWidth = $card.outerWidth(true);//list-itemnの幅を取得
  let column = parentWidth / childWidth;//親要素の幅を子要素の幅を割ったものがカラム数になる
  column = Math.floor(column);//カラム数の小数点切り捨て
  let count = $card.length;//list-itemの数を取得
  let number = count % column;//list-itemの数をカラムで割った余りを出す、余りの値が最後列の要素数になる。
  let need = column - number;//カラム数から最後列の要素数を引いたものが、必要な要素数になる。
  for (i = 0; i < need; i++) {
  emptyCells.push($('<section>', { class: 'blank-card' }));//必要分の空のを配列に追加
  }
  $rbox.append(emptyCells);//list-itemの最後に空の要素を追加する。
});

// hmbのクリック
$(function(){
  $('#hmb-menu').hide();
  $('#hmb').on('click', function() {
    $(this).toggleClass('active');
    $("#hmb-menu").slideToggle(600);
    return false;
  });
});



$('input[name="hmbItem"]').click(function() {
  var r = $('input[name="hmbItem"]:checked').val();
  if(r=='Home'){
    $('input[value="Home"]').prop('checked', true);
  }
  if(r=='About'){
    $('input[value="About"]').prop('checked', true);
  }
  if(r=='Search'){
    $('input[value="Search"]').prop('checked', true);
  }
})

$('input[name="slideItem"]').click(function() {
  var r = $('input[name="slideItem"]:checked').val();
  if(r=='Home'){
    $('input[value="Home"]').prop('checked', true);
  }
  if(r=='About'){
    $('input[value="About"]').prop('checked', true);
  }
  if(r=='Search'){
    $('input[value="Search"]').prop('checked', true);
  }
})