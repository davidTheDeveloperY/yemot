# בדיקות והתקנת הפרוייקט
## בדוק שיש לך את הגירסא המעודכנת של pip
Windows
```
pip install --upgrade pip
```

Linux/MAC OS
```
python3 -m pip install --upgrade pip
```


## התקנת הפרוייקט
Windows
```
pip install yemot
```

Linux/MAC OS
```
python3 -m pip install yemot
```
## מבנה הפרוייקט
הפרוייקט מורכב מארבעה מודלים
1. Client - ניהול החיבור לימות המשיח
2. System - קבלת מידע והפעולות במערכת
3. Campaign - קבלת מידע וביצוע פעולות בקמפיינים
4. Ivr - קבלת מידע וביצוע פעולות בשלוחות
# איך להשתמש בפרוייקט
## כלול את הספריה בקובץ שלך
אפשר לכלול את כל המודלים 
```
import yemot
```
או מודול מסויים
```
from yemot import Client, System, Campaign, IVR
```
וחבר אותו למשתנה, כשאתה קורא לפרוייקט אתה חייב לשלוח את המספר מערכת והסיסמא
```
client = Client(username='0xxxxxxxxx', password='xxxxxxx')
```
כמובן אם השתמשנו ב import yemotאז צריך להשתמש ב 
```
client = yemot.Client(username='0xxxxxxxxx', password='xxxxxxx')
```
וכן בכל השאר

כעת תוכל לבצע את הקריאות

בשביל להתחבר מחדש אחרי ניתוק או ממערכת אחרת
```
client.login(username='0xxxxxxxxx', password='xxxxxxx')
```
לניתוק
```
client.logout()
```

### [לכל הפונקציות של Client](docs/CLIENT.md)

## שימוש במודול System
קריאה למודול
```
system = System(client)
```
לקבלת פרטי המערכת
```
system.system_info()
```
### [לכל הפונקציות של System](docs/SYSTEM.md)

## שימוש במודול Campaign
קריאה למודול
```
camp = Campaign(client)
```
קבלת מצב כל תבניות הקמפיינים
```
camp.get_templates()
```
### [לכל הפונקציות של Campaign](docs/CAMPAIGN.md)

## שימוש במודול IVR
קריאה למודול
```
ivr = IVR(client)
```
קבלת רשימת כל השלוחות
```
ivr.get_ivrs()
```
### [לכל הפונקציות של IVR](docs/IVR.md)


# הפרוייקט יעודכן בתקופה הקרובה באופן שוטף אז תתעדכנו






### References
https://f2.freeivr.co.il/post/75