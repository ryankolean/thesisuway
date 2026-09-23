/* The Sisu Way - concept site.
   One job: links marked aria-disabled (store badges, the web-app button) do nothing until they go live. */
(function () {
  'use strict';
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[aria-disabled="true"]');
    if (a) { e.preventDefault(); }
  });
})();
