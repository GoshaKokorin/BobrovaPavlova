window.addEventListener('DOMContentLoaded', function() {
  // Аккордеон
  $(function() {
    $("#accordion").accordion({
      collapsible: true,
      active: false,
      heightStyle: "content",
      header: "h3"
    });
  });
})