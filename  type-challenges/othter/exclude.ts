type $Exclude<T, K> = T extends K ? never : T

import { Equal, Expect } from '@type-challenges/utils'

type cases = [Expect<Equal<'b' | 'c', $Exclude<'a' | 'b' | 'c', 'a'>>>]

type ans = $Exclude<'a' | 'b' | 'c', 'a'>
