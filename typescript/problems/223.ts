function computeArea(
  ax1: number,
  ay1: number,
  ax2: number,
  ay2: number,
  bx1: number,
  by1: number,
  bx2: number,
  by2: number
): number {
  /**
   * wrap
   */
  const max = Math.max
  const min = Math.min

  /**
   * main
   */
  const rect_area_1 = (ax2 - ax1) * (ay2 - ay1)
  const rect_area_2 = (bx2 - bx1) * (by2 - by1)
  const rect_area_both = max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1))
  return rect_area_1 + rect_area_2 - rect_area_both
}
