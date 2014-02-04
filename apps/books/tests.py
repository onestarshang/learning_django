#coding:utf-8
#from django.test import TestCase

# Create your tests here.
#利用manage的shell，实现一些测试语句，不是严格的testcase
#mysite(blogdemo) manage.py shell
from books.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
        city='Berkeley', state_province='CA', country='U.S.A.',
        website='http://www.apress.com/')

p1.save()


p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
        city='Cambridge', state_province='MA', country='U.S.A.',
        website='http://www.oreilly.com/'
)

p2.save()
publisher_list = Publisher.objects.all()

##调用`` Publisher.objects.all()`` 方法获取数据库中`` Publisher`` 类的所有对象。
##这个操作的幕后，Django执行了一条SQL `` SELECT`` 语句
##
##当你使用Django modle API创建对象时Django并未将对象保存至数据库内，
##除非你调用`` save()`` 方法

p1 = Publisher.objects.create(name='Apress',
        address='2855 Telegraph Avenue',
        city='Berkeley', state_province='CA', country='U.S.A.',
        website='http://www.apress.com/')
p2 = Publisher.objects.create(name="O'Reilly",
        address='10 Fawcett St.', city='Cambridge',
        state_province='MA', country='U.S.A.',
        website='http://www.oreilly.com/')
publisher_list = Publisher.objects.all()

Publisher.objects.filter(name='Apress')
##select * from table where name='Apress';
Publisher.objects.filter(country="U.S.A.", state_province="CA")
##select * from table where country = "U.S.A." and state_province = 'CA';
Publisher.objects.filter(name__contains="press")
##SELECT id, name, address, city, state_province, country, website
##FROM books_publisher
##WHERE name LIKE '%press%';

Publisher.objects.get(name="Apress")
##结果为多个或者为空，报exceptions

"""
Traceback (most recent call last):
    ...
MultipleObjectsReturned: get() returned more than one Publisher --
    it returned 2! Lookup parameters were {'country': 'U.S.A.'}


==========================

>>> Publisher.objects.get(name="Penguin")
Traceback (most recent call last):
    ...
DoesNotExist: Publisher matching query does not exist.
"""

Publisher.objects.order_by("name")
##排序
Publisher.objects.order_by("address")
Publisher.objects.order_by("-name")
##逆排序 “-”

Publisher.objects.filter(country="U.S.A.").order_by("-name")
##where ... order by ...

Publisher.objects.order_by('name')[0]
"""
SELECT id, name, address, city, state_province, country, website
FROM books_publisher
ORDER BY name
LIMIT 1;
"""

Publisher.objects.order_by('name')[0:2]
##不支持Python的负索引(negative slicing)
"""
SELECT id, name, address, city, state_province, country, website
FROM books_publisher
ORDER BY name
OFFSET 0 LIMIT 2;
"""
Publisher.objects.order_by('-name')[0]


Publisher.objects.filter(id=52).update(name='Apress Publishing')
## update()
Publisher.objects.all().update(name='Apress Publishing')
##return 2


Publisher.objects.filter(country='USA').delete()
##delete()

