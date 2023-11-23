
[![Django Model](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_3.png)]()
# Django Model 
A model with various CPU specifications

# Prompt

```
class Zhuban(models.Model):
    modelnum= models.CharField(max_length=50,  verbose_name='CPU')
    brand= models.CharField(max_length=50, verbose_name='CPU级别')
    chipset=models.CharField(max_length=50, verbose_name='接口')
    interface=models.CharField(max_length=50, verbose_name='核心数')
    type=models.CharField(max_length=50, verbose_name='线程数')
    caonum=models.CharField(max_length=50, verbose_name='睿频频率')
    supportfrequency=models.CharField(max_length=50, verbose_name='基础频率')
    m2disk=models.CharField(max_length=50, verbose_name='未锁频')
    platetype= models.CharField(max_length=50, verbose_name='核显')
    supplyelectricity= models.CharField(max_length=50, verbose_name='电源预留功耗（W）')
    wifinetworkcard=models.CharField(max_length=50, verbose_name='价格')
    colour=models.CharField(max_length=50, verbose_name='价格')
    price = models.CharField(max_length=50, verbose_name='价格')
    budgetkeys = models.CharField(max_length=50, verbose_name='价格')
    requirekeys = models.CharField(max_length=50, verbose_name='价格')
    link = models.URLField(verbose_name='链接')
用了什么函数
```

## Conversation

**ASSISTANT**: 这是一个Django模型（models.Model），其中包含了各种字段，每个字段都使用了CharField函数来指定其数据类型为字符型，并指定最大长度。URLField函数被用于链接字段。



此外，还有一些其他的参数被使用，如verbose_name，它们并不是函数，而是在Django框架中用来控制模型元数据（metadata）的属性。


