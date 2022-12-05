$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/homepage";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/homepage";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

function checkFileSize() {
  const FS = document.getElementById("FS");
  const files = FS.files;

  // If there is (at least) one file selected
  if (files.length > 0) {
    if (files[0].size > 75 * 1024) {
      // Check the constraint
      FS.setCustomValidity("The selected file must not be larger than 75 kB");
      return;
    }
  }
  // No custom constraint violation
  FS.setCustomValidity("");
}
