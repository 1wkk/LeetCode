// @ts-check
const debounce = (
  func,
  time = 17,
  options = {
    first: true,
    ctx: null
  }
) => {
  let timer
  const _debounce = (...args) => {
    if (timer) {
      clearTimeout(timer)
    }
    if (options.leading && !timer) {
      timer = setTimeout(null, time)
      func.apply(options.ctx, args)
    } else {
      timer = setTimeout(() => {
        func.apply(options.ctx, args)
        timer = null
      }, time)
    }
  }

  _debounce.cancel = () => {
    clearTimeout(timer)
    timer = null
  }

  return _debounce
}
