def greedy_job_scheduling(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    schedule = []
    profit = 0
    current_time = 0

    for job in sorted_jobs:
        job_start_time = max(job[0], current_time) 
        job_end_time = job_start_time + job[2]  
        if job_end_time <= job[1]:
            schedule.append((job[0], job[1], job[2]))
            profit += job[3]
            current_time = job_end_time

    return schedule, profit

if __name__ =='__main__':
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))
    for i in range(num_jobs):
        print(f"\nDetails for Job {i+1}:")
        release_time = int(input("Release time: "))
        deadline = int(input("Deadline: "))
        processing_time = int(input("Processing time: "))
        profit = int(input("Profit: "))
        jobs.append((release_time, deadline, processing_time, profit))

    schedule, profit = greedy_job_scheduling(jobs)
    
    print("\nOptimal Schedule:")
    print("--------------------------------------------------------------------")
    print("| Job | Release Time | Deadline | Processing Time | Profit | Scheduled |")
    print("--------------------------------------------------------------------")
    for i, job in enumerate(jobs, start=1):
        scheduled = "Yes" if job in schedule else "No"
        print(f"| {i:3} | {job[0]:13} | {job[1]:8} | {job[2]:15} | {job[3]:6} | {scheduled:9} |")
    print("--------------------------------------------------------------------")
    print(f"Maximum Profit: {profit}")
