class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        
        def isLeapYear(year):
            return 1 if year%4==0 and year%100!=0 or year%400==0 else 0
        
        def since1971(day,month,year):
            count = day + (isLeapYear(year) if month > 2 else 0)
            
            for i in range(1971,year):
                count += 365 + isLeapYear(i)
                
            count += sum(daysInMonth[:month-1])
            return count
      
        today = days[(since1971(day,month,year) - since1971(15,8,1993) )% 7]
        return today
