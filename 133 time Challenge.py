import datetime
import pytz

timezones = {
    1: "PL",
    2: "GB",
    3: "PR",
}
print("Podaj strefę czasową lub naciśnij 0 aby wyjść: ")
for time in timezones:
    print("Wybierz {} dla {}".format(time, timezones[time]))
while True:

    ans = int(input())
    zone = pytz.country_timezones(timezones[ans])
    zone = zone[0]
    if ans in timezones:
        tz_to_disp = pytz.timezone(zone)
        print("Czas lokalny to: ",datetime.datetime.now().strftime("%A %x %X %z"))
        print("Czas UTC to: ", datetime.datetime.utcnow())
        print("Wybrano {} dla strefy {}, gdzie czas to: {}".format(ans, timezones[ans], datetime.datetime.now(tz=tz_to_disp)))
    elif ans == 0:
        break
    else:
        print("Wybierz jedną z podanych liczb")