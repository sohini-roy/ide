#time conversion

time = input().strip();
print(list(time));
hour = 0;
mit = 0;
sec = 0;
sec = int(time[6])*10 + int(time[7]);
if(sec>60):
    sec = sec - 60;
    mit = 1 + int(time[3])*10 + int(time[4]);
    if(mit>60):
        mit = mit - 60;
        hour = 1 + int(time[0])*10 + int(time[1]);
        if(time[8] == 'p' or time[8] == 'P'):
            hour += 12;
            if(hour == 24):
                hour = 00;
    else:
        hour = int(time[0])*10 + int(time[1]);
        if(time[8] == 'p' or time[8] == 'P'):
            hour += 12;
            if(hour == 24):
                hour = 00;
else:
    mit = int(time[3])*10 + int(time[4]);
    if(mit>60):
        mit = mit - 60;
        hour = 1 + int(time[0])*10 + int(time[1]);
        if(time[8] == 'p' or time[8] == 'P'):
            hour += 12;
            if(hour == 24):
                hour = 00;
    else:
        hour = int(time[0])*10 + int(time[1]);
        if(time[8] == 'p' or time[8] == 'P'):
            hour += 12;
            if(hour == 24):
                hour = 00;
