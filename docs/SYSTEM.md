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