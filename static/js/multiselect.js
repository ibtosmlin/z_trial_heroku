$(function () {
    $('select').multipleSelect({
    width: 200,
    formatSelectAll: function() {
        return 'すべて';
    },
    formatAllSelected: function() {
        return '全て選択されています';
    }
});
});
