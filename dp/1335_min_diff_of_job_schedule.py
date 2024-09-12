class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)

        if n < d:
            return -1
        
        if n == d:
            return sum(jobs)
        
        max_job_remaining = jobs[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])
        
        @cache
        def min_diff(i, days_rem):

            # last day, finish all remaining jobs
            if days_rem == 1:
                return max_job_remaining[i]
            
            res = float('inf')
            daily_max_job_diff = 0

            for j in range(i, n - days_rem + 1):
                daily_max_job_diff = max(daily_max_job_diff, jobs[j])
                res = min(res, daily_max_job_diff + min_diff(j + 1, days_rem - 1))
        
            return res
        
        return min_diff(0, d)