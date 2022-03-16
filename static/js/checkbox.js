$(function() {
  $all = $('#sya')
  $name = $("input[name='select-years']")
  $boxchecked = $("#cbyear :checked")
  $boxinput = $("#cbyear :input")

  // 1. 「全選択」する
  $all.on('click', function() {
    $name.prop('checked', this.checked);
  });
  // 2. 「全選択」以外のチェックボックスがクリックされたら、
  $name.on('click', function() {
    if ($boxchecked.length == $boxinput.length) {
      // 全てのチェックボックスにチェックが入っていたら、「全選択」 = checked
      $all.prop('checked', true);
    } else {
      // 1つでもチェックが入っていなかったら、「全選択」 != checked
      $all.prop('checked', false);
    }
  });
});