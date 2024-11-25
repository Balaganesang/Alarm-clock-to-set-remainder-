import time
        for alarm_name, alarm_info in alarms.items():
            print("- {}: {} - Message: {}".format(alarm_name, alarm_info["time"], alarm_info["message"]))
    else:
        print("No alarms set.")

def run_alarms():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        alarms_to_snooze = []
        alarms_to_delete = []
        for alarm_name, alarm_info in alarms.items():
            if current_time == alarm_info["time"]:
                print("Alarm '{}' is ringing! Message: {}".format(alarm_name, alarm_info["message"]))
                snooze_choice = input("Do you want to snooze the alarm '{}' (yes/no)? ".format(alarm_name)).strip().lower()
                if snooze_choice == "yes":
                    alarms_to_snooze.append(alarm_name)
                else:
                    alarms_to_delete.append(alarm_name)
        
        for alarm_name in alarms_to_snooze:
            snooze_time = (datetime.strptime(alarms[alarm_name]["time"], "%H:%M:%S") + timedelta(minutes=5)).time()
            alarms[alarm_name]["time"] = snooze_time.strftime("%H:%M:%S")
            alarms[alarm_name]["snooze"] = True

        for alarm_name in alarms_to_delete:
            del alarms[alarm_name]
        
        time.sleep(1)

def main_menu():
    print("\n=== Alarm Clock Menu ===")
    print("1. Set Alarm")
    print("2. Delete Alarm")
    print("3. Display Alarms")
    print("4. Start Alarm")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == '1':
            set_alarm()
        elif choice == '2':
            delete_alarm()
        elif choice == '3':
            display_alarm()
        elif choice == '4':
            print("Alarm will start ringing according to set alarm times.")
            break
        elif choice == '5':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    run_alarms()