(function() {
  const articleLinks = document.querySelectorAll("article a")
  Array.from(articleLinks).forEach(el => {
    el.id = "ref-" + el.href.split('#')[1]
  })
  
}())