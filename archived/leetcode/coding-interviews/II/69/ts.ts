function peakIndexInMountainArray(arr: number[]): number {
    let l = 1
    let r = arr.length - 2
    while (l < r) {
        const m = l + ~~((r - l) / 2)
        const nl = arr[m - 1],
            n = arr[m],
            nr = arr[m + 1]
        if (nl < n && n > nr) return m
        else if (nl < n && n < nr) l++
        else r--
    }
    return l
}
