import os
import datetime



DATE_OF_FIRST_STAKE_REWARD = datetime.date(2019, 12, 22)
ORIGINAL_ADA_SUM = 10000000 # sum of ada staked
USERNAME = "YOUR_WINDOWS_USERNAME"
result = datetime.date.today() - DATE_OF_FIRST_STAKE_REWARD
DAYS_STAKING = result.days
path_to_files = f"C:\\Users\\{USERNAME}\\AppData\\Roaming\\Daedalus - Rewards v1"
if __name__ == "__main__":
    files = os.listdir(path_to_files)
    rewards_sum = 0

    for f in files:
        if f.endswith("csv"):
            path_to_file = os.path.join(path_to_files, f)
            file = open(path_to_file, 'r').readlines()
            prev = rewards_sum
            rewards_sum = sum(float(line.split(',')[1].split()[0]) for line in file[1:])
            difference = 0
            percent_gains = 0
            if not prev == 0:
                difference = rewards_sum - prev
                percent_gains = difference / ORIGINAL_ADA_SUM * 36500
            print("TOTAL REWARDS: ", round(rewards_sum,2),"|", f,"|","DIFFERENCE: ", round(difference,2), "| YEARLY %: ", percent_gains)
    print("AVERAGE YEARLY %: ", rewards_sum/DAYS_STAKING)
