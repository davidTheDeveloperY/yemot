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
from yemot import Client, System, Campaign, Ivr
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
## שימוש במודול System
קריאה למודול
```
system = System(client)
```
לקבלת פרטי המערכת
```
system.system_info()
```
עדכון פרטי מערכת
שלח את הנתון שהינך רוצה לעדכן
```
system.set_system_info(name='שם', email='אימייל', organization='חברה', contact_name='שם איש קשר', phones='טלפון', invoice_name='שם לחשבונית', invoice_address='כתובת לחשבונית', fax='פקס', access_password='סיסמת גישה', record_password='סיסמת הקלטות')
```
לקבלת רשימת חיובי יחידות
ניתן לשלוח מאיזה מספר נתון שימשוך
וכן כמה נתונים שימשוך ברירת מחדל 100
```
system.get_transactions(first='מספר התחלתי', limit='כמה נתונים')
```
העברת יחידות
```
system.transfer_units(destination='מספר מערכת להעברה', amount='כמות יחידות')
```
רשימת השיחות הפעילות במערכת
```
system.get_incoming_calls()
```
העלאת קובץ למערכת
```
system.upload_file()
```
הורדת קבצים
```
system.download_file(path=)
```
## שימוש במודול Campaign
קריאה למודול
```
camp = Campaign(client)
```
קבלת מצב כל תבניות הקמפיינים
```
camp.get_templates()
```
עדכון תבנית קמפיין
```
camp.update_template()
```
העלאת קבצי קמפיין
```
camp.upload_template_file()
```
הורדת קבצי קמפיין
```
camp.downlaoad_template_file()
```
יצירת תבנית קמפיין חדשה

מחיקת תבנית קמפיין

הצגת המספרים שברשימת התפוצה

עדכון מספר בודד ברשימת תפוצה

# הפרוייקט יעודכן בתקופה הקרובה באופן שוטף אז תתעדכנו






### References
https://f2.freeivr.co.il/post/75