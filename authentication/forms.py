#from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, MachineLearning1

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ["username","first_name", "last_name",  "email", "password1", "password2"]

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "description"]


class MachineLearning1Form(forms.ModelForm):

    class Meta:
        model = MachineLearning1
        #fields = '__all__'
        fields = ["Loan_amount","Interest_rate","Annual_income","Mort_accounts","Open_accounts","Monthly_debt_income_ratio","Mort_accounts","Revol_util","Terms", "Application_type","grade","Purpose","Home_ownership","Earliest_cr_line","Public_bankruptcies", "Verification_status"]
        widgets = {
            'Purpose': forms.Select(choices=MachineLearning1.Loan_Purpose_CHOICES),
            'Application_type': forms.Select(choices=MachineLearning1.Application_Type_CHOICES),
            'Verification_status': forms.Select(choices=MachineLearning1.Verification_Status_CHOICES),
            'Home_ownership' : forms.Select(choices=MachineLearning1.Home_OwnerShip_CHOICES),
            'Earliest_cr_line' : forms.Select(choices=MachineLearning1.Earliest_CR_Line_CHOICES ),
            'grade': forms.Select(choices=MachineLearning1.Grade_CHOICES),
            'Terms' : forms.Select(choices=MachineLearning1.Terms_CHOICES),
            'Public_bankruptcies': forms.Select(choices=MachineLearning1.Public_Bankruptcies_CHOICES),

        }

        labels = {
            'Purpose': 'Purpose of Loan Application ',
            'Application_type': 'Application Type ',
            'Verification_status': 'Select if income is verified by Loan Officer or income source ',
            'Home_ownership': 'Home Ownership Status ',
            'Earliest_cr_line': 'Earliest Credit Line for Applicant ',
            'grade': 'Loan Grading A-G ',
            'Loan_amount':'Loan Amount Applied for (in USD$) ',
            'Terms': 'The number of payments on the loan. Values are in months.',
            'Interest_rate': 'Interest Rate on the Loan (upto 30%) ',
            'Annual_income': 'Annual Income of Applicant (in USD$) ',
            'Monthly_debt_income_ratio': 'Ratio of total monthly debt payments divided by borrowers self-reported monthly income ',
            'Open_accounts': 'The number of open credit lines in the borrowers credit file ',
            'Revol_util': 'Amount of credit the borrower is using relative to all available revolving credit (Utilisation rate in %)',
            'Mort_accounts': 'Number of Mortgage Accounts ',
            'Public_bankruptcies': 'Number of public record bankruptcies'
        }


    
    
