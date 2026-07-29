# Cyber Security Log Analyzer
# Created by Rebeka Nyambati

login_logs = [
    {
        "username": "alex",
        "location": "Arizona",
        "status": "Success"
    },
    {
        "username": "jordan",
        "location": "Russia",
        "status": "Failed"
    },
    {
        "username": "sam",
        "location": "California",
        "status": "Success"
    },
    {
        "username": "alex",
        "location": "China",
        "status": "Failed"
    },
    {
        "username": "maria",
        "location": "Arizona",
        "status": "Success"
    }
]


failed_attempts = 0
successful_logins = 0
suspicious_activity = []


# Loop through all login records
for log in login_logs:

    if log["status"] == "Success":
        successful_logins += 1

    else:
        failed_attempts += 1


    # Identify suspicious locations
    if log["location"] in ["Russia", "China"]:
        suspicious_activity.append(log)



print("🔐 Cyber Security Log Report")
print("----------------------------")

print(f"Successful Logins: {successful_logins}")

print(f"Failed Attempts: {failed_attempts}")


print("\n⚠️ Suspicious Activity:")


# Loop through suspicious activity
for activity in suspicious_activity:

    print(
        f"""
        User: {activity['username']}
        Location: {activity['location']}
        Status: {activity['status']}
        """
    )


# While loop example
while True:

    choice = input(
        "\nWould you like to scan logs again? (yes/no): "
    )


    if choice.lower() == "no":

        print("Closing analyzer...")
        break

    elif choice.lower() == "yes":

        print("Scanning complete. No new threats detected.")

    else:

        print("Invalid option.")
