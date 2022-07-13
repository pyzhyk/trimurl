function copyShortUrl() {
  var copyText = document.getElementById("shorturl");
  navigator.clipboard.writeText(copyText.href);
}
