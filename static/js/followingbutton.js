$('#topBtn').load(function(){
    $('#topBtn').click(function () { // #topBtnをクリックすると
        $('body,html').animate({ // いちばん上にanimateする
        scrollTop: 0 // 戻る位置
        }, 400); // 戻るスピード
        return false;
    });
});
