function maxNumberOfBalloons(text: string): number {
    const map_get = (map, k) => map[k] || 0
    // balloon
    let ans = Infinity
    const map = {}
    for (const c of text) {
        map[c] = map_get(map, c) + 1
    }
    ans = Math.min(
        map_get(map, 'b'),
        map_get(map, 'a'),
        map_get(map, 'n'),
        ~~(map_get(map, 'l') / 2),
        ~~(map_get(map, 'o') / 2)
    )
    return ans
}
