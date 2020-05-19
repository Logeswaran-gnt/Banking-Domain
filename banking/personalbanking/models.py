from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Branch(models.Model):
    id = models.IntegerField(primary_key=True)
    branch_name = models.CharField(default='Chennai', max_length=30, null=False)
    address = models.CharField(max_length=30, null=False,default=None)
    def __str__(self):
        return f'{self.id} - {self.branch_name} -  {str(self.address)}'

class Loan(models.Model):
    LOAN_CHOICES = (
        ('PL', 'Personal Loan'),
        ('HL', 'Housing Loan'),
        ('VL', 'Vehicle Loan')
    )
    loan_id = models.IntegerField()
    loan_types = models.CharField(choices=LOAN_CHOICES, max_length=2, default='PL', null=False)
    interest_rate = models.FloatField()
    total_loan = models.FloatField()
    pending_amount = models.FloatField()
    def __str__(self):
        return f'{self.loan_id} - {self.loan_types}'

class Customer(models.Model):
    account_number = models.BigIntegerField(primary_key=True, null=False)#validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    ACCOUNT_CHOICES = (
        ('SB', 'Savings Account'),
        ('CA', 'Current Account')
    )
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30,null=False)
    account_type = models.CharField(max_length=2, default='SB', choices=ACCOUNT_CHOICES, null=False)
    created_time = models.DateField(auto_now_add=True, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True, related_name='customers')
    def __str__(self):
        return f'{self.account_number} - {self.firstname} -  {self.lastname} - {self.branch}'