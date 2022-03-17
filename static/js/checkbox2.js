$(function() {

  let slct_all_id = "#sca"
  let slct_box_name = "input[name='select-companies']"
  let slct_box_id = "#cbcomp"

  let slct_box_count = $(slct_box_id+" :input").length
  let slct_box_checked = slct_box_id+" :checked"
  var $button_submit = $(".button-submit")

  // 1. 「全選択」する
  $(slct_all_id).on('click', function() {
    $button_submit.addClass("show");
    $(slct_box_name).prop('checked', this.checked);
  });
  // 2. 「全選択」以外のチェックボックスがクリックされたら、
  $(slct_box_name).on('click', function() {
    $button_submit.addClass("show");
    if ($(slct_box_checked).length == slct_box_count) {
      // 全てのチェックボックスにチェックが入っていたら、「全選択」 = checked
      $(slct_all_id).prop('checked', true);
    } else {
      // 1つでもチェックが入っていなかったら、「全選択」 != checked
      $(slct_all_id).prop('checked', false);
    }
  });
});
