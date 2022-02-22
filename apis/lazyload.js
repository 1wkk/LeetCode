/**
 * image lazy load
 */

let images = [...document.querySelectorAll('img')]

// Traditional
const lazy_load = () => {
  let count = 0
  return () => {
    const deletes = []
    images.forEach((image, index) => {
      const rect = image.getBoundingClientRect()
      if (rect.top < window.innerHeight) {
        // dataset.src = data-src
        image.src = image.dataset.src
        deletes.push(index)
        count++
        if (count === images.length) {
          document.removeEventListener('scroll', lazy_load)
        }
      }
    })
    images = images.filter((_, index) => !deletes.includes(index))
  }
}

document.addEventListener('scroll', lazy_load)

// IntersectionObserver API
const lazy_load_intersection_observer = () => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.intersectionRatio > 0) {
        entry.target.src = entry.target.dataset.src
        observer.unobserve(entry.target)
      }
    })
  })
  images.forEach(image => observer.observe(image))
}
