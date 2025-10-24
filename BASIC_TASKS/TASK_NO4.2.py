target=100
for i  in range(1,target+1):
  if (i%10==0):
    
    ans=input("Are you tired? ")
    if ans=='Y' or ans =='y':
      
      ans1=input("do you want to skip rest of jumping jacks")
      if ans1=='Y' or ans1=='y':
        print(f"you have completed {i} jumping jacks ")
        break
      if ans1=='N' or ans1=='n':
        print(f"great! uptil now you have completed {i} only {target-i} jumping jacks are remaining!")
    if ans=='n' or ans=='N':
      print(f"great! uptil now you have completed {i} only {target-i} jumping jacks are remaining!")

