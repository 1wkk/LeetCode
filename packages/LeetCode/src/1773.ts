function countMatches(
  items: string[][],
  ruleKey: string,
  ruleValue: string
): number {
  return items.filter(([type, color, name]) => {
    if (
      (ruleKey === 'type' && ruleValue === type) ||
      (ruleKey === 'color' && ruleValue === color) ||
      (ruleKey === 'name' && ruleValue === name)
    )
      return true
    return false
  }).length
}
