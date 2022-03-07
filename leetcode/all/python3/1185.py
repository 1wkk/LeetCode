class Solution:
    def dayOfTheWeek(self, day: int, month: int, y: int) -> str:
        weeks = [
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
        ]
        if month < 3:
            month += 12
            y -= 1
        return weeks[
            (
                y
                + y // 4
                - y // 100
                + y // 400
                + 2 * month
                + 3 * (month + 1) // 5
                + day
                + 1
            )
            % 7
        ]
