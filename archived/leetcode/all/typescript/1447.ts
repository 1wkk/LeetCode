/*
 * @lc app=leetcode.cn id=1447 lang=typescript
 *
 * [1447] 最简分数
 */

// @lc code=start

const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b))

function simplifiedFractions(n: number): string[] {
    const ans = []
    for (let deno = 2; deno <= n; deno++)
        for (let mole = 1; mole < deno; mole++)
            if (gcd(mole, deno) === 1) ans.push(`${mole}/${deno}`)
    return ans
}
// @lc code=end
