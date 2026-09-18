trials = int(input("no. of trials "))
successful_trial =int ( input("no. of successful trials "))
failed_trials = trials - successful_trial
successful_rate = (successful_trial / trials)*100
failed_rate =  (failed_trials / trials)*100
print("Failed trials", failed_trials)
print("Successful rate:", successful_rate, "%")
print("Failed rate:", failed_rate, "%")
