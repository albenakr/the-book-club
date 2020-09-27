  // Update quantity on click
  $(".update-link").click(function (e) {
    var form = $(this).prev(".update-form");
    form.submit();
  });

  // Remove item and reload on click - books
  $(".remove-item-book").click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr("id").split("remove_")[1];
    var url = `/bag/remove/${itemId}/`;
    var data = { csrfmiddlewaretoken: csrfToken };

    $.post(url, data).done(function () {
      location.reload();
    });
  });

  // Remove item and reload on click - plans
  $(".remove-item-plan").click(function (e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr("id").split("remove_plan_")[1];
    var url = `/bag/remove_plan/${itemId}/`;
    var data = { csrfmiddlewaretoken: csrfToken };

    $.post(url, data).done(function () {
      location.reload();
    });
  });
