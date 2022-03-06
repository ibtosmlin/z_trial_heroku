$(function () {

   var $rbox = $("#resultbox");
   var $card = $(".card");

   let emptyCells = [];//空の配列を作っておく
   let parentWidth = $rbox.width();//rbox(sectionの親要素)の幅を取得
   let childWidth = $card.outerWidth(true);//list-itemnの幅を取得
   let column = parentWidth / childWidth;//親要素の幅を子要素の幅を割ったものがカラム数になる
   column = Math.floor(column);//カラム数の小数点切り捨て
   let count = $card.length;//list-itemの数を取得
   let number = count % column;//list-itemの数をカラムで割った余りを出す、余りの値が最後列の要素数になる。
   let need = column - number;//カラム数から最後列の要素数を引いたものが、必要な要素数になる。
   for (i = 0; i < need; i++) {
      emptyCells.push($('<section>', { class: 'blankcard' }));//必要分の空のを配列に追加
   }

   $rbox.append(emptyCells);//list-itemの最後に空の要素を追加する。

});
