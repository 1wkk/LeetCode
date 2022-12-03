import { randTo } from './random'

const shuffle = (list: Array<any>) => list.sort(() => Math.random() - 0.5)

// 随机生成六位数的手机验证码(重复/不可重复)
const vc = ({ len = 6, repeat = true } = {}) => {
  if (len > 10 && repeat === false) {
    throw new Error('len should less equal than 10 if repeat is false')
  }
  if (repeat) {
    return Array(len)
      .fill(0)
      .map(() => randTo(9))
  } else {
    return shuffle([...Array(10).keys()]).slice(0, len)
  }
}

console.log(vc())
console.log(vc({ len: 9 }))
console.log(vc({ repeat: false }))
console.log(vc({ len: 9, repeat: false }))
console.log(vc({ len: 11, repeat: false }))

// 学习一下 Array.from
