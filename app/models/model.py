# 22
# Delicate
# Clean
def calculate_song (form_data):
    print(form_data)
    total = 0
    for label in form_data:
        value = form_data[label][0]
        total += int(value)

    if total == 4:
        return "Clean by Taylor Swift!!"
    elif total >= 5 and total <= 10:
        return "Delicate by Taylor Swift!!"
    elif total >= 11 and total <= 16:
        return "22 by Taylor Swift!!"