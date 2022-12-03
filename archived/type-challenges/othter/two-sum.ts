type ToTuple<A extends number, T extends any[] = []> = T extends { length: A }
  ? T
  : ToTuple<A, [...T, any]>

type Add<A extends number, B extends number> = [
  ...ToTuple<A>,
  ...ToTuple<B>
]['length']

type Sub<A extends number, B extends number> = ToTuple<A> extends [
  ...ToTuple<B>,
  ...infer C
]
  ? C['length']
  : never

type Tail<T extends any[]> = T extends [infer F, ...infer V] ? V : []

type ToUnion<T extends any[]> = T[number]

type TwoSum<T extends number[], V extends number> = T['length'] extends 0
  ? false
  : Sub<V, T[0]> extends never // fix
  ? false
  : Sub<V, T[0]> extends ToUnion<Tail<T>>
  ? true
  : TwoSum<Tail<T>, V>

type cases = [
  TwoSum<[2, 7, 11, 15], 3>,
  TwoSum<[2, 7, 11, 15], 9>,
  TwoSum<[2, 7, 11, 15], 19>,
  TwoSum<[2, 7, 11, 15], 18>
]
