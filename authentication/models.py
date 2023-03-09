#from tkinter import CASCADE
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user being referenced to is deleted, the post will be deleted as well
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #str method for viewing
    def __str__(self):
        return self.title + "\n" + self.description


class MachineLearning1(models.Model):
    Loan_Purpose_CHOICES = [
        ('car','Car'),
        ('house','House'),
        ('other','Other'),
        ('moving','Moving'),
         ('wedding','Wedding'),
        ('medical','Medical expenses'),
        ('educational','Educational'),
        ('credit_card','Credit card'),
        ('major_purchase','Major purchase'),
        ('small_business','Small business (SME)'),
        ('vacation', 'Vacation or Holiday'),
        ('renewable_energy','Renewable energy'),
        ('home_improvement','Home improvement'),
        ('debt_consolidation', 'Debt consolidation'),
    ]
    Application_Type_CHOICES =[
        ('INDIVIDUAL', 'Individual Application'),
        ('JOINT', 'Joint Application (two co-borrowers)'),
        ('DIRECT_PAY', 'Other'),
    ]
    Verification_Status_CHOICES = [
        ('Verified', 'LO Verified'),
        ('Source Verified', 'Source Verified'),
        ('Not Verified','Not Verified'),
    ]
    Home_OwnerShip_CHOICES = [
        ('MORTGAGE', 'Mortgage'),
        ('RENT', 'Rented'),
        ('OWN','Owned'),
        ('OTHER','Other'),
    ]
    Earliest_CR_Line_CHOICES = [(earliest_cr_linez, earliest_cr_linez) for earliest_cr_linez in range(1990, 2022)]

    Grade_CHOICES = [
        ('A','A - Lowest Risk'),
        ('B','B  '),
        ('C','C '),
        ('D','D - Medium Risk'),
        ('E','E '),
        ('F','F '),
        ('G','G - Highest Risk'),
    ]
        
    Terms_CHOICES = [
        ('36','36 months'),
        ('60','60 months'),
    ]
    Public_Bankruptcies_CHOICES = [
        ('0','Never'),
        ('1','Only one time'),
        ('2','Two or more times')
    ]

    # define form fields
    Purpose = models.CharField(max_length=50, choices=Loan_Purpose_CHOICES)
    Application_type = models.CharField(max_length=50, choices=Application_Type_CHOICES )
    Verification_status = models.CharField(max_length=50, choices=Verification_Status_CHOICES )
    Home_ownership = models.CharField(max_length=50, choices=Home_OwnerShip_CHOICES )
    Earliest_cr_line = models.IntegerField(choices=Earliest_CR_Line_CHOICES)
    grade = models.CharField(max_length=20, choices=Grade_CHOICES )
    #sub_grade = models.CharField(max_length=2, choices=SUBGRADE_CHOICES.get(grade, ()))
    Loan_amount = models.IntegerField()
    Terms = models.CharField(max_length=20, choices=Terms_CHOICES )
    Interest_rate = models.FloatField()
    Annual_income = models.IntegerField()
    Monthly_debt_income_ratio = models.FloatField()
    Open_accounts = models.IntegerField()
    Revol_util = models.FloatField()
    Mort_accounts = models.IntegerField()
    Public_bankruptcies = models.CharField(max_length=20, choices=Public_Bankruptcies_CHOICES)


    