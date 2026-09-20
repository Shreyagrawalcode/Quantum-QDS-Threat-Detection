experiment ={
    "trials": int(input("enter the trial done")),
    "successful": int(input("enter the success done")),
    "failed": int(input("enter the failed done"))
}
if experiment["successful"] + experiment["failed"] != experiment["trials"]:
    print("invalid")

else:  
    def success_rate(success,trials):
        return (success/trials)*100
    
    def failure_rate(failed , trials):
        return(failed/trials)*100
        
    success_percent = success_rate(
        experiment["successful"],
        experiment["trials"]
    )

    failure_percent = failure_rate(
        experiment["failed"],
        experiment["trials"]
    )

    print ("Trials :" ,experiment["trials"])
    print("successful :" , experiment["successful"])
    print("failed :" ,experiment["failed"])
    print("success percent :" ,success_percent)
    print("failure percent :" ,failure_percent)
        