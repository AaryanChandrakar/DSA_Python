# Priority Task Scheduler for AI Jobs
"""
Problem Statement:
An AI research lab schedules multiple ML training jobs. Each job has:
• job_id
• priority (1 = highest)
• execution_time
Jobs must be executed based on:
1. Higher priority first
2. If priority is same → smaller execution time
3. If still same → smaller job_id
Return the order of execution.
EXAMPLE Sample Input:
4
201 2 30
202 1 20
203 1 25
204 2 10

Sample Output:
202 203 204 201
"""

n = int(input("Enter number of jobs: "))

jobs = []
print("Enter job details in format: job_id priority execution_time")
for i in range(n):
    job_id, priority, execution_time = map(int, input(f"job {i+1}:").split())
    jobs.append((job_id, priority, execution_time))


def schedule_jobs(jobs):
    jobs.sort(key=lambda x: (x[1], x[2], x[0]))
    sequence = " ".join(str(job[0]) for job in jobs)
    return sequence

print("Execution Order:")   
print(schedule_jobs(jobs))

