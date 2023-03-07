from django.shortcuts import redirect, render
# for registering user in a database
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, CommentForm, MachineLearning1Form
# use decorators to redirect us to /login if not logged in : cannot make comments if not logged in
from django.contrib.auth.decorators import login_required, permission_required
from .models import Comment, MachineLearning1
import joblib  # for machine learning model
import pandas as pd
#from xgboost import set_config
#set_config(verbosity=0, enable_categorical=True)

# Create your views here.


# redirect us to login if not logged in already
@login_required(login_url="/login")
def home(request):
    return render(request, "authentication/home.html")


# redirect us to login if not logged in already
@login_required(login_url="/login")
def reviews(request):
    comments = Comment.objects.all()  # this gives all the comments that we have
    if request.method == "POST":
        # getting the comment_id by clicking e delete btn.
        comment_id = request.POST.get("comment_id")
        Comment.objects.filter(id=comment_id).delete()

        # getting user_id to ban user by clicking the btn
        user_id = request.POST.get("user_id")
        user = User.objects.filter(id=user_id).first()
        Group.objects.get(name='default').user_set.remove(user)
    return render(request, "authentication/reviews.html", {"comments": comments})


# redirects to login if not supposed to access comments
@permission_required("authentication.add_comment", login_url="/login", raise_exception=True)
# if not logged in, this redirects us to login if we click comment
@login_required(login_url="/login")
def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # by default commit=T; we do not want to save the form yet cz its incomplete so we add user as well
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()  # saves creates 1 in the database
            return redirect("/home")
    else:
        form = CommentForm()
    return render(request, "authentication/create_comment.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  # creates a new form
        if form.is_valid():
            user = form.save()  # this creates new user
            login(request, user)  # after that, we try to login new user
            # after new user has sucessfully signed in, it redirects the user to the sign in page or can be log in page
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})


def create_ML1(request):

    import pickle
    import xgboost as xgb
    from sklearn.ensemble import BaggingClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.pipeline import Pipeline
    from joblib import load

    # load the preprocessor
    preprocessor = joblib.load('preprocessor.joblib')

    # Load the models using open
    with open('xgb_model2.pickle', 'rb') as f:
        xgboost_model, feature_names = pickle.load(f)

    # 'C:\\Users\\hp\\Desktop\\CREDIT SCORE\\Ratings\\xgb_model2.pkl'

    if request.method == 'POST':
        form = MachineLearning1Form(request.POST)
        if form.is_valid():

            # load the models
            #preprocessor = joblib.load('preprocessor.gz')
            #xgboost_model = joblib.load('xgb_model2.joblib')
            #random_forest_model = joblib.load('random_forest_model.joblib')
            boosting_model = joblib.load('boosting_model.gz')
            #log_regression_model = joblib.load('log_regression_model.joblib')

            #random_forest_model = load('random_forest_model.pkl')
            #boosting_model = load('boosting_model.pkl')
            #log_regression_model = load('log_regression_model.pkl')

            # access clean form data after validation is performed
            Loan_amount = form.cleaned_data['Loan_amount']
            Interest_rate = form.cleaned_data['Interest_rate']
            Annual_income = form.cleaned_data['Annual_income']
            Mort_accounts = form.cleaned_data['Mort_accounts']
            Open_accounts = form.cleaned_data['Open_accounts']
            Monthly_debt_income_ratio = form.cleaned_data['Monthly_debt_income_ratio']
            Revol_util = form.cleaned_data['Revol_util']
            Terms = int(form.cleaned_data['Terms'])
            Application_type = form.cleaned_data['Application_type']
            grade = form.cleaned_data['grade']
            Purpose = form.cleaned_data['Purpose']
            Home_ownership = form.cleaned_data['Home_ownership']
            Earliest_cr_line = form.cleaned_data['Earliest_cr_line']
            Public_bankruptcies = int(form.cleaned_data['Public_bankruptcies'])
            Verification_status = form.cleaned_data['Verification_status']

            input_variables = [[Loan_amount, Interest_rate, Annual_income, Mort_accounts, Open_accounts, Monthly_debt_income_ratio,
                                Revol_util, Terms, Application_type, Purpose, grade, Home_ownership, Earliest_cr_line, Public_bankruptcies, Verification_status]]
            feature_names = ['loan_amnt', 'int_rate', 'annual_inc', 'mort_acc', 'open_acc', 'dti', 'revol_util', 'term',
                             'application_type', 'purpose', 'grade', 'home_ownership', 'earliest_cr_line', 'pub_rec_bankruptcies', 'verification_status']

            # create a dataframe
            df = pd.DataFrame(input_variables, columns=feature_names)

            # transform new data using preprocessor model
            X_test = preprocessor.transform(df)

            # create a dmatrix for xgboost model
            dtest = xgb.DMatrix(X_test)

            # predictions of all models (probability predictions)
            xg_pred = xgboost_model.predict(dtest)[0]
            #rf_pred = round(random_forest_model.predict_proba(input_variables)[0][1], 4)
            bg_pred = round(boosting_model.predict_proba(input_variables)[0][1], 3)
            #lg_pred = round(log_regression_model.predict_proba(input_variables)[0][1], 3)
            #xg_pred = 0
            rf_pred = None
            lg_pred = None

            # Actual predictions of output variable
            #rf_pred  = random_forest_model.predict(dtest)
            #bg_pred = boosting_model.predict(dtest)
            #lg_pred = log_regression_model.predict(dtest)

            # Convert the DataFrame to HTML; classes="table" is code from css
            html_table1 = df.iloc[:, :8].to_html(index=False, header=True, classes="table").replace(
                '<table', '<table style="text-align:center"')
            html_table2 = df.iloc[:, 8:].to_html(index=False, header=True, classes="table").replace(
                '<table', '<table style="text-align:center"')
            # Add style to the header row
            html_table1 = html_table1.replace(
                '<th>', '<th style="color:black;">')
            html_table2 = html_table2.replace(
                '<th>', '<th style="color:black;">')

            # if prediction[0] > 0.7:
            #ans = 'Fully Charged'
            # else:
            #ans = 'Paid Off'

            # get results to be displayed in html content
            context = {'form': form, 'xg_pred': xg_pred, 'rf_pred': rf_pred, 'bg_pred': bg_pred,
                       'lg_pred': lg_pred, 'html_table1': html_table1, 'html_table2': html_table2}

            return render(request, 'authentication/ML1_results.html', context)
    else:
        form = MachineLearning1Form()
    return render(request, 'authentication/create_ML1.html', {'form': form})


def create_ML2(request):

    return render(request, 'authentication/create_ML2.html')
