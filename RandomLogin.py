import os;
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"Shop.settings");
import django;
django.setup();
from Login.models import UserLogin;
from faker import Faker;
urs=UserLogin.objects.all();
for x in urs:
    print(x.UserName,x.Passwords);