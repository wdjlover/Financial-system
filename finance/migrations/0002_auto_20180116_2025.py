# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminApply',
            fields=[
                ('baseapply_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finance.BaseApply')),
                ('apply_name', models.CharField(default='行政采购申请表', editable=False, max_length=32, verbose_name='申请表名称')),
                ('purchase_type', models.IntegerField(choices=[(1, '推广用品'), (2, '办公用品'), (3, '日用品'), (4, '食品'), (5, '测试机'), (6, '其他')], verbose_name='采购类别')),
                ('gooduse', models.CharField(max_length=120, verbose_name='物品用途')),
                ('apply_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.SecondType', verbose_name='申请表类型')),
            ],
            bases=('finance.baseapply',),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='物品名称')),
                ('godmdoel', models.IntegerField(choices=[(1, '大'), (2, '中'), (3, '小')], verbose_name='物品型号')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='物品价格')),
                ('note', models.CharField(max_length=64, verbose_name='商品备注')),
            ],
        ),
        migrations.AddField(
            model_name='adminapply',
            name='good',
            field=models.ManyToManyField(to='finance.Goods', verbose_name='采购商品'),
        ),
    ]