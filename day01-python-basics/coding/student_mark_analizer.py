def student_marks_summary(nums):
    max_score=max(nums)
    avg_score=sum(nums)/len(nums)
    seen=set()
    duplicate=set()
    for num in nums:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    

    print(str(max_score)+" max score of students and avge"+str(avg_score)+"duplicates in the given data "+str(duplicate))


def main():
    nums=[99,89,99,90,78,63,90,63]
    student_marks_summary(nums)
if __name__=="__main__":
    main()