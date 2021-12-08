
# בדוק שיש לך את הגירסא המעודכנת של pip
Windows
```
py -m pip install --upgrade pip
```

Linux/MAC OS
```
python3 -m pip install --upgrade pip
```


# התקנת הפרוייקט
Windows
```
py -m pip install yemot
```

Linux/MAC OS
```
python3 -m pip install yemot
```

# איך להשתמש בפרוייקט
כלול את הספריה בקובץ שלך
```
from yemot import Yemot
```
וחבר אותו למשתנה, כשאתה קורא לפרוייקט אתה חייב לשלוח את המספר מערכת והסיסמא
```
yemot = Yemot(username='0xxxxxxxxx', password='xxxxxxx')
```

כעת תוכל לבצע את הקריאות

בשביל להתחבר מחדש אחרי ניתוק או ממערכת אחרת
```
yemot.login(username='0xxxxxxxxx', password='xxxxxxx')
```
לניתוק
```
yemot.logout()
```
לקבלת פרטי המערכת
```
yemot.system_info()
```
עדכון פרטי מערכת
שלח את הנתון שהינך רוצה לעדכן
```
yemot.set_system_info(name='שם', email='אימייל', organization='חברה', contact_name='שם איש קשר', phones='טלפון', invoice_name='שם לחשבונית', invoice_address='כתובת לחשבונית', fax='פקס', access_password='סיסמת גישה', record_password='סיסמת הקלטות')
```
לקבלת רשימת חיובי יחידות
ניתן לשלוח מאיזה מספר נתון שימשוך
וכן כמה נתונים שימשוך ברירת מחדל 100
```
yemot.get_units_transactions(first='מספר התחלתי', limit='כמה נתונים')
```
העברת יחידות
```
yemot.transfer_units(destination='מספר מערכת להעברה', amount='כמות יחידות'
```
רשימת השיחות הפעילות במערכת
```
yemot.incoming_calls()
```
# הפרוייקט תתעדכן בתקופה הקרובה באופן שוטף אז תתעדכנו






### References
